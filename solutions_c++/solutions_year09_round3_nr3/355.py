#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <bitset>
#include <utility>

#define REP(i, a, b) for (typeof(a) i = a; i < b; i++)
#define FOR(i, k) REP(i, 0, k)

#define all(x) x.begin(), x.end()

#define mp make_pair
#define pb push_back

#define watch(x) cout << #x << ": " << x << endl

using namespace std;

typedef long long LL;
typedef pair < int, int > PII;
typedef vector < int > VI;
typedef vector < string > VS;

const int Q = 109;

int q;
int cell[Q];
map < PII, int > memo;

int f(int begin, int end){ //inclusive
	if (begin >= end) return 0;

	if (memo.count(mp(begin, end))) return memo[mp(begin, end)];

	int ans = 900900900;
	bool flag = false;

	FOR(i, q){
		if (cell[i] >= begin && cell[i] <= end){
			ans = min(ans, end - begin + f(begin, cell[i] - 1) + f(cell[i] + 1, end));
			flag = true;
		}
	}

	if (!flag) ans = 0;

	return memo[mp(begin, end)] = ans;
}

int main(){
	int t; scanf("%d", &t);

	FOR(tt, t){
		int p;
		scanf("%d %d", &p, &q);

		FOR(i, q)
			scanf("%d", &cell[i]);

		memo.clear();

		printf("Case #%d: %d\n", tt + 1, f(1, p));

	}

	return 0;
}
