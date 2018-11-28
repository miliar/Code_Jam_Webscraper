#include <vector>
#include <string>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <cstdio>

using namespace std;

#define fn(i, n)	for(int i = 0; i < (n); ++i)
#define set1(a)		memset(a, 0x3f, sizeof(a))
#define INF			0x3f3f3f3f

char S[65536], s[16][65536];
int cost1[16][16], cost[16][16], sol[65536][16][16];
int n, T, k, l, END;

int solve(int mask, int cur, int first) {
	if (sol[mask][cur][first] != INF)
		return sol[mask][cur][first];
	int tmp, &res = sol[mask][cur][first];
	int mask1 = (mask | (1 << cur));
	if (mask1 == END) {
		res = cost1[cur][first];
	} else {
		fn(next, k) {
			if (mask1 & (1 << next)) continue;
			tmp = cost[cur][next] + solve(mask1, next, first);
			if (tmp < res) res = tmp;
		}
	}
	return res;
}

int main() {
	freopen("d.in", "rt", stdin);
	freopen("d.out", "wt", stdout);

	cin >> T;
	fn(test, T) {
		cin >> k;
		cin >> S;
		l = strlen(S) / k;
		fn(i, k) {
			fn(j, l) {
				s[i][j] = S[i + j * k];
			}
		}
		fn(i, k) {
			fn(j, k) {
				cost[i][j] = 0;
				cost1[i][j] = 1;
				fn(r, l) {
					if (s[i][r] != s[j][r]) ++cost[i][j];
				}
				fn(r, l-1) {
					if (s[i][r] != s[j][r+1]) ++cost1[i][j];
				}
			}
		}
		int ans = INF, tmp;
		END = (1 << k) - 1;
		set1(sol);
		fn(i, k) {
			tmp = solve(0, i, i);
			if (tmp < ans)
				ans = tmp;
		}
		cout << "Case #" << test+1 << ": " << ans;
		cout << endl;
	}

	return 0;
}
