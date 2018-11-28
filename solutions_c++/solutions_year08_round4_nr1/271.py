#include <cstdio>
#include <vector>
#define pb push_back
#define fi first
#define se second
#define INF 1000000000
using namespace std;
typedef long long ll;
typedef pair<int,int> pi;
int solve()
{
	int t[10002];
	int d[10002];
	int w[10002][2];
	int n,m;
	scanf("%d %d",&n,&m);
	for (int i=0; i<=n; i++)
	{
		w[i][0]=INF;
		w[i][1]=INF;
	}
	for (int i=1; i<=n/2; i++)
	{
		int a,b;
		scanf("%d %d",&a,&b);
		t[i]=a;
		d[i]=b;
	}
	for (int i=n/2+1; i<=n; i++)
	{
		int a;
		scanf("%d",&a);
		t[i]=a;
		d[i]=0;
		w[i][a]=0;
	}
	for (int i=n/2; i>0; i--)
	{
		if (t[i]==1||d[i]==1)
		{
			w[i][0]=min(w[i][0],w[i*2][0]+w[i*2+1][0]+(t[i]==0));
			w[i][0]=min(w[i][0],w[i*2][1]+w[i*2+1][0]+(t[i]==0));
			w[i][0]=min(w[i][0],w[i*2][0]+w[i*2+1][1]+(t[i]==0));
			w[i][1]=min(w[i][1],w[i*2][1]+w[i*2+1][1]+(t[i]==0));
		}
		if (t[i]==0||d[i]==1)
		{
			w[i][1]=min(w[i][1],w[i*2][1]+w[i*2+1][1]+(t[i]==1));
			w[i][1]=min(w[i][1],w[i*2][1]+w[i*2+1][0]+(t[i]==1));
			w[i][1]=min(w[i][1],w[i*2][0]+w[i*2+1][1]+(t[i]==1));
			w[i][0]=min(w[i][0],w[i*2][0]+w[i*2+1][0]+(t[i]==1));
		}
		//printf("%d: %d %d\n",i,w[i][0],w[i][1]);
	}
	if (w[1][m]==INF) return -1;
	return w[1][m];
}
		
int main()
{
	int tests;
	scanf("%d",&tests);
	for (int u=1; u<=tests; u++)
	{
		int w=solve();
		if (w>=0) printf("Case #%d: %d\n",u,w);
		else printf("Case #%d: IMPOSSIBLE\n",u);
	}
}
