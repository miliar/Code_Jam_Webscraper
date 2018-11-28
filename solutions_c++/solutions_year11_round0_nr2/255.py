#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>

using namespace std;


char comb[128][128];
bool opps[128][128];
int T, C, D, N;
char str[102];

int main()
{
	freopen("B-large.out","w",stdout);
	freopen("B-large.in","r",stdin);
	scanf("%d", &T);
	for (int cases = 1; cases <= T; cases++)
	{
		memset(comb, 0, sizeof(comb));
		memset(opps, 0, sizeof(opps));

		scanf("%d", &C);
		for (int i = 0; i < C; i++)
		{
			scanf("%s", str);
			comb[str[0]][str[1]] = str[2];
			comb[str[1]][str[0]] = str[2];
		}

		scanf("%d", &D);
		for (int i = 0; i < D; i++)
		{
			scanf("%s", str);
			opps[str[0]][str[1]] = true;
			opps[str[1]][str[0]] = true;
		}

		scanf("%d", &N);
		scanf("%s", str);

		vector<char> vc;
		for (int i = 0; i < strlen(str); i++)
		{
			vc.push_back(str[i]);


			while (vc.size() >= 2 && comb[vc[vc.size() - 1]][vc[vc.size() - 2]] > 0)
			{
				char comb_res = comb[vc[vc.size() - 1]][vc[vc.size() - 2]];
				vc.erase(vc.end() - 1);
				vc.erase(vc.end() - 1);
				vc.push_back(comb_res);
			}

			for (int k = 0; k < vc.size() - 1; k++)
			{
				if (opps[vc[k]][vc[vc.size() - 1]])
				{
					vc.clear();
					break;
				}
			}
		}

		if (vc.size() == 0)
		{
			printf("Case #%d: []\n", cases);
		}
		else
		{
			printf("Case #%d: [", cases);
			for (int i = 0; i < vc.size() - 1; i++)
			{
				printf("%c, ", vc[i]);
			}
			printf("%c]\n", vc[vc.size() - 1]);
		}
	}
	return 0;
}