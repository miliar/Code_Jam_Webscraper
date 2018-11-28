#include <stdio.h>
#include <algorithm>
#include <vector>
#include <utility>

#define mp make_pair
#define fi first
#define se second
using namespace std;

int main()
{
	int i, j, sz1, sz2, task1, task2, pos1, pos2, time, T, n, num, dummy;
	char temp, com;
	vector <pair <int, int> > command1, command2;
	freopen("1-2.in", "r", stdin);
	freopen("1-2.out", "w", stdout);
	scanf("%d", &T);
	for (i = 1; i <= T; ++i)
	{
		command1.clear();
		command2.clear();
		scanf("%d", &n);
		for (j = 1; j <= n; ++j)
		{
			scanf("%c", &temp);
			scanf("%c %d", &com, &num);
			if (com == 'O')
				command1.push_back(mp(j, num));
			else
				command2.push_back(mp(j, num));
		}
		command1.push_back(mp(1000, 1000));
		command2.push_back(mp(1000, 1000));
		sz1 = command1.size();
		sz2 = command2.size();
		task1 = 0;
		task2 = 0;
		pos1 = pos2 = 1;
		time = 0;
		while ((task1 < (sz1-1)) || (task2 < (sz2-1)))
		{
			if (command1[task1].fi < command2[task2].fi)
			{
				dummy = abs(pos1-command1[task1].se)+1;
				pos1 = command1[task1].se;
				if (pos2 < command2[task2].se)
				{
					pos2 += dummy;
					if (pos2 > command2[task2].se)
						pos2 = command2[task2].se;
				}
				else
				{
					pos2 -= dummy;
					if (pos2 < command2[task2].se)
						pos2 = command2[task2].se;
				}
				time += dummy;
				++task1;
			}
			else
			{
				dummy = abs(pos2-command2[task2].se)+1;
				pos2 = command2[task2].se;
				if (pos1 < command1[task1].se)
				{
					pos1 += dummy;
					if (pos1 > command1[task1].se)
						pos1 = command1[task1].se;
				}
				else
				{
					pos1 -= dummy;
					if (pos1 < command1[task1].se)
						pos1 = command1[task1].se;
				}
				time += dummy;
				++task2;
			}
		}
		printf("Case #%d: %d\n", i, time);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
