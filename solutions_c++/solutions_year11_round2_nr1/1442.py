#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define all(x) x.begin(), x.end()
#define sz(v) int(v.size())
#define fori(i,b,n) for (int i = b; i < n; i++)
#define forn(i,n) fori(i,0,n)
#define forall(i,v) forn(i,sz(v))
#define var(x,y) typeof(y) x = y
#define foreach(it,v) for (var(it,v.begin()); it != v.end(); it++)
#define forreach(it,v) for (var(it,v.rbegin()); it != v.rend(); it++)
#define pb(x) push_back(x)

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;

typedef set<int> iset;
typedef set<string> sset;

typedef map<int,int> iimap;

typedef vector<int> ivec;
typedef vector<vector<int> > iivec;

int main() {
	int T, N;
	cin >> T;
	for (int CASE = 1; CASE <= T; CASE++) {
		cin >> N;
		string line[N];
		int wc[N], lc[N];
		double WP[N], OWP[N], OOWP[N];
		forn(i,N) {
			cin>>line[i];
			wc[i] = lc[i] = 0;
			WP[i] = OWP[i] = OOWP[i] = 0;
		}			
		printf("Case #%d:\n", CASE);
		forn(i,N) {
			forn(j,N) if (i!=j) {
				switch (line[i][j]) {
					case '1': wc[i]++; break;
					case '0': lc[i]++; break;
				}
			}
			WP[i] = (double)wc[i]/(wc[i]+lc[i]);
		}
		forn(i,N) {
			int count = 0;
			forn(j,N) if (line[i][j] != '.') {
				int w = wc[j], l = lc[j];
				switch (line[j][i]) {
					case '1': w--; break;
					case '0': l--; break;
				}
				OWP[i] += (double)w/(w+l);
				count++;
			}
			OWP[i] /= count;
		}
		forn(i,N) {
			int count = 0;
			forn(j,N) if (line[i][j] != '.') {
				OOWP[i] += OWP[j];
				count++;
			}
			OOWP[i] /= count;
		}
		forn(i,N)
			printf("%.9f\n",  0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]);
	}
	return 0;
}
