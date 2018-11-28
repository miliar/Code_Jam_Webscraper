#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <ctime>

#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <iostream>
#include <numeric>
using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define fornd(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, a, b) for (int i = (int)(a); i <= (int)(b); i++)
#define forabd(i, a, b) for (int i = (int)(b); i >= (int)(a); i--)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define all(a) (a).begin(), (a).end()
#define zero(a) memset(a, 0, sizeof(a))
#define pb push_back
#define mp make_pair


typedef long long int64;
typedef unsigned long long uint64;

template<typename T> int size(const T& c) { return (int)c.size(); }
template<typename T> inline void relaxmin(T& a, const T& b) { if (a > b) a = b; }
template<typename T> inline void relaxmax(T& a, const T& b) { if (a < b) a = b; }
template<typename T> T abs(T x) { return x < 0 ? -x : x; }
template<typename T> T sqr(T x) { return x*x; }
template<typename T> int sign(T x) { return x > 0 ? 1 : (x < 0 ? -1 : 0); }

string str( int i ) { char s[100]; sprintf(s, "%d", i); return string(s); }


void Solve(int caseNo)
{
	int H,W,D;
	scanf("%d%d%d", &H, &W, &D);

	char hh[200][200];
	zero(hh);
	
	int xr;
	int xc;
	string s;
	forn(r,H) {
		cin >> s;
		assert(s.length()==W);
		forn(c, W) {
			if (s[c]=='X') {
				xr = 100 + r - 1;
				xc = 100 + c - 1;
				break;
			}
		}
	}

	int ans=0;
	int h = H - 2;
	int w = W - 2;
	map<pair<int,int>, int> hits;
	forn(r,200)
	forn(c,200) {
		int dr = abs(xr - r);
		int dr1 = abs(200 - xr - 1 - r);
		bool isROk = (dr % (2*h) == 0) || (dr1 % (2*h) == 0);
		int dc = abs(xc - c);
		int dc1 = abs(200 - xc - 1 - c);
		bool isCOk = (dc % (2*w) == 0) || (dc1 % (2*w) == 0);
		if (isROk && isCOk) {
			//hh[r][c] = 'x'
			int ddr = r - xr;
			int ddc = c - xc;
			int d2 = ddr*ddr + ddc*ddc;
			if ((d2 > 0) && (d2 <= D*D)) {
				bool isOK = true;
				while (isOK){
					isOK = false;
					forab(n,2,50) {
						if ((ddr%n == 0) && (ddc%n == 0)) {
							ddr /= n;
							ddc /= n;
							isOK = true;
						}
					}
				}
				pair<int,int> key = make_pair(ddr,ddc);
				if (hits.count(key) == 0) {
					hits[key] = 1;
					ans++;
				}
			}
		}
	}

	printf("Case #%d: %d\n", caseNo, ans);
    //printf( "%2.1f\n", ans );
}


int main()
{
	//if (freopen("c:\\_temp\\D.in", "rt", stdin) == NULL) throw 1;
	//if (freopen("c:\\_temp\\D.out", "wt", stdout) == NULL) throw 2;

	if (freopen("c:\\_temp\\D-small-attempt0.in", "rt", stdin) == NULL) throw 1;
	if (freopen("c:\\_temp\\D-small-attempt0.out", "wt", stdout) == NULL) throw 2;

	//if (freopen("c:\\_temp\\D_test.in", "rt", stdin) == NULL) throw 1;
	//if (freopen("c:\\_temp\\D_test.out", "wt", stdout) == NULL) throw 2;

	//if (freopen("c:\\_temp\\D-large.in", "rt", stdin) == NULL) throw 1;
	//if (freopen("c:\\_temp\\D-large.out", "wt", stdout) == NULL) throw 2;

	int caseCount;
	scanf("%d%", &caseCount);
	clock_t totalNow = clock();

	forab(i, 1, caseCount) {
		clock_t now = clock();
		cerr << "case " << i << "...";
		
		Solve(i);
		fflush(stdout);

		cerr << "Done!; Elapsed ms:" << (double)(clock() - now) * 1000 / CLOCKS_PER_SEC << "\n";
	}
	cerr << "Total elapsed seconds:" << (double)(clock() - totalNow) / CLOCKS_PER_SEC << "\n";

	exit(0);
}