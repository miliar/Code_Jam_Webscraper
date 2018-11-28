#include <algorithm>
#include <stdio.h>

#define MAX 10024

using namespace std;

int l, d, n;
int sel[MAX], pos[MAX];
char strT[MAX];
char strWord[MAX][32];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	scanf("%d %d %d\n", &l, &d, &n);

	for (int i = 1; i <= d; i++)
		fgets(strWord[i] + 1, 32, stdin);

	for (int testNr = 1; testNr <= n; testNr++)
	{
		fgets(strT + 1, MAX, stdin);

		for (int i = 1; i <= d; i++)
			pos[i] = 1;

		int r = 0;
		for (int i = 1; i <= l; i++)
		{
			r++;
			memset(sel, 0, sizeof(sel));

			if (strT[r] == '(')
				for (r++; strT[r] != ')'; r++)
					sel[strT[r] - 'a'] = 1;
			else sel[strT[r] - 'a'] = 1;

			for (int j = 1; j <= d; j++)
				if (!sel[strWord[j][i] - 'a'])
					pos[j] = 0;
		}

		int sol = 0;
		for (int i = 1; i <= d; i++)
			sol += pos[i];

		printf("Case #%d: %d\n", testNr, sol);
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}
