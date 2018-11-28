#pragma comment(linker, "/STACK:16777216")

#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <memory.h>

using namespace std;

#define REP(i,n) for (int i = 0; i < n; ++i)
#define MAX(a,b) ((a)>(b)?(a):(b))
#define SQR(a) (a)*(a)
#define MP make_pair
#define PB push_back
#define FILL(a) memset(a,0,sizeof(a));
#define SIZE(a) (int)((a).size())
#define ALL(a) (a).begin(),(a).end()
#define y1 yyyyyyyyyy1
#define LL long long
#define LD long double
const double PI = 2*acos(0.0);
const double EPS = 1e-8;
const int INF = 1000000000;

int tc, n;
double w, h;
bool istr;
pair<double,int> r[10000];
double x[10000], y[10000];

double smallestY (double loX, double hiX, int cnt){
	double res = -INF;
	REP(i,cnt) if (x[i]+r[i].first > loX && x[i]-r[i].first < hiX){
		res = MAX(res, y[i]+r[i].first);
	}
	return res;
}

bool solve1(){
	double currX = -INF, currY = -INF;
	REP(i,n){
		double nX = currX + r[i].first;
		if (nX < 0 || nX > w+EPS){
			nX = 0;
		}
		double nY = smallestY (nX-r[i].first, nX+r[i].first, i) + r[i].first;
		if (nY < 0) nY = 0;
		if (nY > h+EPS) return false;
		x[i] = nX;
		y[i] = nY;
		currX = nX + r[i].first;
	}
	vector<pair<double,double>> ans(n, MP(0,0));
	REP(i,n) if (!istr) ans[r[i].second] = MP(x[i],y[i]);
	else ans[r[i].second] = MP(y[i],x[i]);
	REP(i,n) printf (" %.8lf %.8lf", ans[i].first, ans[i].second);
	cout << endl;
	return true;
}

void solve(){
	istr = false;
	if (solve1()) return;
	istr = true;
	swap (w, h);
	if (solve1()) return;
	cout<<"FUCK!!!" << endl;
}

int main(){
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
	cin >> tc;
	REP(ic,tc){
		cin >> n >> w >> h;
		REP(i,n){
			cin >> r[i].first;
			r[i].second = i;
		}
		sort (r, r+n);
		reverse (r, r+n);
		cout << "Case #" << ic+1 << ":";
		solve();
	}
	return 0;
};