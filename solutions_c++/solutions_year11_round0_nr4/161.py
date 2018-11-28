#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <cmath>
#include <stack>
#include <list>
#include <map>
#include <set>
using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
template<class T> string i2s(T x) { ostringstream o; o<<x; return o.str(); }

int main() {
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
    int T, N, a[1024];
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
	scanf("%d", &N);
	int ans = 0;
	for (int i = 0; i < N; ++i) {
	    scanf("%d", &a[i]);
	    if (a[i] != i + 1)
		ans++;
	}
	printf("Case #%d: %d.000000\n", cas, ans);
    }
    return 0;
}
