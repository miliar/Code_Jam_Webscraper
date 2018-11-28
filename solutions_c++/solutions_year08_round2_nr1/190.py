#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
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

#define pb push_back
#define mp make_pair
#define all(v) v.begin(),v.end()

long long solve() {
	long long n, A, B, C, D, M;
	cin >> n >> A >> B >> C >> D;
	vector<long long> x(n), y(n);
	cin >> x[0] >> y[0] >> M;
	for (int i = 1; i < n; i++) {
		x[i] = (A * x[i - 1] + B) % M;
		y[i] = (C * y[i - 1] + D) % M;		
	}
	vector<long long> cnt(9);
	for (int i = 0; i < n; i++) {
		x[i] %= 3;
		y[i] %= 3;		
		++cnt[x[i] + 3 * y[i]];
	}
	long long res = 0;
	for (int i = 0; i < 9; i++)
		for (int j = i; j < 9; j++) {
			for (int k = j; k < 9; k++) {
				int p1 = i / 3;
				int p2 = i % 3;
				int q1 = j / 3;
				int q2 = j % 3;
				int r1 = k / 3;
				int r2 = k % 3;				
				if ((p1 + q1 + r1) % 3 == 0 && (p2 + q2 + r2) % 3 == 0) {
					long long dres = 0;
					if (i == j && j == k)
						dres = cnt[i] * (cnt[i] - 1) * (cnt[i] - 2) / 6;
					else if (i == j)
						dres = cnt[k] * cnt[i] * (cnt[i] - 1) / 2;
					else if (i == k)
						dres = cnt[j] * cnt[i] * (cnt[i] - 1) / 2;
					else if (j == k)
						dres = cnt[i] * cnt[j] * (cnt[j] - 1) / 2;
					else
						dres = cnt[i] * cnt[j] * cnt[k];
					
					if (dres < 0) dres = 0;
					res += dres;
				}
			}
		}	
	return res;
}

int main () {
	freopen("a.in", "r", stdin); freopen("a.out", "w", stdout);
	int nTests;
	scanf("%d", &nTests);
	for (int T = 1; T <= nTests; T++)
		printf("Case #%d: %lld\n", T, solve());
	fclose(stdin); fclose(stdout);
	return 0;
}
