#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <utility>
#include <vector>
using namespace std;

typedef long long LL;
template <class A, class B> void CONV(A &x, B &y) { stringstream s; s << x; s >> y; }
int CMP(double a, double b) { return a < b-1e-7 ? -1 : a > b+1e-7 ? 1 : 0; }
#define FOR(i, a, b) for (int i = a; i < b; ++i)
#define FORE(i, v) FOR(i, 0, v.size())
#define SORT(v) sort(v.begin(), v.end())
#define SET(a, n) memset(a, n, sizeof a)

int bound[1<<10];
LL dp[10][1<<9][11];
vector< vector<int> > cost;

LL go(int level, int pos, int cnt) {
	if (level == cost.size()-1) {
		if (cnt > bound[2*pos] || cnt > bound[2*pos+1]) return -2;
		if (cnt+1 > bound[2*pos] || cnt+1 > bound[2*pos+1]) return cost[level][pos]; 
		return 0;
	}
	if (dp[level][pos][cnt] != -1) return dp[level][pos][cnt];
	LL temp1 = go(level+1, 2*pos, cnt), temp2 = go(level+1, 2*pos+1, cnt);
	if (temp1 == -2 || temp2 == -2) return dp[level][pos][cnt] = -2;
	LL res = cost[level][pos]+temp1+temp2;
	if (cnt != 10) {
		temp1 = go(level+1, 2*pos, cnt+1);
		temp2 = go(level+1, 2*pos+1, cnt+1);
		if (temp1 != -2 && temp2 != -2) res = min(res, temp1+temp2);
	}
	return dp[level][pos][cnt] = res;
}

int main() {
	int t;
	cin >> t;
	FOR(i, 0, t) {
		int p;
		cin >> p;
		FOR(j, 0, 1<<p) cin >> bound[j];
		cost = vector< vector<int> >(p);
		FOR(j, 0, p) {
			FOR(k, 0, 1<<(p-j-1)) {
				int temp;
				cin >> temp;
				cost[p-j-1].push_back(temp);
			}
		}
		SET(dp, -1);
		cout << "Case #" << i+1 << ": " << go(0, 0, 0) << endl;
	}
}
