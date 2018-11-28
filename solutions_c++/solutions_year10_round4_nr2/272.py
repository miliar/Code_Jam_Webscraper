#include<cstdio>
#include<algorithm>
using namespace std;
const int maxn = 4000 + 10;
const int INF = 1<<29;

int price[maxn],limit[maxn];
int n,tot;

int f[maxn][20];

int main()
{
	int TT;
	scanf("%d",&TT);
	int T = 0;
	while(TT--)
	{
		printf("Case #%d: ",++T);
		scanf("%d",&n);
		tot = 2*(1<<n)-1;
		for(int i=1;i<=tot;i++) limit[i] = 10000;
		for(int i=0;i<(1<<n);i++) scanf("%d",limit+tot-i);
		for(int i=tot-(1<<n);i;i--) scanf("%d",price+i);

		for(int i=tot;i>tot-(1<<n);i--)
		for(int j=0;j<=n+1;j++)
			if( j <=limit[i] ) f[i][j] = 0;else f[i][j] = INF;
		for(int i=tot-(1<<n);i>0;i--)
		{
			f[i][n+1] = INF;
			for(int j=0;j<=n;j++)
			{
				f[i][j] = INF;
				f[i][j] = min( f[i][j],f[2*i][j+1]+f[2*i+1][j+1]);
				f[i][j] = min( f[i][j],f[2*i][j]+f[2*i+1][j]+price[i]);
			}
		}
		printf("%d\n",f[1][0]);
	}
	return 0;
}
