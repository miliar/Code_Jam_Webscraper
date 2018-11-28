#include <cassert>
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <climits>
#include <cstddef>
#include <cctype>
#include <cmath>
#include <cstring>
#include <fstream>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <numeric>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#include <bitset>
#include <list>
#include <string>
#include <functional>
#include <utility>
using namespace std;
typedef long long llint;
int const L = 7;
int bs[L + 1];
int a, b;
void init() {
	bs[0] = 1;
	for (int i = 1; i <= L; ++i) {
		bs[i] = bs[i - 1] * 10;
	}
}
bool readin() {
	return scanf("%d%d", &a, &b) != EOF;
}
int solve() {
	int ret = 0;
	int l;
	for (l = 0; ; ++l) {
		if (b < bs[l]) {
			break;
		}
	}
	for (int i = a; i <= b; ++i) {
		vector <bool> used(b + 1);
		for (int j = 1; j < l; ++j) {
			int k = (i % bs[j]) * bs[l - j] + i / bs[j];
			if (k > i && k <= b && !used[k]) {
				++ret;
				used[k] = true;
			}
		}
	}
	return ret;
}
int main() {
	init();
	int tc;
	int cc = 0;
	scanf("%d", &tc);
	while (tc--) {
		readin();
		printf("Case #%d: %d\n", ++cc, solve());
	}
	return 0;
}
