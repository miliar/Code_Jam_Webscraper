#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
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
#include <ctime>
#include <cstring>

using namespace std;

typedef long long LL;

int main() {
	int d;
	scanf("%d", &d);
	for (int i = 1; i <= d; ++i) {
		int n, k;
		scanf("%d %d", &n, &k);
		printf("Case #%d: %s\n", i, ((k + 1) % (1 << n)) ? "OFF" : "ON");
	}
}
