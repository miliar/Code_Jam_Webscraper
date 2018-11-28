#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
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

#define PB push_back
#define MP make_pair

const double pi = 3.1415926535;
const double eps = 1e-6;

const int fx[4] = {0, 1, 1, 1};
const int fy[4] = {1, 0, -1, 1};

char ch;
int n, m, ki[110][110], du[20][20];
int gk(char ch)
{
	if (ch == '-')
		return 0;
	if (ch == '|')
		return 1;
	if (ch == '/')
		return 2;
	if (ch == '\\')
		return 3;
}
int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int T, ca = 0;
	for (scanf("%d", &T); T; T--) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++) {
				scanf(" %c", &ch);
				ki[i][j] = gk(ch);
			}
		int all = (n * m), ans = 0;
		for (int i = 0; i < (1 << all); i++) {
			for (int x = 0; x < n; x++)
				for (int y = 0; y < m; y++)
					du[x][y] = 0;
			bool flag = 1;
			for (int x = 0; x < n; x++)
				for (int y = 0; y < m; y++)
					if ((1 << (x * m + y)) & i)
						du[(x + fx[ki[x][y]] + n) % n][(y + fy[ki[x][y]] + m) % m]++;
					else
						du[(x - fx[ki[x][y]] + n) % n][(y - fy[ki[x][y]] + m) % m]++;
			for (int x = 0; x < n; x++)
				for (int y = 0; y < m; y++)
					if (du[x][y] != 1)
						flag = 0;
			if (flag)
				ans++;
		}
		printf("Case #%d: %d\n", ++ca, ans);
	}
}
