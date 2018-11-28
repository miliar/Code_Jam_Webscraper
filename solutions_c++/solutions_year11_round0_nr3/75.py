#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define sz(a) int((a).size())
#define all(X) (X).begin(), (X).end()
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;

int run()
{
	int n;
	scanf("%d", &n);
	int sum = 0, s = 0, mmin = 10000000;
	while (n--) {
		int num;
		scanf("%d", &num);
		sum ^= num;
		s += num;
		mmin = min(num, mmin);
	}
	if (sum == 0) {
		return s - mmin;
	}
	else {
		return -1;
	}
}

int main()
{
	freopen("C1.in", "r", stdin);
	freopen("C1.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: \n", i);
		int res = run();
		if (res < 0) puts("NO");
		else printf("%d\n", res);
	}
	return 0;
}