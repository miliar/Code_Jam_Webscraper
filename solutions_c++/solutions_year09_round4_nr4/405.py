#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <cstring>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <numeric>
#define beg 10000000
#define pb push_back
#define mp make_pair
#define sz(x) (int)x.size()
#define ss stringstream
#define pf pop_front()
#define nd second
#define st first
#define fr(i, n) for(int i = 0; i < (int)n; i++)
#define LL long long
#define vi vector<int>
#define pii pair<int, int>
#define vii vector<pii >
#define vs vector<string>
#define LD long double

using namespace std;

//always reset global variables!

double dist(double x0, LD y0, LD x1, LD y1) {
	return sqrt((x0 - x1)*(x0 - x1) + (y0 - y1) * (y0 - y1));
}

void solveCase() {
	int n;
	cin >> n;
	int X[50], Y[50], R[50];
	fr(i, n) cin >> X[i] >> Y[i] >> R[i];
	if(n == 1) {
		cout << R[0] << endl;
		return;
	}
	if(n == 2) {
		cout << max(R[0], R[1]) << endl;
		return;
	}
	double mn = beg;
	fr(i, n) {
		vi x, y, r;
		fr(j, n) if(j != i) x.pb(X[j]), y.pb(Y[j]), r.pb(R[j]);
		double t = (dist(x[0], y[0], x[1], y[1]) + r[0] + r[1])/2;
		double mx = R[i];
		mx >?= t;
		mn <?= mx;
	}
	printf("%.5f\n", mn);
}

int main() {
	int t;
	cin >> t;
	fr(i, t) {
		cout << "Case #" << i + 1 << ": ";
		solveCase();
	}
	return 0;
}
