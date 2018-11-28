/*
 * RPI
 * May 21, 2011,
 * Another buggy code by Khaled Samy;)
 */
#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <bitset>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <valarray>
#include <memory.h>
using namespace std;
#define PB                      push_back
#define MP                      make_pair
#define ALL(v)                  v.begin(),v.end()
#define SZ(v)					(int)v.size()
#define CLR(v, d)               memset(v, d, sizeof(v))
#define loop(i,n) 		        for(int i=0;i<(int)n;i++)
#define loop2(i,n,m)            for(int i=n;i<(int)(m);i++)

typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef vector<vd> vvd;
typedef vector<string> vs;
typedef long long ll;
typedef stringstream SS;
typedef pair<int, int> pii;
typedef vector<pii> vpii;

const int OO = (int) 2e9;
const double PI = 2 * acos(0.0);
const double EPS = 1e-9;

int dcmp(double a, double b) {
	return fabs(a - b) <= EPS ? 0 : a > b ? 1 : 2;
}

int DI[] = { -1, 0, 1, 0, 1, -1, -1, 1 };
int DJ[] = { 0, 1, 0, -1, 1, -1, 1, -1 };

int t, n;
char g[101][101];
vector<double> res;
vector<double> wp, owp, oowp;

void clcRPI() {
	// clc wp
	wp.clear();
	loop(i,n) {
		double w = 0.0, tot = 0.0;
		loop(j,n) {
			if (g[i][j] == '1')
				w++;
			if (g[i][j] != '.')
				tot++;
		}
		wp.PB(w / tot);
	}

	// clc owp
	owp.clear();
	loop(i,n) {
		double tot = 0.0;
		double c = 0;
		loop(j,n) {
			if (g[i][j] != '.') {
				c++;
				double tot2 = 0.0, w = 0.0;
				loop(k,n) {
					if (g[j][k] != '.' && k != i)
						tot2++;
					if (g[j][k] == '1' && k != i)
						w++;
				}
				if (tot2 != 0)
					tot += (w / tot2);
				//cout << w << "     " << tot2 << endl;
			}
		}
		if (c != 0)
			tot /= c;

		owp.PB(tot);
	}

	// clc oowp
	oowp.clear();
	loop(i,n) {
		double tot = 0.0, c = 0;
		loop(j,n) {
			if (g[i][j] != '.') {
				c++;
				tot += owp[j];
			}
		}
		if (c != 0)
			tot /= c;
		oowp.PB(tot);
	}

	loop(i,n)
		res.push_back(0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);

}
int main() {
#ifndef ONLINE_JUDGE
	freopen("in.in", "rt", stdin);
	freopen("out.in", "wt", stdout);
#endif
	scanf("%d", &t);
	loop(id,t) {
		scanf("%d", &n);
		loop(i,n)
			loop(j,n)
				cin >> g[i][j];
		res.clear();
		clcRPI();
		printf("Case #%d:\n", id + 1);
		loop(i,SZ(res))
			printf("%0.9lf\n", res[i]);

	}
	return 0;
}
