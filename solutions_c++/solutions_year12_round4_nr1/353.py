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

int n, d[110000], l[110000], f[110000];
int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int T, ca = 0;
	for (scanf("%d", &T); T; T--) {
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%d%d", d + i, l + i);
		memset(f, -1, sizeof f);
		f[0] = 0;
		int E;
		scanf("%d", &E);
		bool flag = 0;
		for (int i = 0; i < n; i++) {
			if (f[i] == -1) continue;
			if (d[i] - f[i] + d[i] >= E)
				flag = 1;
			for (int j = i + 1; j < n; j++)
				if (d[i] - f[i] + d[i] >= d[j]) {
					if (f[j] == -1 || f[j] > max(d[j] - l[j], d[i]))
						f[j] = max(d[j] - l[j], d[i]);
					if (d[j] - f[j] + d[j] >= E)
						flag = 1;
				}
		}
		printf("Case #%d: ", ++ca);
		if (flag) puts("YES"); else puts("NO");
	}
}
