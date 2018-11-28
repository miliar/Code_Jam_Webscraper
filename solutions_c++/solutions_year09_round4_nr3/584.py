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

const int N = 128;
int price[N][N];
int n, k;

bool intersects(int x, int y) {
	for (int i = 0; i < k; i++)
		if (price[x][i] == price[y][i])
			return true;

	for (int i = 0; i < k - 1; i++)
		if ((price[x][i] > price[y][i]) != (price[x][i + 1] > price[y][i + 1]))
			return true;	
	
	return false;
}

bool contains (int x, int i) {
	return (x & (1 << i)) > 0;
}

int solve() {	
	scanf("%d%d", &n, &k);
	for (int i = 0; i < n; i++)
		for (int j = 0; j < k; j++)
			scanf("%d", &price[i][j]);

	vector<vector<bool> > adj(n, vector<bool>(n));
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			if (!intersects(i, j))
				adj[i][j] = true;

	vector<int> d((1 << n), 2 * n);
	d[0] = 0;
	for (int i = 0; i < n; i++) {		
		for (int mask = 0; mask < (1 << i); mask++) {
			for (int sub = mask; sub >= 0; sub = (sub - 1) & mask) {
				bool ok = true;
				for (int j = 0; j < i; j++)
					if (contains(sub, j) && !adj[i][j]) {
						ok = false;
						break;
					}				
				if (ok) {
					if (sub == 0)
						d[mask | (1 << i)] = min(d[mask | (1 << i)], 1 + d[sub] + d[mask ^ sub]);
					else
						d[mask | (1 << i)] = min(d[mask | (1 << i)], d[sub] + d[mask ^ sub]);
				}
				if (sub == 0)
					break;
			}
		}
	}		
	return d[(1 << n) - 1];
}

int main () {
	freopen("c.in", "r", stdin); freopen("c.out", "w", stdout);
	int nTests;
	scanf("%d", &nTests);
	for (int T = 1; T <= nTests; T++)
		printf("Case #%d: %d\n", T, solve());
	fclose(stdin); fclose(stdout);
	return 0;
}
