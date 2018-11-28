#include <stdio.h>
#include <memory.h>
int R,N,K,T;
int g[1001];
int sum[1001];
int next[1001];
int round[1001];
bool visit[1001];

void work_sum()
{
/*	int i,j,total;
	total=0;
	j = 1;
	for (i = 1;i <= N;i++)
	{
		if (j == i)
		{
			total += g[j];
			j = j%N+1;
		}
		while (j != i && total + g[j] > 0 && total + g[j] <= K)
		{
			total+=g[j];
			j = j%N + 1;
		}
		sum[i] = total;
		next[i] = j;
		total -= g[i];
	}
*/
	int i;
	for (i = 1;i <= N;i++)
	{
		int total = g[i];
		int j = i%N +1;
		while (j != i && total + g[j] > 0 && total + g[j] <= K)
		{
			total+=g[j];
			j = j%N+1;
		}
		next[i] =j;
		sum[i] = total;
	}
}

void work_round(int ncase)
{
	memset(visit,0,sizeof(visit));
	int i=1;
	int nr = 0;
	__int64 total = 0;
	while (!visit[i])
	{
		visit[i] = true;
		nr++;
		round[nr] = sum[i];
		total += round[nr];
		i = next[i];
	}
	__int64 total1= sum[i];
	int j = next[i];
	int cnt = 1;
	
	while (j != i)
	{
		total1+= sum[j];
		j = next[j];
		cnt++;
	}
	
	int t= (R-nr+cnt)%cnt;
	__int64 total2= 0;
	for (j = 1;j <= t;j++)
	{
		total2+=sum[i];
		i = next[i];
	}
	printf("Case #%d: %I64d\n",ncase,(R-nr+cnt)/cnt * total1 + total - total1+total2);
}

int main()
{
	freopen("d:\\C-large.in","r",stdin);
	freopen("d:\\output.txt","w",stdout);
	scanf("%d",&T);
	int i;
	for (i = 1;i <= T;i++)
	{
		scanf("%d %d %d",&R,&K,&N);
		int j;
		for (j = 1;j <= N;j++)
			scanf("%d",&g[j]);
		work_sum();

		work_round(i);

	}
	return 0;
}