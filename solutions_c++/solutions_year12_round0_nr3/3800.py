#include <cmath>
#include <ctime>
#include <cctype>
#include <cstdio>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#define FOR(i,n) for(int i = 0 ; i < n ; i++)
#define FORL(i,i0,n) for(int i = i0 ; i < n ; i++)
#define FORIT(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();it++)
#define ALL(x) x.begin(), x.end()
#define SZ(x) int(x.size())
#define LEN(x) int(x.length())
#define PB push_back
#define MP make_pair
#define FST(x) (x).first
#define SEC(x) (x).second
#define LL long long
#define mem(x, n) memset(x, n, sizeof(x))
#define ni() ({int t;scanf("%d",&t);t;})
#define SRAND() srand(time(NULL))
#define RAND(from, to) ((rand() % (to-from+1)) + (from))
#if 1
#define DBG(z) cerr << #z << ": " << (z) << endl
#else
#define DBG(z)
#endif
#define LOCAL 0
using namespace std;

const int MAX = 2000002;
set<int> used[MAX];

bool seen_before(int x, int y) {
	int a = min(x, y);
	int b = max(x, y);
	if (used[a].find(b) != used[a].end())
		return true;
	return false;
}

int main() {
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int kases = ni();
	for (int kase = 1; kase <= kases; kase++) {
		FOR(i, MAX) used[i].clear();
		int A = ni(), B = ni();
		int ans = 0;
		for (int x = A; x <= B; x++) {
			stringstream ss;
			ss << x;
			string s;
			ss >> s;
			for (int i = 1; i < SZ(s); i++) {
				string beg = s.substr(0, i);
				string end = s.substr(i, SZ(s) - i);
				string t = end + beg;
				if (SZ(t) != SZ(s))
					continue;
				int y = atoi(t.c_str());
				if (A <= y && y <= B && x != y && !seen_before(x, y)) {
					used[min(x,y)].insert(max(x,y));
					ans++;
				}
			}
		}
		printf("Case #%d: %d\n", kase, ans);
	}
	return 0;
}
