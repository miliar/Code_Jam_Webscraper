#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>
#include <functional>
#include <queue>
#include <set>
#include <map>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n);i++)
#define forall(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)

#define DBG(x) cerr << #x << " = " << (x) << endl

typedef long long tint;
typedef long double tdbl;

#define MAXN 128

tint tt;
tint n;
int tab[MAXN][MAXN];
int w[MAXN], p[MAXN];
tdbl wp[MAXN], owp[MAXN], oowp[MAXN];

tdbl rpi(int i) {
	return 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
}

int main() {
	freopen("entrada.in","r",stdin);
	freopen("salida.out","w",stdout);
	cin >> tt;
	forn(t,tt) {
		cin >> n;
		forn(i,n)
			w[i] = p[i] = wp[i] = owp[i] = oowp[i] =  0;
		string bas;
		getline(cin, bas);
		forn(i,n) {
			string buff;
			getline(cin, buff);
			forn(j,n) {
				tab[i][j] = (buff[j] == '1')?1:((buff[j] == '0')?0:-1);
				if (tab[i][j] >= 0)
					p[i]++;
				if (tab[i][j] == 1)
					w[i]++;
			}
		}
		forn(i,n)
			wp[i] = (tdbl)w[i] / (tdbl) p[i];
		forn(i,n) {
			int cant = 0;
			forn(j,n)
			if (tab[j][i] != -1) {
				cant++;
				if (tab[j][i] == 1)
					owp[i] += (tdbl)(w[j] - 1)/(tdbl)(p[j] - 1);
				else
					owp[i] += (tdbl)w[j]/(tdbl)(p[j] - 1);
			}
			owp[i] /= cant;
		}
		forn(i,n) {
			int cant = 0;
			forn(j,n) {
				if ( tab[i][j] != -1) {
					cant++;
					oowp[i] += owp[j];
				}
			}
			oowp[i] /= cant;
		}
		cout << "Case #" << t+1 << ": " << endl;
		cerr << "Case #" << t+1 << ": " << endl;
		forn(i,n) {
			printf("%.20f\n", (double)rpi(i));
			cerr << rpi(i) << endl;

		}
	}
}
