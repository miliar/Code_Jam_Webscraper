#include <stdio.h>
#define N 50
char s[N];
int l[N];
int main()
{
	int i, j, k, t, ts, r, n;
	for(scanf("%d", &ts), t=0; t<ts; t++)
	{
		for(r=0, scanf("%d", &n), i=0; i<n; l[i]=j, i++)
			for(scanf("%s", s), j=n-1; j>=0 && s[j]=='0'; j--);
		for(r=0, i=0; i<n; i++)
		{
			for(j=i; j<n && l[j]>i; j++);
			for(; j>i; k=l[j], l[j]=l[j-1], l[j-1]=k, r++, j--);
		}
		printf("Case #%d: %d\n", t+1, r);
	}
	return 0;
}