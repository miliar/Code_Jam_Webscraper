#include <stdio.h>
#include <string.h>
#define MAXN 1005

unsigned long long g[MAXN];
unsigned long long val[MAXN];
unsigned long long flag[MAXN];
int n, k, r;

long long Process()
{
	memset(flag, -1, sizeof(flag));
	memset(val, 0, sizeof(val));
	unsigned long long i = 0; 
	unsigned long long sum = 0;
	unsigned long long t = 0;
	unsigned long long p;
	unsigned long long cnt = 0;
	while(1)
	{
		if(sum + g[i%n] > k)
		{
			p = (i + n - 1) % n;
			if(flag[p] != -1)
				break;
			else 
			{
				flag[p] = t++;
				val[p] = sum;
			}
			sum = 0;	
		}	
		sum += g[i%n];
		i ++;		
	}
	long long j;
	if(r <= t)
	{
		for(j = 0; j < n; j ++)
		{
			if(flag[j] >= 0 && flag[j] < r)	
			{
				cnt += val[j];	
			}
		}	
		return cnt;
	}
	else
	{
		cnt = 0;
		unsigned long long be = sum;
		for(j = 0; j < n; j ++)	
		{
			if(flag[j] >= 0 && flag[j] <= flag[p])
				cnt += val[j];	
			if(flag[j] > flag[p])
				be += val[j];
		}
		r = r - flag[p] - 1;
		unsigned long long tt = r / (t - flag[p]);
		cnt += be * tt ;
		unsigned long long q = r % (t - flag[p]) ;
		for(j = 0; j < n; j ++)
		{
			if(flag[j] > flag[p] && flag[j] <= flag[p] + q)
				cnt += val[j];	
		}
		
	}
	return cnt;			
}


long long work()
{
	unsigned long long cnt = 0;
	scanf("%d%d%d",&r, &k, &n);
	unsigned long long i;
	unsigned long long sum = 0;
	for(i = 0; i < n; i ++)
	{
		scanf("%d", &g[i]);
		sum += g[i];
	}
	if(sum <= k)	return sum * r ;

	return Process();
}


int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int kase;
	int t;
	scanf("%d", &t);
	for(kase = 1; kase <= t; kase ++)
	{	
		if(kase == 50)	
			t = 50;	
		printf("Case #%d: %I64d\n", kase, work());
				
	}	
	return 0;	
}
