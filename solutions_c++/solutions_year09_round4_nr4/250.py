#include <iostream>
#include <cassert>
#include <cstring>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

const int inf = (int)1E+9;

typedef long long int64;
typedef pair<int,int> pii;

#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define all(a) a.begin(), a.end()
#define last(a) (int)a.size() - 1
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define norm(a) sort(all(a)); a.erase(unique(all(a)), a.end());
#define num(a, v) (int)(lower_bound(all(a), v) - a.begin())

const int nmax = 1000;

int n;
double x[nmax], y[nmax], r[nmax];

double dist(double x1, double y1, double x2, double y2){
	return sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
}

int main(){
	freopen ("input.txt", "rt", stdin);
	freopen ("output.txt", "wt", stdout);

	int tst;

	cin >> tst;
	forn(e,tst){
		int n;
		cin >> n;
		forn(i,n)
			cin >> x[i] >> y[i] >> r[i];
		double res = 1e9;
		if (n == 1) res = r[0];
		if (n == 2) res = max(r[0],r[1]);
		if (n == 3){
			forn(i,n)
				forn(j,n)
					if (i != j){
					int  k = 0;
					while (k == i || k == j) k++;
					double e = max(r[i],max(r[j],r[k]));
					double now = max((dist(x[i],y[i],x[j],y[j]) + r[i] + r[j]) / 2.0, e);
					res = min(res,now);
				}
		}
		printf("Case #%d: %0.9lf\n",e+1, res);
	}	

}
