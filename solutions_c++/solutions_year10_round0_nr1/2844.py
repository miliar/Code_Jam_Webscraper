#define CRT_SECURE_NO_DEPRECATE
#include <cstdio>

using namespace std;

int main()
{
	freopen("A-large.in.txt", "r", stdin);
	freopen("test.out", "w", stdout);
	int t, n;
	long long int k, res;
	scanf("%d", &t);
	
	for (int i = 0; i < t; i++)
	{
		scanf("%d%d", &n, &k);	
		res = 1 << n;
		++k %= res;
		if (k) printf("Case #%d: OFF\n", i+1);
		else printf("Case #%d: ON\n", i+1);
	}

	return 0;
}