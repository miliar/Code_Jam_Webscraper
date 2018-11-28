#include <vector>
#include <map>
#include <set>
#include <queue>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cassert>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#define For(i,l,h) for (int i = (l); i < (h); ++i)
#define ForU(i,l,h) for (int i = (l); i <= (h); ++i)
#define sz(x) ((int)(x.size()))
#define all(c) (c).begin(),(c).end() 
#define pb push_back 
#define mp make_pair
#define DEBUG(x) x
using namespace std;
typedef vector<int> int1; 
typedef vector<int1> int2; 
typedef vector<string> string1; 
typedef pair<int,int> pii; 
typedef vector<pii> vpii; 
typedef long long lint;
const double eps = 1e-8;
const double pi = acos(-1.0);
const double inf = 1e30;
inline bool Eq(double a, double b) { return fabs(a - b) <= eps; }
inline bool Le(double a, double b) { return a <= b || Eq(a, b); }
inline bool Lt(double a, double b) { return a < b && !Eq(a, b); }
inline bool Ge(double a, double b) { return a >= b || Eq(a, b); }
inline bool Gt(double a, double b) { return a > b && !Eq(a, b); }
inline bool Btw(double x, double lo, double hi) { return Le(min(lo, hi), x) && Le(x, max(lo, hi)); }
inline bool TestBit(int x, int p) { return (x >> p) & 1; }
inline void SetBit(int &x, int p) { x |= (1 << p); }
inline void ResetBit(int &x, int p) { x &= ~(1 << p); }
struct Point { double x, y; Point(double x = 0, double y = 0) : x(x), y(y) {} };
const int INF = 1 << 30;
const int MAXN = 300;

struct Item {
	int l, r;
};

bool operator <(const Item &a, const Item &b) {
	if (a.l != b.l) return a.l < b.l;
	return a.r < b.r;
}

Item A[MAXN + 10];
int N, M;
int L[MAXN + 10];
int R[MAXN + 10];
char buf[100];
map<string, int> id;
int CurColor;
int C[MAXN + 10];

int GetId(string &s) {
	map<string, int>::iterator it = id.find(s);
	if (it == id.end()) {
		id[s] = CurColor++;
		//it->second = CurColor++;
		return CurColor - 1;
	}
	return id[s];
}



//int DP[11][10000 + 10][1024]; 
int DP[MAXN + 10][10000 + 10];

void InitDP() {
	for (int i = 0; i <= M; ++i)
		for (int j = 0; j <= 10001; ++j)
			DP[i][j] = -1;
}

int rec(int k, int beg) {
	if (DP[k][beg] != -1) return DP[k][beg];
	if (beg > 10000) return DP[k][beg] = 0;
	if (k == M) {
		if (beg > 10000) return DP[k][beg] = 0;
		else return DP[k][beg] = INF;
	}
	if (L[k] > beg) return DP[k][beg] = INF;
	int t1 = rec(k + 1, R[k] + 1);
	int t2 = rec(k + 1, beg);
	if (t1 != INF) ++t1;
	return DP[k][beg] = min(t1, t2);
}

void Solve(int num) {
	scanf("%d", &N);
	CurColor = 0;
	id.clear();
	for (int i = 0; i < N; ++i) {
		scanf("%s %d %d", buf, &A[i].l, &A[i].r);
		string s(buf);
		int j = GetId(s);
		C[i] = j;
	}
	int ans = INF;
	int Fr[10000 + 1];
	memset(Fr, 0, sizeof(Fr));
	for (int use = 1; use < (1 << N); ++use) {
		set<int> set;
		bool ok = true;
		for (int i = 0; i < N; ++i) {
			if (TestBit(use, i)) {
				set.insert(C[i]);
				if (sz(set) > 3) {
					ok = false;
					break;
				}
			}
		}
		if (!ok) continue;
		if (sz(set) > 3) continue;
		set.clear();
		int cnt = 0;
		int val = 0;
		for (int i = 0; i < N; ++i) {
			if (TestBit(use, i)) {
				++cnt;
				//set.insert(C[i]);
				for (int j = A[i].l; j <= A[i].r; ++j) {
					if (use != Fr[j]) ++val;
					Fr[j] = use;
				}
					//set.insert(j);
			}
		}
		if (val == 10000) {
			ans = min(ans, cnt);
		}
	}
	
	if (ans == INF) {
		printf("Case #%d: IMPOSSIBLE\n", num);	
	}
	else 
		printf("Case #%d: %d\n", num, ans);	
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tst = 0;
	cin >> tst;
	for (int i = 1; i <= tst; ++i) Solve(i);		
	return 0;
}