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

int c[1024];

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int T, N;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
	scanf("%d", &N);
	int s = 0, sum = 0, mi = 100000000;
	for (int i = 0; i < N; ++i) {
	    scanf("%d", &c[i]);
	    s ^= c[i];
	    sum += c[i];
	    mi = min(mi, c[i]);
	}
	int ans;
	if (s == 0)
	    ans = sum - mi;
	else
	    ans = -1;
	/*
	int ans = -1;
	for (int mask = 1; mask < (1 << N) - 1; ++mask) {
	    int s1 = 0, s2 = 0;
	    int sum1 = 0, sum2 = 0;
	    for (int i = 0; i < N; ++i) {
		if (mask & (1 << i)) {
		    s1 ^= c[i];
		    sum1 += c[i];
		} else {
		    s2 ^= c[i];
		    sum2 += c[i];
		}
	    }
	    if (s1 == s2) {
		ans = max(ans, max(sum1, sum2));
	    }
	}
	*/
	printf("Case #%d: ", cas);
	
	if (ans == -1)
	    puts("NO");
	else
	    printf("%d\n", ans);
    }
    return 0;
}
