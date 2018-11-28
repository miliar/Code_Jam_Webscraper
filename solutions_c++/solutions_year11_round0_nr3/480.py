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

int n, a1;
int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int T, tt = 0;
	for (scanf("%d", &T); T; T--) {
		scanf("%d", &n);
		int sum = 0, mi = 1000010, s = 0;
		for (int i = 0; i < n; i++) {
			scanf("%d", &a1);
			s ^= a1;
			sum += a1;
			mi = min(mi, a1);
		}
		printf("Case #%d: ", ++tt);
		if (s != 0)
			puts("NO");
		else
			printf("%d\n", sum - mi);
	}
}
