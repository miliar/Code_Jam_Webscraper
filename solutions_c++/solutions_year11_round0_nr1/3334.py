
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
//#define SMALL
#define LARGE

int main()
{
#ifdef SMALL
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif
	int T,n,p,lstT,res;
	char r,lstR;
	cin>>T;
	int lst[128]={0};
	for(int t = 1 ; t <= T ; t++)
	{
		lst['O'] = lst['B'] = 1;
		lstT = res = 0;
		cin>> n;
		for(int i = 0 ; i < n ; i++)
		{
			cin>>r>>p;
			if(lstR!=r||i==0)
			{
				int temp = abs(lst[r]-p);
				if(lstT>temp)lstT=1;
				else lstT = temp-lstT+1;
				res+=lstT;
			}else
			{
				int temp = abs(lst[r]-p);
				lstT+=temp+1;
				res+=temp+1;
			}
			lst[r]=p;
			lstR =r;
		}
		cout<<"Case #"<<t<<": "<<res<<endl;
	}


	return 0;
}
