#include<stdio.h>

int main(void)
{
	int i, k, t;
	int N;
	int P, K, L;
	long long ans;
	long long freq[1000], tmp;
	long long j;
	
	scanf("%d", &N);
	for(i=1; i<=N; i++)
	{
		ans = 0;
		scanf("%d%d%d", &P, &K, &L);
		for(j=0; j<L;j++)
		{
			scanf("%lld", &freq[j]);
		}
		for(j=0; j<L; j++)
		{
			for(k=j+1; k<L; k++)
			{
				if(freq[j]<freq[k])	
				{
					tmp = freq[j];
					freq[j] = freq[k];
					freq[k] = tmp;
				}
			}
		}
		k = 0;
		for(j = 1; j<=P; j++)
		{			
			for(t=0; t<K&&k<L; t++)
			{
				ans+=freq[k]*j;
				k++;
//				printf("%lld = + %lld * %lld \n", ans, freq[k], j);
			}
		}
		printf("Case #%d: %lld\n", i, ans);
	}
	
}
