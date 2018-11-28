#include<stdio.h>
#include<math.h>
#include<string.h>

int main()
{
	FILE *in =fopen ("small.in","r");
    FILE *out=fopen("small.out","w");
    int t;
	fscanf(in,"%d",&t);
	for(int x = 1; x <= t;x++)
	{
		int r,k,n;
		fscanf(in,"%d %d %d",&r,&k,&n);
		int groups[1005];
		for(int i = 0; i < n;i++)
			fscanf(in,"%d",&groups[i]);
		int position = 0;
		int time = 0;
		long long earn = 0;
		long long beforeearn[1005];
		int beforetimes[1005];
		for(int i = 0; i < n + 2;i++)
		{
			beforeearn[i] = -1;
			beforetimes[i] = -1;
		}
		beforeearn[0] = 0;
		beforetimes[0] = 0;
		long long roundearn = 0;
		int roundtime = 0;
		for(int z = 0;z < r;z++)
		{
			int flag[1005],j;
			long long counter = 0;
			memset(flag,0,sizeof(flag));
			for(j = position;;j++)
			{
				if (j == n)
					j = 0;
				if (counter + groups[j] <= k && flag[j] == 0)
				{
					flag[j] = 1;
					counter += groups[j];
				}
				else
					break;
			}
			time ++;
			earn += counter;
			if (beforeearn[j] > -1)
			{
				roundtime = time - beforetimes[j];
				roundearn = earn - beforeearn[j];
				position = j;
				break;
			}
			position = j;
			beforeearn[position] = earn;
			beforetimes[position] = time;
		}
		r-= time;
		if (roundtime > 0)
		{
			if (r / roundtime >= 0)
			{
				int rounds = r / roundtime;
				earn += roundearn * rounds;
				time += roundtime * rounds;
				r %= roundtime;
			}
		}
		for(int z = 0;z < r;z++)
		{
			int j;
			long long counter = 0;
			for(j = position;;j++)
			{
				if (j == n)
					j = 0;
				if (counter + groups[j] <= k)
					counter += groups[j];
				else
					break;
			}
			time ++;
			position = j;
			earn += counter;
		}
		fprintf(out,"Case #%d: %lld\n",x,earn);
	}
}