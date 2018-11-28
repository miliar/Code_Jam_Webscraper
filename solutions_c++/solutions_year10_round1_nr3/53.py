#include <stdio.h>
#define N 1001000
int m[N], b[N];
int main()
{
	int i, j, l, c, r, a1, a2, b1, b2, t, ts;
	__int64 a;
	for(m[1]=1, i=2; i<N; m[i]=r, i++)
		for(l=i+1, r=2*i-1; l<r; )
		{
			c=(l+r+1)/2;
			if(i<=m[c-i]) r=c-1;
			else l=c;
		}
	for(j=1, i=1; i<N; b[i]=j, i++)
		if(i>m[j]) j++;
	for(scanf("%d", &ts), t=0; t<ts; t++)
	{
		scanf("%d%d%d%d", &a1, &a2, &b1, &b2);
		for(a=0, i=a1; i<=a2; i++)
			if(b2<b[i] || b1>m[i]) a+=b2-b1+1;
			else
			{
				if(b1<b[i]) a+=b[i]-b1;
				if(b2>m[i]) a+=b2-m[i];
			}
			printf("Case #%d: %I64d\n", t+1, a);
	}
	return 0;
}