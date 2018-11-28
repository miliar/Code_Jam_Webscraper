#define _CRT_SECURE_NO_WARNINGS
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <fstream>
#include <iostream>
#include <queue>
#include <algorithm>
#include <time.h>
#include <sstream>
#include <assert.h>
#include <limits>
#define _USE_MATH_DEFINES
#include <math.h>

#define pb(a) push_back(a)
#define sz size()
#define ALL(a) a.begin(),a.end()
#define ALLR(a) a.rbegin(),a.rend()
#define X first
#define Y second
#define mp(a,b) make_pair(a,b)

typedef long long ll;
typedef long double ld;

template<typename T> inline void SWAP(T &a, T &b) {
	T tmp = a;
	a = b;
	b = tmp;
}
template<typename T> inline T ABS(const T &VAL) {
	return VAL < 0 ? -VAL : VAL;
}
template<typename T> inline T MAX(const T &a, const T &b) {
	return a < b ? b : a;
}
template<typename T> inline T MIN(const T &a, const T &b) {
	return a < b ? a : b;
}
template<typename T> inline T SQR(const T &a) {
	return a * a;
}

#define MSET(d) memset(d,0,sizeof(d))
#define forn(i,n) for(int i=0;i!=n;i++)
#define for1(i,n) for(int i=1;i<=n;i++)
#define forab(i,a,b) for(int i=a;i!=b;i++)
#define for1ab(i,a,b) for(int i=a+1;i<=b;i++)
#define fordab(i,a,b) for(int i=b-1;i>=a;i--)
#define ford1ab(i,a,b) for(int i=b;i!=a;i--)
#define ford(i,n) for(int i=n-1;i!=-1;i--)
#define ford1(i,n) for(int i=n;i!=0;i--)

//const int INTinf = 2147483647;
const int INTinf = 1000000005;
const int nINTinf = 0 - 2147483648;
const ll LLinf = 9223372036854775807LL;

using namespace std;
typedef pair<int, int> pii;
typedef unsigned int uint;

int t, n, w, l;
pii r[1005];
ld X[1005];
ld Y[1005];
ld AX[1005];
ld AY[1005];

int main() {
#ifndef ONLINE_JUDGE
	//freopen("output.txt", "w", stdout);
	freopen("input.txt", "r", stdin);
#endif
	cin >> t;
	cout.setf(ios_base::fixed);
	cout.precision(8);
	srand(9);
	for1(x, t) {
		cin >> n >> w >> l;
		forn(i, n) {
			cin >> r[i].X;
			r[i].Y = i;
		}
		sort(r, r + n, greater<pii>());
		X[0] = 0;
		Y[0] = 0;
		X[1] = w;
		Y[1] = l;
		for (int j = 2; j < n; j++) {
			bool ok = false;
			ld sx;
			ld sy;
			while (!ok) {
				sx = rand() % (w + 1);
				sy = rand() % (l + 1);
				ld minrst = numeric_limits<int>::max();
				int nom = 0;
				forn(i,j) {
					ld rst = sqrt((ld) ((sx - X[i]) * (sx - X[i]) + (sy - Y[i]) * (sy - Y[i])));
					rst -= r[i].X;
					if (rst < minrst) {
						minrst = rst;
						nom = i;
					}
				}
				ld needrst = r[j].X + r[nom].X + 0.00001;
				needrst *= needrst;
				ld dx = sx - X[nom];
				ld dy = sy - Y[nom];
				needrst /= sqrt(
						(ld) ((sx - X[nom]) * (sx - X[nom]) + (sy - Y[nom]) * (sy - Y[nom])));
				dx *= minrst;
				dy *= minrst;
				sx = X[nom] + dx;
				sy = Y[nom] + dy;
				if (sx >= 0 && sx <= w && sy >= 0 && sy <= l) {
					ok = true;
					forn(i,j) {
						ld rst = sqrt((ld) ((sx - X[i]) * (sx - X[i]) + (sy - Y[i]) * (sy - Y[i])));
						if (rst < r[i].X + r[j].X + 0.00001) {
							ok = false;
							break;
						}
					}
				}
			}
			X[j] = sx;
			Y[j] = sy;
		}
		cout << "Case #" << x << ": ";
		forn(i,n) {
			AX[r[i].Y] = X[i];
			AY[r[i].Y] = Y[i];
		}
		forn(i,n) {
			cout << AX[i] << ' ' << AY[i] << ' ';
		}
		cout << endl;
	}

#ifndef ONLINE_JUDGE
	//fclose(stdout);
	fclose(stdin);
#endif
	return 0;
}
