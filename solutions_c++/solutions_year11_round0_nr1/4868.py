#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	int caseID = 1;
	while (caseID <= t)
	{
		printf("Case #%d: ", caseID++);
		int m;
		scanf("%d", &m);
		int sum = 0, opos = 1, bpos = 1, lef = 0;
		char cur;
		int i;
		for (i = 0; i < m; i++)
		{
			char action[2];
			int but;
			scanf("%s %d", action, &but);
			if (i == 0) cur = action[0];
			if (action[0] == cur)
			{
				if (action[0] == 'O') lef += abs(but - opos) + 1, opos = but;
				if (action[0] == 'B') lef += abs(but - bpos) + 1, bpos = but;
			}
			else
			{
				sum += lef;
				if (action[0] == 'O')
				{
					if (abs(but - opos) <= lef) opos = but;
					else opos = opos + (but - opos) / abs(but - opos) * lef;
					lef = abs(but - opos) + 1;
				}
				if (action[0] == 'B')
				{
					if (abs(but - bpos) <= lef) bpos = but;
					else bpos = bpos + (but - bpos) / abs(but - bpos) * lef;
					lef = abs(but - bpos) + 1;
				}
			}
			cur = action[0];
		}
		sum += lef;
		printf("%d\n", sum);
	}
	return 0;
}