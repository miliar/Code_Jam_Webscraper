#include <cstdio>

int n;
int p[5];

int _abs(int a)
{
	if(a < 0) return -a;
	return a;
}

int euclid(int a, int b)
{
	int c;
	while(c = a % b) { a = b; b = c; }
	return b;
}

int main()
{
	int t, i, j, z, gcd, ans;

	z = 1;
	scanf("%d", &t);
	while(t > 0)
	{
		scanf("%d", &n);
		for(i = 0; i < n; i++)
			scanf("%d", &p[i]);
		gcd = 0;
		for(i = 0; i < n; i++)
			for(j = i+1; j < n; j++)
			{
				if(p[i] != p[j])
					gcd = euclid(gcd, _abs(p[i]-p[j]));
			}
		
		ans = (gcd - (p[0] % gcd)) % gcd;
		printf("Case #%d: %d\n", z++, ans);
		t--;
	}

	return 0;
}