#include <stdio.h>

bool p[10000000];
int fact[10];
const int Maxb = 2000001;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	for (int i = 0; i <= 9; i++)
		fact[i] = i*(i+1)/2;


	int testnum;
	scanf("%d", &testnum);
	for (int testcase = 1; testcase <= testnum; testcase++)
	{
		int a, b;
		scanf("%d%d", &a, &b);
		for (int i = 0; i <= Maxb; i++)
			p[i] = true;
		
		int kol = 1, st10 = 1;
		while (st10*10 <= a)
		{
			kol++;
			st10 *= 10;
		}

		int res = 0;
		for (int i = a; i <= b; i++)
			if (p[i])
			{
				p[i] = false;
				int k = 1;
				int n = i;

				for (int j = 1; j <= kol; j++)
				{
					int temp = n % 10;
					n = n/10 + temp*st10;

					if (p[n] && n >= a && n <= b)
					{
						p[n] = false;
						k++;
					}
				}

				res += fact[k-1];
			}

		printf("Case #%d: %d\n", testcase, res);
	}


	return 0;
}

