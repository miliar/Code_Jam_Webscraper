#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <cassert>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define all(a) a.begin(), a.end()
#define fs first
#define sc second
#define mp make_pair
#define pb push_back

typedef pair<int,int> pii;
typedef long long int64;

const int inf = 2 * 1e9 + 2;
const double eps = 1e-6;

double d;
int c;
double p[300], v[300];

void solve(){
	cin >> c >> d;
	int n = 0;
	forn(i, c){
		cin >> p[i] >> v[i];
	}
	double l = 0, r = 1e13;
	forn(i,1000){
		double m = (l + r) / 2.0;
		double now = p[0] - m + d * v[0];
		bool done = 1;
		if (now - p[0] > m + d)
			done = 0;
		for (int i = 1; i < c; i++){
			now = max(now, p[i] - m);
			now += d * v[i];
			if (now - p[i] > m + d)
				done = 0;
		}
		if (done)
			r = m;
		else
			l = m;
	}
	printf("%0.9lf\n", l);

}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tst;
	scanf("%d", &tst);
	for (int i = 0; i < tst; i++){
		printf("Case #%d: ", i + 1);
		solve();
	}

	return 0;
}