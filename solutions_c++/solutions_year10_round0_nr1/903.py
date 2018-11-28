#include <iostream>
#include <cstdio>

using namespace std;

typedef long long ll;

ll x[40];
int cases;

int main()
{
	x[0] = 1;
	for (int i = 1; i < 40; ++i)
		x[i] = x[i - 1] << 1;

	int t;
	scanf("%d", &t);
	while (t--)
	{
		int n, k;
		scanf("%d %d", &n, &k);
		printf("Case #%d: ", ++cases);
		if (k % x[n] == x[n] - 1)
			printf("ON\n");
		else
			printf("OFF\n");
	}
}