#include <iostream>

using namespace std;

int t;
int n, k;
int f[11];

int main()
{
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	scanf("%d", &t);
	for(int i = 1; i <= t; i++)
	{
		scanf("%d%d", &n, &k);
		if(k == 0)
		{
            printf("Case #%d: OFF\n", i);
            continue;
        }
		f[1] = 1;
		for(int j = 2; j <= n; j++)
			f[j] = 2 * f[j - 1] + 1;
		if(f[n] > k)
			printf("Case #%d: OFF\n", i);
		else
		{
			if((k - f[n]) % (f[n] + 1) == 0)
			{
				printf("Case #%d: ON\n", i);
			}
			else
			{
				printf("Case #%d: OFF\n", i);
			}
		}
	}
	return 0;
}
