#include <stdio.h>
#define maxm 200
#define maxn 20
int n,m,ans;
int map[maxm][maxn + maxn + maxn][2];
int num[maxm];
int main(void)
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout);
	int C;
	scanf("%d",&C);
	for (int cases = 1;cases <= C;cases++)
	{
		scanf("%d",&n);
		scanf("%d",&m);
		for (int i = 0;i < m;i++)
		{
			scanf("%d",&num[i]);
			for (int j = 0;j < num[i];j++) scanf("%d%d",&map[i][j][0],&map[i][j][1]);
		}
		ans = -1;
		for (int state = 0;state < 1 << n;state++)
		{
			bool ok = true;
			for (int j = 0;j < m;j++)
			{
				bool now = false;
				for (int k = 0;k < num[j];k++) if (((state >> (map[j][k][0] - 1)) & 1) == map[j][k][1])
				{
					now = true;
					break;
				}
				if (!now)
				{
					ok = false;
					break;
				}
			}
			if (ok)
			{
				ans = state;
				break;
			}
		}
		printf("Case #%d: ",cases);
		if (ans != -1)
		{
			printf("%d",ans & 1);
			for (int i = 1;i < n;i++) printf(" %d",(ans >> i) & 1);
			printf("\n");
		}
		else {printf("IMPOSSIBLE\n");}
	}
	return 0;
}
