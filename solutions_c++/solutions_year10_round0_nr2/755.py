#include <stdio.h>
#include <algorithm>

using namespace std;

long long gcd(long long x, long long y)
{
	if (x<y) swap(x, y);
	if (y==0) return x;
	while (x%y!=0)
	{
		x=x%y;
		swap(x,y);
	}
	return y;
}

int main()
{
	long long cas=0;
	long long t[50];
	long long i, dif, g, T, n;
	freopen("b.txt", "r", stdin);
	freopen("b.out", "w", stdout);
	scanf("%I64d", &T);
	while (T--)
	{
		scanf("%I64d", &n);
		for (i=0; i<n; i++)
		  scanf("%I64d", &t[i]);
		sort(t, t+n);  
		g=0;
		for (i=1; i<n; i++)
		{
			dif=t[i]-t[i-1];
			if (i==1) g=dif;
			else g=gcd(g, dif);
		}
		if (g==0 || t[0]%g==0) printf("Case #%I64d: %I64d\n", ++cas, 0LL);
		else printf("Case #%I64d: %I64d\n", ++cas, g-t[0]%g);
	}
	return 0;
}
