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

int GCD(int a, int b)
{
	if (b == 0) return a;
	else return GCD(b, a % b);
}

int run()
{
	long long n;
	int pd, pg;
	scanf("%lld %d %d", &n, &pd, &pg);
	if (pg == 0 && pd != 0) return false;
	if (pg == 100 && pd != 100) return false;
	int g = GCD(pd, 100);
	int a = 100 / g;
	return a <= n;
}

int main()
{
	freopen("A1.in", "r", stdin);
	freopen("A1.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: %s\n", i, run() ? "Possible" : "Broken");
	}
	return 0;
}