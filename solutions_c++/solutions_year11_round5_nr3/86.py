#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>
using namespace std;
typedef long long ll;
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define P 1000003
#define N 10010
int n,m;
int getN(int x,int y){return x*m+y;}
vector<pair<int,int> > E;
vector<int> A[N],B[N];
bool v[N];int d[N];
int main()
{
	int _;scanf("%d",&_);
	for(int __=1;__<=_;__++)
	{
		scanf("%d%d",&n,&m);
		E.clear();
		for(int i=0;i<n*m;i++)
			A[i].clear(),B[i].clear();
		for(int i=0;i<n;i++)
		{
			char s[111];
			scanf("%s",s);
			for(int j=0;j<m;j++)
			{
				if(s[j]=='-')
					E.pb(mp(getN(i,j),getN(i,(j+1)%m))),
					E.pb(mp(getN(i,j),getN(i,(j-1+m)%m)));else
				if(s[j]=='|')
					E.pb(mp(getN(i,j),getN((i+1)%n,j))),
					E.pb(mp(getN(i,j),getN((i-1+n)%n,j)));else
				if(s[j]=='\\')
					E.pb(mp(getN(i,j),getN((i+1)%n,(j+1)%m))),
					E.pb(mp(getN(i,j),getN((i-1+n)%n,(j-1+m)%m)));else
				if(s[j]=='/')
					E.pb(mp(getN(i,j),getN((i+1)%n,(j-1+m)%m))),
					E.pb(mp(getN(i,j),getN((i-1+n)%n,(j+1)%m)));
			}
		}
		for(int i=0;i<(int)E.size();i++)
			A[E[i].fi].pb(E[i].se),
			B[E[i].se].pb(E[i].fi);
		int S=(1<<(n*m));
		memset(v,0,sizeof v);
		for(int i=0;i<(1<<(n*m));i++)
		{
			memset(d,0,sizeof d);
			for(int j=0;j<n*m;j++)
				d[A[j][(i>>j)&1]]++;
			for(int j=0;j<n*m;j++)
				if(d[j]!=1){S--;break;}
		}
		printf("Case #%d: %d\n",__,S);
	}
	return 0;
}

