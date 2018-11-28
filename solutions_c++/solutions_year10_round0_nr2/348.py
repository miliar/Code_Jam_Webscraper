#include<cstdio>
#include<cstdlib>

int gcd(int a, int b)
{
	if(b == 0)return a;
	return gcd(b, a%b);
}

int main()
{
	int Z, T;
	scanf("%d", &T);
	for(Z = 1; Z <= T; Z ++)
	{
		int n, t[3], d[3], gg;
		int i;
		scanf("%d", &n);
		for(i = 0; i < n; i ++)
		{
			scanf("%d", &t[i]);
			if(i > 0)d[i] = abs(t[i]-t[i-1]);
			if(i == 1)gg = d[i];
			if(i > 1)
			{
				gg = gcd(gg, d[i]);
			}
		}
		int ans = 0;
		for(i = 0; i < n; i ++)
		{
			ans >?= (gg-t[i]%gg)%gg;
		}
		printf("Case #%d: %d\n", Z, ans);
	}
	return 0;
}
