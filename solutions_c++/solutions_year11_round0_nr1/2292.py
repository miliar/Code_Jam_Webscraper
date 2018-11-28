#define _CRT_SECURE_NO_DEPRECATE
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cmath>

using namespace std;

const int inf = 10000000;

int koltest, n;
int cur1, cur2, kol1, kol2;
int a1[1000][2];
int a2[1000][2];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	scanf("%d", &koltest);
	for (int nom_test = 0; nom_test < koltest; ++nom_test)
	{
		scanf("%d ", &n);
		kol1 = 0;
		kol2 = 0;
		for (int j = 0; j < n; ++j)
		{
			char tempc;
			int temp;
			scanf("%c %d ", &tempc, &temp);
			if (tempc == 'O')
			{
				a1[kol1][0] = temp;
				a1[kol1][1] = j;
				++kol1;
			}
			else
			{
				a2[kol2][0] = temp;
				a2[kol2][1] = j;
				++kol2;
			}
		}
		a1[kol1][1] = inf;
		a2[kol2][1] = inf;

		int time = 0;
		cur1 = 1;
		cur2 = 1;
		int nom1 = 0, nom2 = 0;
		while (nom1 != kol1 || nom2 != kol2)
		{
			if (a1[nom1][1] < a2[nom2][1])
			{
				if (cur1 != a1[nom1][0])
				{
					cur1 += (a1[nom1][0] - cur1) / (abs(a1[nom1][0] - cur1));
				}
				else
				{
					++nom1;
				}
				if (cur2 != a2[nom2][0])
				{
					cur2 += (a2[nom2][0] - cur2) / (abs(a2[nom2][0] - cur2));
				}
			}
			else
			{
				if (cur2 != a2[nom2][0])
				{
					cur2 += (a2[nom2][0] - cur2) / (abs(a2[nom2][0] - cur2));
				}
				else
				{
					++nom2;
				}
				if (cur1 != a1[nom1][0])
				{
					cur1 += (a1[nom1][0] - cur1) / (abs(a1[nom1][0] - cur1));
				}
			}
			++time;
		}
		printf("Case #%d: %d\n", nom_test + 1, time);
	}

	return 0;
}