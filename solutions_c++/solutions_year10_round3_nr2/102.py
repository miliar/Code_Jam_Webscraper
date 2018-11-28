#include <stdio.h>

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);	
	long long l,p, c;
	int ti, k, ans, T;
	scanf("%d", &T);
	for (ti=1; ti<=T; ti++)
	{
		scanf("%I64d%I64d%I64d", &l, &p, &c);
		k=0;
		while (l*c<p)
		{
			l*=c;
			k++;
		}
		ans=0;
		while (k>0)
		{
			ans++;
			k>>=1;
		}
		printf("Case #%d: %d\n", ti, ans);
	}
	return 0;
}
