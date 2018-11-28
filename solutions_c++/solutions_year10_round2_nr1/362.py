//GCC 4.4.3 C++ Compiler

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>

#define FI(i,a) for (int i=0; i<(a); ++i)
#define FOR(i,s,e) for (int i=(s); i<(e); ++i)
#define MEMS(a,b) memset(a,b,sizeof(a))
#define ISIN(s,a) (s.find(a)!=s.end())
#define VI vector <int>
#define VVI vector <vector <int> >
#define pb push_back
#define mp make_pair
#define pnt pair <int,int>
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
#define ABS(a) (((a)>0)?(a):-(a))
#define LL long long
#define U unsigned
#define ALL(a) a.begin(),a.end()

using namespace std;

#define DOUT(a) cerr << a << endl;
#define SOUT(a) cerr << a << "  ";

VVI G(20000);
map <string, int> nms;
char sc[100001];
string s;
bool was[20000];

int dfs(int v)
{
	was[v]=true;
	int sum=1;
	FI(i,(int)G[v].size())
	if (!was[G[v][i]]) sum+=dfs(G[v][i]);
	return sum;
}

int main()
{
	//freopen("sample.in","rt",stdin);
	freopen("input.in","rt",stdin);
	freopen("result.txt","wt",stdout);
	int tt;
	scanf("%d",&tt);
	FI(it,tt)
	{
		G.clear();
		nms.clear();
		int n,m; scanf("%d%d",&n,&m);
		G.resize(20000);
		int sz=1;
		FI(i,n)
		{
			cin >> s;
			s+='/';
			int pr=1;
			int p=0;
			FOR(j,1,(int)s.size())
			{
				if (s[j]=='/')
				{
					string ss=s.substr(0,j); pr=j+1;
					if (ISIN(nms,ss))
					{
						p=nms[ss];
					}
					else
					{
						nms[ss]=sz;
						G[p].pb(sz);
						p=sz;
						sz++;
					}
				}
			}
		}
		MEMS(was,0);
		int fst=dfs(0);
		FI(i,m)
				{
					cin >> s;
					s+='/';
					int pr=1;
					int p=0;
					FOR(j,1,(int)s.size())
					{
						if (s[j]=='/')
						{
							string ss=s.substr(0,j); pr=j+1;
							if (ISIN(nms,ss))
							{
								p=nms[ss];
							}
							else
							{
								nms[ss]=sz;
								G[p].pb(sz);
								p=sz;
								sz++;
							}
						}
					}
				}
		MEMS(was,0);
		int res=dfs(0)-fst;
		printf("Case #%d: %d\n",it+1,res);
	}
	return 0;
}
