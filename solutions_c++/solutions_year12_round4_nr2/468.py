// tuan anh 
// hanoi tower

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <string>
#include <map>
#include <set>
#include <stack>
#include <vector>
#include <queue>

using namespace std;

#define PI acos(-1)
#define MP make_pair
#define PB push_back
#define VI vector <int>
#define PII pair <int, int>
#define LL long long
#define SET(v,i) memset(v, i, sizeof(v))
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define FORD(i,a,b) for (int i = (a); i >= (b); i--)
#define FORN(i,a,b) for (int i = (a); i < (b); i++)
#define DOWN(i,a,b) for (int i = (a); i > (b); i--)
#define FIT(it,v) for (typeof((v.begin()))::iterator it = v.begin(); it != v.end(); it++)
#define FITD(it,v) for (typeof(v)::iterator it = v.rbegin(); it != v.rend(); it++)
#define FREOPEN freopen("hanoi.inp", "r", stdin); freopen("hanoi.out", "w", stdout)

#define maxn 2010

int W, L, n;
int R[maxn];
int cs[maxn];
pair <int, int> P[maxn];

bool cmp (int u, int v) {
	return R[u] > R[v];
}

bool lower(double x, double y) {
	if (fabs(x - y) <= 0.0000001) return false;
	return x < y;
}

bool check(int u, int v) {
	double L = R[u] + R[v];
	
	double L2 = sqrt((double) (P[u].first - P[v].first) * (P[u].first - P[v].first) +
					 (double) (P[u].second - P[v].second) * (P[u].second - P[v].second));

	return lower(L2, L);
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int ntest;
	cin >> ntest;
	FOR (test, 1, ntest) {
		cin >> n >> W >> L;
		FOR (i, 1, n) cin >> R[i];

		cout << "Case #" << test << ": ";
		int X = 0, Y;
		int ok = 1;
		
		FOR (i, 1, n) cs[i] = i;
		sort(cs + 1, cs + 1 + n);
		
		FOR (i, 1, n) {
			Y = 0;
			FOR (j, 1, i - 1)
				if (!(P[cs[j]].first + R[cs[j]] <= X - R[cs[i]] 
				    ||P[cs[j]].first - R[cs[j]] >= X + R[cs[i]] )) Y = max(Y, P[cs[j]].second + R[cs[j]] + R[cs[i]]);
			
			
			P[cs[i]] = MP(X, Y);
			
			if (i == n) break;
			
			if (ok == 1) {
				X += R[cs[i]] + R[cs[i + 1]];
				if (X > W) {
					ok = -1;
					X = W;
				}
			}
			else {
				X -= R[cs[i]] + R[cs[i + 1]];
				if (X < 0) {
					ok = 1;
					X = 0;
				}
			}
			
		}
		
		FOR (i, 1, n) if (P[i].second < 0 || P[i].second > L || P[i].first < 0 || P[i].first > W) cerr<<"??"<<endl ;
		FOR (i, 1, n)
		FOR (j, i + 1, n)
			if (check(i, j)) cerr << "???" << endl;
		
		FOR (i, 1, n) cout << P[i].first << " " << P[i].second << " ";
		cout << endl;
	}
}
