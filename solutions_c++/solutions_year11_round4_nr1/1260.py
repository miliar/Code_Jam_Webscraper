#include <vector>
#include <iostream>
#include <map>
#include <cstdio>
#include <string>
#include <algorithm>
#include <cmath>
#include <queue>
#include <cassert>
using namespace std;
#define mp make_pair
#define pb push_back
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
typedef pair<int, int> pii;
typedef vector<int> vint;

double X, S, R, T, N;
vector<pair<double, double> > V;

typedef pair<double, double> pdd;

/*bool cmp(pdd a, pdd b) {
	return*/ 

void solve(int test) {
	printf("Case #%d:", test);
	cin >> X >> S >> R >> T >> N;
	V.clear();
	for(int i = 0; i < N; ++i) {
		double b, e, w;
		cin >> b >> e >> w;
		V.pb(mp(w, e - b));
		X -= e - b;
	}
	V.pb(mp(0, X));
	sort(all(V));
	//reverse(all(V));
	double ans = 0.0;
	for(int i = 0; i < sz(V); ++i) {
		double runt = min(T, 1.0 * V[i].second / (R + V[i].first));
		ans += runt;
		T -= runt;
		V[i].second -= runt * (R + V[i].first);
		ans += V[i].second / (S + V[i].first);
	}
	printf(" %.8lf\n", ans);
}

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int t;
  scanf("%d", &t);
  for(int i = 1; i <= t; ++i) {
    solve(i);
  }
  return 0;
}
