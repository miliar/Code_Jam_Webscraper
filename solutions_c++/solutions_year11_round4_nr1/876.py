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
	int X,S,R,t,N;
	scanf("%d%d%d%d%d", &X,&S,&R,&t,&N);

	vector<pair<int,int>> ww(N);
	forn(i,N) {
		int b,e,v;
		cin >> b >> e >> v;
		ww[i].first = v + S;
		ww[i].second = (e-b);
	}

	// Calc zero length
	int len = 0;
	forn(i,N)
	{
		len += ww[i].second;
	}
	assert(X-len >= 0);
	ww.push_back(make_pair(S, X-len));

	sort(all(ww));

	double time = 0;
	double tLeft = t;
	forn(i,ww.size())
	{
		if (tLeft <= 0)
		{
			time += (double)ww[i].second / ww[i].first;
		}
		else
		{
			double fastDt = (double)ww[i].second / (ww[i].first + (R-S));
			if (tLeft >= fastDt)
			{
				tLeft -= fastDt;
				time += fastDt;
			}
			else
			{
				double leftLen = (double)ww[i].second - (ww[i].first + (R-S)) * tLeft;
				time += tLeft;
				tLeft = 0;

				double slowDt = leftLen / ww[i].first;
				time += slowDt;
			}
		}
	}

	printf("Case #%d: %2.8f\n", caseNo, time);
}


int main()
{
	//if (freopen("c:\\_temp\\A.in", "rt", stdin) == NULL) throw 1;
	//if (freopen("c:\\_temp\\A.out", "wt", stdout) == NULL) throw 2;

	//if (freopen("c:\\_temp\\A-small-attempt1.in", "rt", stdin) == NULL) throw 1;
	//if (freopen("c:\\_temp\\A-small-attempt1.out", "wt", stdout) == NULL) throw 2;

	//if (freopen("c:\\_temp\\A_test.in", "rt", stdin) == NULL) throw 1;
	//if (freopen("c:\\_temp\\A_test.out", "wt", stdout) == NULL) throw 2;

	if (freopen("c:\\_temp\\A-large.in", "rt", stdin) == NULL) throw 1;
	if (freopen("c:\\_temp\\A-large.out", "wt", stdout) == NULL) throw 2;

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