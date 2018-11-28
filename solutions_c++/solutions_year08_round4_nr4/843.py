#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <string>
#include <cctype>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <sstream>
#include <deque>
#include <memory>
using namespace std;
typedef vector<int> vi;
typedef long long li;
typedef pair<int,int> pi;
#define all(c) c.begin(), c.end()
#define fr(i, n) for(i = 0; i < n; ++i)
#define pb push_back
#define mp make_pair
#define INT 2147483647
#define X first
#define Y second
#define sc(a) scanf("%d", &(a))

int dp[10];
char em[10000], temp[10000];
int main() {
	freopen("e:\\code\\d\\d-small.in", "r", stdin);
	freopen("e:\\code\\d\\d-small.out", "w", stdout);
	int i, j, k, n, t, T;
	sc(T);
	fr(t, T) {
		int ans = INT;
		sc(k);
		scanf("%s", em);
		fr(i, k) dp[i] = i;
		n = strlen(em);
		do {
			fr(i, n) temp[i] = em[i];
			for (i = 0; i < n; i += k) {
				fr(j, k) {
					temp[i + j] = em[i + dp[j]];
				}
			}
			int cur = 1;
			for (i = 1; i < n; ++i) {
				if (temp[i] != temp[i - 1]) ++cur;
			}
			ans = min(cur, ans);

		} while(next_permutation(dp, dp + k));
		printf("Case #%d: %d\n", t + 1, ans);
	}
	return 0;
}
		
