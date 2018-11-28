#include<stdio.h>

const int MAXN = 1000;

int a[MAXN][MAXN];
int n, m;
int tempval;
int T;
int ret;

int main(void)
{
	int l0, l1, l2, l3, l4, l5;

	freopen("b1.in","r",stdin);
	freopen("b1.out","w",stdout);

	//freopen("input.txt","r",stdin);

	scanf("%d",&T);
	for(l0=1;l0<=T;l0++)
	{
		scanf("%d %d %d",&n,&m,&tempval);
		for(l1=1;l1<=n;l1++) for(l2=1;l2<=m;l2++) scanf("%1d",&a[l1][l2]);

		int ret = 0;
		for(l1=1;l1<=n;l1++) for(l2=1;l2<=m;l2++)
		{
			for(l3=1;;l3++)
			{
				if(l1-l3 < 1) break;
				if(l2-l3 < 1) break;
				if(l1+l3 > n) break;
				if(l2+l3 > m) break;
				int X = 0, Y = 0;
				for(l4=l1-l3;l4<=l1+l3;l4++)
				{
					for(l5=l2-l3;l5<=l2+l3;l5++)
					{
						if(l4 == l1-l3 && l5 == l2-l3) continue;
						if(l4 == l1-l3 && l5 == l2+l3) continue;
						if(l4 == l1+l3 && l5 == l2-l3) continue;
						if(l4 == l1+l3 && l5 == l2+l3) continue;

						X += a[l4][l5] * (l4 - l1);
						Y += a[l4][l5] * (l5 - l2);
					}
				}
				if(X == 0 && Y == 0 && l3*2+1 > ret) ret = l3*2 + 1;
			}
		}

		for(l1=1;l1<=n;l1++)
		{
			for(l2=1;l2<=m;l2++)
			{
				for(l3=1;;l3+=2)
				{
					if(l3 == 1) continue;
					if(l1+l3 > n) break;
					if(l2+l3 > m) break;

					int X = 0, Y = 0;
					int dx, dy;
					for(l4=l1;l4<=l1+l3;l4++)
					{
						dx = l4*2 - (l1*2+l3);
						for(l5=l2;l5<=l2+l3;l5++)
						{
							dy = l5*2 - (l2*2+l3);
							if(l4 == l1 && l5==l2) continue;
							if(l4 == l1 && l5==l2+l3) continue;
							if(l4 == l1+l3 && l5==l2) continue;
							if(l4 == l1+l3 && l5==l2+l3) continue;

							X += a[l4][l5] * dx;
							Y += a[l4][l5] * dy;
						}
					}


					if(X == 0 && Y == 0 && l3+1 > ret) ret = l3+1;
				}
			}
		}

		printf("Case #%d: ",l0);
		if(ret == 0) printf("IMPOSSIBLE\n");
		else printf("%d\n",ret);
	}
}