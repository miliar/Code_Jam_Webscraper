#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <numeric>
#include <utility>
#include <functional>
#include <algorithm>
#include <bitset>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

int main(int argc, char *argv[])
{
	int nc, ci;

	scanf("%d", &nc);
	for (ci = 1; ci <= nc; ci++) {
		int n, D;
		cin >> n;
		vector<int> d(n), l(n);
		for (int i = 0; i < n; i++)
			cin >> d[i] >> l[i];
		cin >> D;
		int x = min(d[0], l[0]), k = x;
		if (l[0] < d[0]) {
			printf("Case #%d: NO\n", ci);
			continue;
		}
		
		vector<int> a(n, -1);
		a[0] = k;
		for (int i = 0; i < n; i++) {
			if (a[i] < 0) break;
			for (int j = i + 1; j < n; j++) {
				int t = d[j] - d[i];
				if (t > a[i]) break;
				if (a[j] < 0 || a[j] < min(t, l[j]))
					a[j] = min(t, l[j]);
			}
		}
		
		int ok = false;
		for (int i = 0; i < n; i++)
			if (d[i] + a[i] >= D) ok = true;
		
		printf("Case #%d: %s\n", ci, ok ? "YES" : "NO");
	}

	return 0;
}
