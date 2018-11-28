#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <complex>
#include <cctype>
#include <algorithm>
#include <functional>
#include <cmath>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <valarray>
#include <set>
#ifdef _MSC_VER
#include <hash_set>
#include <hash_map>
using namespace stdext;
#else
#if __GNUC__ > 2
#include <ext/hash_set>
#include <ext/hash_map>
using namespace __gnu_cxx;
#else
#include <hash_set>
#include <hash_map>
#endif
#endif

template<class key>
struct hashtemp
{

	enum
	{
		bucket_size = 4, min_buckets = 8
	};
	virtual size_t operator()(const key &p) const=0;

};
using namespace std;

#define fo(i,n) for(i=0;i<(n);++i)

typedef vector<int> vi ;
typedef vector<string> vs ;
typedef vector<double> vd ;
#define sz(x) ((int)(x).size())
#define all(x) x.begin(),x.end()
#define pb(x) push_back(x)
typedef long long ll;
vector<string> b;
vector<string> a;
void reflect(vector<string>mat1,vector<string>&mat2)
{
	mat2 = mat1;
	for(int i= 0 ; i < sz(mat2) ; i ++)
		reverse(all(mat2[i]));
}
void rotate90(vector<string>mat1,vector<string>&mat2)
{
	mat2 = mat1;
	for(int i = 0 ; i < sz(mat1) ; i++)
		for(int j = 0 ; j < sz(mat1) ; j++)
			mat2[j][i] = mat1[i][j];
		reflect(mat2,mat2);
}

int N,K;
void gravity(vector<string>&b)
{
	bool great = 0;
	while(!great)
	{
		great = 1;
		for(int i = 0 ; i < N-1 ; i++)
		{
			for(int j = 0 ; j < N ; j++)
				if(b[i][j]!='.'&&b[i+1][j]=='.'){
					b[i+1][j]=b[i][j];
					b[i][j]='.';
					great = 0;
				}

		}

	}
}

bool check(vector<string>&b,char t)
{
	for(int i = 0 ; i < N ; i++)
		for(int j = 0 ; j <= N-K ; j++)
		{
			bool f = 0;
			for(int k = 0 ; k < K ; k++)
				if(b[i][j+k]!=t){
					f=1;
					break;
				}
			if(!f)return true;
			f = 0;
			for(int k = 0 ; k < K ; k++)
				if(b[j+k][i]!=t){
					f=1;
					break;
				}
			if(!f)return true;
		}
	for(int i = 0 ; i < N ; i++)
			for(int j = 0 ; j < N ; j++)
			{
				bool f = 0;
				for(int k = 0 ; k < K ; k++)
				{
					if(j+k>=N||i+k>=N||b[i+k][j+k]!=t){
						f=1;
						break;
					}
				}
				if(!f)return true;
				f = 0;
				for(int k = 0 ; k < K ; k++)
				{
					if(j-k<0||i+k>=N||b[i+k][j-k]!=t){
						f=1;
						break;
					}
				}
				if(!f)return true;
			}

	return false;
}

int main()
{
	freopen("A-large.in","rt",stdin);
	freopen("a.out","wt",stdout);


	int tt;
	cin>>tt;
	for(int t = 0 ; t < tt ; t++)
	{
		cin>>N>>K;
		a.clear();
		a.resize(N);
		for(int i = 0 ; i < N ; i++)
		{
			cin>>a[i];
		}
		rotate90(a,b);
		gravity(b);
		/*cerr<<endl<<endl;
		for(int i = 0 ; i < N ; i++)
			cerr<<b[i]<<endl;
		cerr<<endl<<endl;*/
		printf("Case #%d: ",t+1);
		bool r = check(b,'R');
		bool bl=check(b,'B');
		if(r&&bl)cout<<"Both"<<endl;else
		if(r)cout<<"Red"<<endl;else
		if(bl)cout<<"Blue"<<endl;else
			cout<<"Neither"<<endl;




	}


	return 0;
}
