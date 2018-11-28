#include <algorithm>
#include <stdio.h>

using namespace std;

int testCases, t, n, misc;
int poz[64];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	scanf("%d\n", &testCases);

	for (int t = 1; t <= testCases; t++)
	{
		scanf("%d\n", &n);

		misc = 0;

		memset(poz, 0, sizeof(poz));

		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= n; j++)
			{
				char ch;
				scanf("%c", &ch);

				if (ch == '1')
					poz[i] = j;
			}
			scanf("\n");
		}

		for (int i = 1; i <= n; i++)
			for (int ii = i; ii <= n; ii++)
				if (poz[ii] <= i)
				{
					for (int j = ii; j > i; j--)
					{
						swap(poz[j], poz[j - 1]);

						misc++;
					}

					break;
				}

		printf("Case #%d: %d\n", t, misc);
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}
