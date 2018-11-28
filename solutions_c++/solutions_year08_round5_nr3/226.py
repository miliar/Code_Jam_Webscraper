#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <deque>
#include <list>
#include <map>
#include <set>
using namespace std;
#define all(a) (a).begin(),(a).end()
#define mset(a,v) memset(a,v,sizeof(a))
#define pb push_back
#define sz(a) a.size()
#define rep(i,n) for(i=0; i<n; i++)
#define forr(i,a,b) for(i=a; i<=b; i++)
#define ford(i,a,b) for(i=a; i>=b; i--)
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define X first
#define Y second
typedef long long ll;
typedef vector<int> VI;

int U,N, i,j, u,v, n,m, l;
char a[100][100];
int d[100][1<<12];

int main()
{
	freopen("c-small.in","r",stdin);//large-small
	freopen("c-small.out","w",stdout);
	scanf("%d",&N);
	rep(U,N)
	{
		mset(a,0); mset(d,0);
		scanf("%d%d",&n,&m);
		rep(i,n) scanf("%s",a[i]);
		rep(u,1<<n)
		{
			d[0][u]=0;
			rep(i,n) if(u&(1<<i))
			{
				d[0][u]++;
				if(a[i][0]=='x') { d[0][u]=-1; break; }
			}
		}

		forr(j,1,m-1) rep(u,1<<n)
		{
			d[j][u]=0;
			rep(i,n) if(u&(1<<i))
			{
				d[j][u]++;
				if(a[i][j]=='x') { d[j][u]=-1; break; }
			}
			if(d[j][u]==-1) continue;
			l=-1;
			rep(v,1<<n) if(d[j-1][v]!=-1)
			{
				bool t=1;
				rep(i,n) if(u&(1<<i))
				{
					if( ((v&(1<<i))>0) || ((v&(1<<(i+1)))>0) || ((v&(1<<(i-1)))>0) ) { t=0; break; }
				}
				if(t) l=max(l, d[j-1][v]);
			}
			if(l==-1) d[j][u]=-1;
			else d[j][u]+=l;
		}
		l=0;
		rep(u,(1<<n)) l=max(l, d[m-1][u]);
		printf("Case #%d: %d\n",U+1,l);		
	}
	return 0;
}
