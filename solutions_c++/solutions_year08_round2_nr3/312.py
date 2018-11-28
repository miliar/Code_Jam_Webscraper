#include <cstdio>
#include <cstring>

using namespace std;

int a[6000];
char free[6000];
int K, n, d;

void calc(void)
{
	int i, j, cnt;
	
	memset(free, 1, sizeof free);
	j=1;
	for(i = 1; i<= K; i++)
	{
		//j=1;
		cnt=0;
		while(cnt<i)
		{
			cnt += free[j];	
			if(cnt<i)
			{
				++j;
				if(j>K)
				{
					j=1;
				}
			}
		}
		//printf("asq %d\n", j);
		
		a[j] = i;
		free[j] = 0;
	}
}

int main(void)
{
	int T, i, j;	
	
	scanf("%d", &T);
	
	for(i=1; i<=T; ++i)
	{
		fprintf(stderr, "%d\n", i);
		scanf("%d %d", &K, &n);
		printf("Case #%d:", i);
		calc();
		for(j=0; j<n; ++j)
		{
			scanf("%d", &d);
			printf(" %d", a[d]);
		}
		printf("\n");
	}
	return 0;
}
