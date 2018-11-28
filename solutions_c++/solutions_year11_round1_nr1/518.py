#include<cstdio>
#include<cstring>

long long N;
int Pd, Pg;

int gcd(int a, int b)
{
	int r;
	do
	{
		r = a % b; a = b; b = r;
	} while (r);
	return a;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt","w", stdout);
	int cases;
	scanf("%d" , &cases);
	for (int ca = 1; ca <= cases; ++ca)
	{
		scanf("%lld%d%d", &N, &Pd, &Pg);
		bool ok;
		if (Pg == 0 && Pd != 0) ok = false;
		else if (Pg == 100 && Pd != 100) ok = false;
		else
		{
			int r = gcd(Pd, 100);
			int d = 100 / r;
			if (N >= d) ok = true; else ok = false;
		}
		printf("Case #%d: " , ca);
		if (ok) puts("Possible"); else puts("Broken");
	}
}
