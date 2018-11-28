#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>

using namespace std;

const int inf = 1000000000;

int d[10000], l[10000], f[10000];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	scanf("%d", &T);
	for (int test = 0; test < T; test ++) {
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; i ++) scanf("%d%d", &d[i], &l[i]);
		int D;
		scanf("%d", &D);
		f[0] = d[0];
		for (int i = 1; i < n; i ++) {
			f[i] = -inf;
			for (int j = 0; j < i; j ++)
				if (d[i] - d[j] <= f[j])
					f[i] = max(f[i], min(l[i], d[i] - d[j]));
		}
		bool flag = false;
		for (int i = 0; i < n; i ++)
			if (f[i] > -inf && D - d[i] <= f[i]) flag = true;
		if (flag)
			printf("Case #%d: YES\n", test + 1);
		else
			printf("Case #%d: NO\n", test + 1);
	}
	
	return 0;
}
