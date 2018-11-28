#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>

using namespace std;

int d[300];

int main() {
/*	d[1] = 1;
	for (int i = 2; i <= 30; ++i) {
		d[i] = 2 * d[i - 1] + 1;
		cout << d[i] << endl;
	}*/
	int T; scanf("%d", &T);
	for (int tt = 0; tt < T; ++tt) {
		int n, k;
		scanf("%d %d", &n, &k);
		printf("Case #%d: ", tt + 1);
		if (!k || ((k & ((1 << n) - 1)) != (1 << n) - 1)) printf("OFF\n");
		else printf("ON\n");
	}
	return 0;
}
