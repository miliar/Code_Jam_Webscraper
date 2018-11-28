#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>

using namespace std;

char c[64][64];

bool change(char s[64][64], int r, int c)
{
    if (s[r][c] != '#')
    {
        return true;
    }

    for (int i = r; i <= r + 1; i++)
    {
        for (int j = c; j <= c + 1; j++)
        {
            if (s[i][j] != '#')
            {
                return false;
            }
        }
    }

    char ss[] = "/\\\\/";
    int k = 0;
    for (int i = r; i <= r + 1; i++)
    {
        for (int j = c; j <= c + 1; j++)
        {
            s[i][j] = ss[k++];
        }
    }    
}

void solve()
{
	int caseNum;
	scanf("%d", &caseNum);

	for (int caseId = 1; caseId <= caseNum; caseId++)
	{
		printf("Case #%d:\n", caseId);

        int R, C;
        scanf("%d %d", &R, &C);

        for (int i = 0; i < R; i++)
        {
            scanf("%s", c[i]);
        }

        bool bOK = true;
        for (int i = 0; i < R - 1 && bOK; i++)
        {
            for (int j = 0; j < C - 1 && bOK; j++)
            {
                if (!change(c, i, j))
                {
                    bOK = false;
                }
            }
        }

        for (int i = 0; i < R  && bOK; i++)
        {
            if (c[i][C - 1] == '#')
            {
                bOK = false;
            }
        }

        for (int i = 0; i < C && bOK; i++)
        {
            if (c[R - 1][i] == '#')
            {
                bOK = false;
            }
        }
        if (!bOK)
        {
            printf("Impossible\n");
        }
        else
        {
            for (int i = 0; i < R; i++)
            {
                puts(c[i]);
            }
        }
	}
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	solve();

	return 0;
}