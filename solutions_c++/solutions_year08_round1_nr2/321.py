#include <stdio.h>

int KASE;
int N,M;
int FLAG[110][11][2];
int ans , BTANS;
int GETNUM(int v)
{
	int num =0;
	while (v)
	{
		num+=v &0x01;
		v >>=1;
	}
	return num;
}
int is_ok(int index, int nbit, int ans)
{
	index >>=(nbit-1);
	if ((index &0x01) == ans) return 1;
	else return 0;
}
int check(int index)
{
	int i,j,k,ttt;
	for (i = 0; i < M; i ++)
	{
		ttt = 0;
		for (j = 1; j <= FLAG[i][0][0]; j ++)
			if (is_ok(index, FLAG[i][j][0], FLAG[i][j][1])) 
			{
				ttt = 1;
				break;
			}
		if (!ttt) return 0;
	}
	return 1;
}
int main()
{
	int i,j,MAX, found,tmp;
	freopen("B-small-attempt0_my.in","r",stdin);
	freopen("B-small-attempt0.out_my.txt", "w",stdout);
	scanf("%d",&KASE);
	for (int kase = 1;  kase <= KASE; kase++)
	{
		scanf("%d %d",&N, &M);
		for (i = 0; i < M; i ++)
		{
			scanf("%d", &FLAG[i][0][0]);
			for (j = 1; j <= FLAG[i][0][0]; j ++)
				scanf("%d %d", &FLAG[i][j][0],&FLAG[i][j][1]);
		}
		MAX = 1;
		for (i = 0; i < N; i ++)
			MAX *=2;
		found = 0;

		for (i =0; i < MAX; i ++)
		{
			if (check(i))
			{
				if (!found)
				{
					found = 1;
					ans = i;
					BTANS = GETNUM(ans);
				}
				else 
				{
					int tmp = GETNUM(i);
					if (tmp < BTANS)
					{
						BTANS = tmp;
						ans = i;
					}
				}
			}
		}
		if (!found) printf("Case #%d: IMPOSSIBLE\n",kase);
		else 
		{
			printf("Case #%d:",kase);
			tmp = ans;
			for (i =0; i < N; i ++)
			{
				printf(" %d", tmp &0x01);
				tmp>>=1;
			}
			printf("\n");
		}
	}
	return 0;
}
