#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

typedef long long LL;

int tc, ntc;

bool win(int a, int b)
{
	if (a < b) swap(a,b);	
	if (a == b) return false;
	if (a-b >= b) return true;
	return !win(b, a-b);	
}

int calc1(int a, int b1, int b2)
{
	if (b1 >= a) return 0;
	b2 <?= a - 1;
	
	if (!win(a, b1)) return 0;
	int p = b1;
	int q = b2;
	while (p < q)
	{
		int mid = (p + q + 1) / 2;
		if (win(a, mid)) p = mid;
		else q = mid - 1;
	}	
	return p - b1 + 1;
}

int main()
{
	scanf("%d", &ntc);
	int a1, a2, b1, b2;
	for (tc = 1; tc <= ntc; tc++)
	{
		scanf("%d %d %d %d", &a1, &a2, &b1, &b2);

		LL res = 0;		
		int i, j;
		
		for (i=a1; i<=a2; i++)
			res += calc1(i, b1, b2);
		for (i=b1; i<=b2; i++)
			res += calc1(i, a1, a2);
		
		printf("Case #%d: %lld\n", tc, res);
	}
}