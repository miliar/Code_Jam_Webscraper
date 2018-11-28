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
tint r,c;
int tab[MAXN][MAXN];
string str = ".#/\\";

bool sepuede() {
	forn(i,r)
			forn(j,c) {
		if (tab[i][j] == 1) {
			forn(k,2)
				forn(l,2) {
					if (i+k >= r || j+l >=c || tab[i+k][j+l] != 1) {
						return false;
					}
					tab[i+k][j+l] = 2 + (k+l) %2;
			}
		}
	}
	return true;
}

int main() {
	freopen("entrada.in","r",stdin);
	freopen("salida.out","w",stdout);
	cin >> tt;
	forn(t,tt) {
		cin >> r >> c;
		string bas;
				getline(cin, bas);
				forn(i,r) {
					string buff;
					getline(cin, buff);
					forn(j,c) {
						tab[i][j] = (buff[j]=='.')?0:1;
					}
				}

		forn(i,r) {
			forn(j,c)
					cerr << str[tab[i][j]];
			cerr << endl;
		}
		cout << "Case #" << t+1 << ":" << endl ;
		cerr << "Case #" << t+1 << ":" << endl ;
		if (!sepuede()) {
			cout << "Impossible" << endl;
			cerr << "Impossible" << endl;
		} else {
			forn(i,r) {
				forn(j,c) {
					cout << str[tab[i][j]];
					cerr << str[tab[i][j]];
				}
			cout << endl;
			cerr << endl;
			}
		}

	}
}
