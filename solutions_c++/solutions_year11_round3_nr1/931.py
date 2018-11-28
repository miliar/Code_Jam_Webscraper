/*
ID: mythic_1
PROG: a
LANG: C++
*/

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

	int t,R,C;
	cin>>t;
	vector<string> g;
	for(int tt = 1 ; tt <= t ; tt++)
	{
		cin>>R>>C;
		g.clear();
		g.resize(R);
		for(int  i = 0 ; i < R ; i++)
			cin>>g[i];

		for(int i = 0 ; i < R -1; i++)
		{
			for(int j = 0 ; j < C -1 ; j ++)
			{
				if(g[i][j]=='#'&&g[i][j+1]=='#'&&g[i+1][j]=='#'&&g[i+1][j+1]=='#')
				{
					g[i][j]=g[i+1][j+1]='/';
					g[i+1][j]=g[i][j+1]='\\';
				}
			}
		}
		bool imp = false;
		for(int i = 0 ; i < R ; i++)
			for(int j = 0 ; j < C ; j++)
				if(g[i][j]=='#')
					imp = true;

		cout<<"Case #"<<tt<<":\n";
		if(imp)cout<<"Impossible\n";
		else
			for(int i = 0 ; i < R ; i++)
			{
				for(int j = 0 ; j < C ; j++)
				{
					cout<<g[i][j];
				}
				cout<<endl;
			}
	}

	return 0;
}
