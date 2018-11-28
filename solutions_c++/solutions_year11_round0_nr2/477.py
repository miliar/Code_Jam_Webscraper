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

char c1, c2, c3, Q[110];
int n, m;
char re[100][100], x[100], y[100];
int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int T, tt = 0;
	for (scanf("%d", &T); T; T--) {
		scanf("%d", &n);
		memset(re, 0, sizeof(re));
		for (int i = 0; i < n; i++) {
			scanf(" %c %c %c", &c1, &c2, &c3);
			re[c1 - 'A'][c2 - 'A'] = c3;
			re[c2 - 'A'][c1 - 'A'] = c3;
		}
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf(" %c %c", x + i, y + i);
		scanf("%d", &m);
		int t = 0;
		for (int i = 0; i < m; i++) {
			scanf(" %c", &c1);
			Q[++t] = c1;
			while (t > 1 && re[Q[t - 1] - 'A'][Q[t] - 'A']) {
				Q[t - 1] = re[Q[t - 1] - 'A'][Q[t] - 'A'];
				t--;
			}
			for (int j = 0; j < n; j++)
				for (int a = 1; a <= t; a++)
					for (int b = a + 1; b <= t; b++)
						if (Q[a] == x[j] && Q[b] == y[j])
							t = 0;
			for (int j = 0; j < n; j++)
				for (int a = 1; a <= t; a++)
					for (int b = a + 1; b <= t; b++)
						if (Q[a] == y[j] && Q[b] == x[j])
							t = 0;
		}
		printf("Case #%d: [", ++tt);
		for (int i = 1; i <= t; i++)
			if (i == 1)
				putchar(Q[i]);
			else {
				putchar(',');
				putchar(' ');
				putchar(Q[i]);
			}
		puts("]");
	}
}
