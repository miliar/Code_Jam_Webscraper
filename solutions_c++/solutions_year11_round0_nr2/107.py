#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <queue>

using namespace std;

char comb[128][128];
bool oppo[128][128];

deque<char> dq;

int main()
{
	freopen("f:\\B-small-attempt0.in", "r", stdin);
	freopen("f:\\B-small-attempt0.out", "w", stdout);

	char s[128];
	int T;
	scanf("%d", &T);
	for (int t_case = 1; t_case <= T; t_case++)
	{
		memset(comb, 0, sizeof(comb));
		memset(oppo, 0, sizeof(oppo));
		int C, D;
		scanf("%d", &C);
		while (C--)
		{
			scanf("%s", s);
			comb[s[0]][s[1]] = s[2];
			comb[s[1]][s[0]] = s[2];
		}
		scanf("%d", &D);
		while (D--)
		{
			scanf("%s", s);
			oppo[s[0]][s[1]] = true;
			oppo[s[1]][s[0]] = true;
		}
		
		dq.clear();
		scanf("%d %s", &C, s);
		for (int i = 0; s[i]; i++)
		{
			if (dq.empty())
			{
				dq.push_back(s[i]);
			}
			else if (comb[dq.back()][s[i]])
			{
				char c = comb[dq.back()][s[i]];
				dq.pop_back();
				s[i] = c; i--;
			}
			else
			{
				bool x = false;
				for (deque<char>::iterator it = dq.begin(); it != dq.end(); it++)
				{
					if (oppo[*it][s[i]])
					{
						x = true;
						dq.clear();
						break;
					}
				}
				if (!x) dq.push_back(s[i]);
			}
			
		}
		printf("Case #%d: [", t_case);
		for (int i = 0; i < dq.size(); i++)
		{
			if (i < dq.size() - 1)
				printf("%c, ", dq[i]);
			else
				printf("%c", dq[i]);
		}
		printf("]\n");
	}
	return 0;
}
