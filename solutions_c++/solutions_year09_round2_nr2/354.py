#include <algorithm>
#include <stdio.h>

#define MAX 512

using namespace std;

int testCases;
char strNr[MAX];
int ap[MAX];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	scanf("%d\n", &testCases);

	for (int test = 1; test <= testCases; test++)
	{
		printf("Case #%d: ", test);

		fgets(strNr + 1, MAX, stdin);
		strNr[0] = '0';

		int lung = strlen(strNr) - 2;

		int ok = 0;
		for (int i = lung; i >= 0 && !ok; i--)
		{
			for (int j = lung; j > i && !ok; j--)
				if (strNr[i] < strNr[j])
				{
					ok = 1;

					swap(strNr[i], strNr[j]);
					for (int k = i + 1; k <= lung; k++)
						ap[strNr[k] - '0']++;

					for (int k = i + 1; k <= lung; k++)
						for (int h = 0; h < 10; h++)
							if (ap[h])
							{
								ap[h]--;

								strNr[k] = '0' + h;
								break;
							}
				}
		}

		if (strNr[0] == '0')
			printf("%s", (strNr + 1));
		else printf("%s", strNr);
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}
