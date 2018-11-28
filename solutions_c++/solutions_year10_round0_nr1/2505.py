#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	//freopen("test.in", "w", stdout);
	int n,k,t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		scanf("%d%d", &n, &k);
		if ((k % (int)pow(2, (double)n)) == (pow(2, (double)n) - 1))
			printf("Case #%d: ON\n", i + 1);
		else
			printf("Case #%d: OFF\n", i + 1);
	}

	return 0;
}