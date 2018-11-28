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

vector<int> solve() {
	int n;   
	scanf("%d", &n);
	vector<int> deck(n, -1);
	vector<int> next(n), prev(n);
	for (int i = 0; i < n; i++) {
		next[i] = (i + 1) % n;
		prev[i] = (i - 1 + n) % n;
	}
	int cur = 0;
	for (int step = 0; step < n; step++) {
		int count = 0;
		while (count != step) {
			if (deck[cur] == -1) count++;
			cur = next[cur];
		}
		while (deck[cur] != -1)
			cur = next[cur];		
		
		int a = prev[cur], b = next[cur];
		next[a] = b;
		prev[b] = a;
		
		deck[cur] = step + 1;
	}
	return deck;
}

int main () {
	freopen("c.in", "r", stdin); freopen("c.out", "w", stdout);
	int nTests;
	scanf("%d", &nTests);	
	for (int T = 1; T <= nTests; T++) {		
		printf("Case #%d:", T);
		vector<int> deck = solve();
		int n_ind;
		scanf("%d", &n_ind);
		for (int i = 0; i < n_ind; i++) {
			int pos;
			scanf("%d", &pos);
			printf(" %d", deck[pos - 1]);
		}
		putchar('\n');
	}
	fclose(stdin); fclose(stdout);
	return 0;
}
