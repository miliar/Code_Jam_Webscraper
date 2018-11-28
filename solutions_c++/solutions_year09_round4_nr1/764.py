#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <string>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define N 100

using namespace std;

char mat[N][N];
int n;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	int caseID = 1;
	while (caseID <= t)
	{
		scanf("%d", &n);
		int i, j, k;
		for (i = 0; i < n; i++)
			scanf("%s", mat[i]);
		bool flag = 0;
		int step = 0;
		while (!flag)
		{
			flag = 1;
			for (i = 0; i < n; i++)
			{
				for (j = n - 1; j > i; j--)
					if (mat[i][j] == '1')
					{
						flag = 0;
						break;
					}
				if (!flag) break;
			}
			if (!flag)
			{
				for (k = i + 1; k < n; k++)
				{
					bool f = 1;
					for (j = n - 1; j > i; j--)
						if (mat[k][j] == '1') f = 0;
					if (f)  break;
				}
				step += k - i;
				char temp[N];
				strcpy(temp, mat[k]);
				for (j = k; j > i; j--)
					strcpy(mat[j], mat[j - 1]);
				strcpy(mat[i], temp);
			}
		}
		printf("Case #%d: %d\n", caseID++, step);
	}
	return 0;
}