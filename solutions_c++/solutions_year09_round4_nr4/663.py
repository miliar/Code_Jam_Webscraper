#include <iostream>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <vector>

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define for1(i, n) for(int i = 1; i < int(n); i++)
#define mp(a, b) make_pair(a, b);
#define X first
#define Y second
#define pb(a) push_back(a)
#define sz(a) a.size()

using namespace std;

typedef long long li;
typedef pair<int, int> pt;

pair<double, double> a[100];
double r[100];
double dist(pair<double, double> a, pair<double, double> b){
	return sqrt((a.X - b.X) * (a.X - b.X) + (a.Y - b.Y) * (a.Y - b.Y));
}
int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t, n;
	cin >> t;
	forn(x, t){
		cin >> n;
		forn(i, n){
			cin >> a[i].X >> a[i].Y >> r[i];
		}
		double R = 1000.0 * 1000.0 * 100.0;
		printf("Case #%d: ", x + 1);
		if (n == 1){
			R = r[0];
			printf("%.6lf\n", R);
			continue;
		}
		if (n == 2){
			R = max(r[0], r[1]);
			printf("%.6lf\n", R);
			continue;
		}
		R = min(R, max(r[0], (dist(a[1], a[2]) + r[1] + r[2]) / 2.0));
		R = min(R, max(r[1], (dist(a[0], a[2]) + r[0] + r[2]) / 2.0));
		R = min(R, max(r[2], (dist(a[1], a[0]) + r[1] + r[0]) / 2.0));
		printf("%.6lf\n", R);
	}
	return 0;
}