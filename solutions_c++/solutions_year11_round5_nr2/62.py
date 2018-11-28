#include <stdio.h>
#define N 10010
int h[N];
int main()
{
	int t, ts, n, i, j, r, k;
	for(scanf("%d", &ts), t=0; t<ts; t++)
	{
		for(i=0; i<N; h[i]=0, i++);
		for(scanf("%d", &n), i=0; i<n; scanf("%d", &j), h[j]++, i++);
		for(r=N, i=0; i<N; i++)
			if(h[i]>h[i+1])
			{
				for(j=i, k=0; j>=0 && h[j]>0; h[j]--, k++, j--);
				if(k<r) r=k;
				i--;
			}
		if(r==N) r=0;
		printf("Case #%d: %d\n", t+1, r);
	}
	return 0;
}