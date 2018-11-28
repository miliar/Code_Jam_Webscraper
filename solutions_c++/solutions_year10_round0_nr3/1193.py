/*
 * c.cpp
 *
 *  Created on: 2010-5-8
 *      Author: Allie
 */
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cmath>
#include <complex>
#include <cassert>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

#define SZ(c) ((int) (c).size())

const int INF = 1000000000;

ll eurosMade(int R, int k, vi g)
{
	int n = SZ(g);
	vector<bool> was(n);
	vector<ll> earning;
	{
		int i = 0;
		while (!was[i]) {
			ll take;
			if (g[i] > k) {
				take = 0;
			} else {
				take = g[i];
				int j = i;
				while (true) {
					++j;
					if (j >= n)
						j = 0;
					if (j == i || take + g[j] > k)
						break;
					take += g[j];
				}
				i = j;
			}
			earning.push_back(take);
			if (SZ(earning) >= R || take == 0) {
				ll res = 0;
				for (int u = 0; u < SZ(earning); ++u)
					res += earning[u];
				return res;
			}
		}
	}
	int period = SZ(earning);
	ll whole = 0;
	ll remaining = 0;
	for (int i = 0; i < period; ++i) {
		whole += earning[i];
		if (i < R % period)
			remaining += earning[i];
	}
	return R / period * whole + remaining;
}

int main()
{
	int T;
	cin >> T;
	for (int icase = 1; icase <= T; ++icase) {
		int R;
		int k;
		int N;
		cin >> R >> k >> N;
		vi g(N);
		for (int i = 0; i < N; ++i)
			cin >> g[i];
		printf("Case #%d: %lld\n", icase, eurosMade(R, k, g));
	}
	return 0;
}

