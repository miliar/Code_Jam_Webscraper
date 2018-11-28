#include <algorithm>
#include <stdio.h>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int t = 0, testCases;
	for (scanf("%d", &testCases); testCases; testCases--)
	{
		t++;
		int n;
		scanf("%d", &n);

		int bO = 1, tO = 0;
		int bB = 1, tB = 0;
		for (int i = 1; i <= n; i++)
		{
			char ch;
			int b;
			scanf(" %c %d", &ch, &b);

			if (ch == 'O')
			{
				tO = max(tB + 1, tO + abs(bO - b) + 1);
				bO = b;
			}
			else
			{
				tB = max(tO + 1, tB + abs(bB - b) + 1);
				bB = b;
			}
		}
		
		printf("Case #%d: %d\n", t, max(tO, tB));
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}
