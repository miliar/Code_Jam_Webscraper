#include <algorithm>
#include <stdio.h>
#include <vector>

#define MAX 256
#define pb push_back

using namespace std;

int per[MAX][MAX], op[MAX][MAX];

int main()
{
	freopen("b-large.in", "r", stdin);
	freopen("b-large.out", "w", stdout);

	int t = 0, testCases;
	for (scanf("%d\n", &testCases); testCases; testCases--)
	{
		t++;
		int p;

		memset(per, 0, sizeof(per));
		memset(op, 0, sizeof(op));
		for (scanf("%d", &p); p; p--)
		{
			char ch1, ch2, ch3;
			scanf(" %c%c%c", &ch1, &ch2, &ch3);

			per[ch1][ch2] = per[ch2][ch1] = ch3;
		}

		for (scanf("%d", &p); p; p--)
		{
			char ch1, ch2;
			scanf(" %c%c", &ch1, &ch2);

			op[ch1][ch2] = op[ch2][ch1] = 1;
		}

		vector <char> vctCh;
		for (scanf("%d", &p); p; p--)
		{
			char ch;
			scanf(" %c", &ch);

			vctCh.pb(ch);

			if (vctCh.size() > 1)
			{
				char c = per[vctCh[vctCh.size() - 1]][vctCh[vctCh.size() - 2]];
				if (c)
					vctCh.pop_back(), vctCh.pop_back(), vctCh.pb(c);
				else
					for (int i = 0; i < vctCh.size() - 1; i++)
						if (op[vctCh[vctCh.size() - 1]][vctCh[i]])
						{
							vctCh.clear();
							break;
						}
			}
		}

		printf("Case #%d: [", t);
		if (vctCh.size())
			printf("%c", vctCh[0]);
		for (int i = 1; i < vctCh.size(); i++)
			printf(", %c", vctCh[i]);
		printf("]\n");
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}
					