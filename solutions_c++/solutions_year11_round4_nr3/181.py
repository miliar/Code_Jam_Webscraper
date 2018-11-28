#include <stdio.h>
#define N 1010000
long long p[N];
int main()
{
	int i, j, k, t, ts;
	long long a, n;
	for(i=2; i*i<N; i++)
		if(!p[i])
			for(j=i*i; j<N; p[j]=1, j+=i);
	for(j=0, i=2; i<N; i++)
		if(!p[i]) p[j++]=i;
	k=j;
	for(scanf("%d", &ts), t=0; t<ts; t++)
	{
		for(scanf("%lld", &n), j=1-(n==1), i=0; i<k; i++)
			for(a=p[i]; a*p[i]<=n; j++, a*=p[i]);
		printf("Case #%d: %d\n", t+1, j);
	}
	return 0;
}