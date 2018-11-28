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
	int R,C,D;
	scanf("%d%d%d", &R, &C, &D);

	vector<vector<int>> ww(R,C);
	string s;
	forn(i,R) {
		cin >> s;
		forn(j,C)
		{
			ww[i][j]=s[j]-'0';
		}
	}

	bool isFound = false;
	int maxK = min(R,C);
	forabd(k, 3, maxK)
	{
		forab(r,0, R-k)
		{
			forab(c,0,C-k)
			{
				double centR = r + (double)k / 2;
				double centC = c + (double)k / 2;
				double balX = 0;
				double balY = 0;
				forab(r1,r,r+k-1)
				{
					forab(c1,c,c+k-1)
					{
						if ((r1==r && c1 ==c) || (r1==r && c1 == c+k-1) || (r1==r+k-1 && c1 == c) || (r1==r+k-1 && c1 == c+k-1))
						{
							continue;
						}
						double dx = centC - (c1 + 0.5);
						double dy = centR - (r1 + 0.5);
						balX += dx * (D + ww[r1][c1]);
						balY += dy * (D + ww[r1][c1]);
					}
				}
				if (abs(balX) < 1e-8 && abs(balY) < 1E-8)
				{
					printf("Case #%d: %d\n", caseNo, k);
					return;
				}
			}
		}
	}

	printf("Case #%d: IMPOSSIBLE\n", caseNo);
	return;
}


int main()
{
	//if (freopen("c:\\_temp\\B.in", "rt", stdin) == NULL) throw 1;
	//if (freopen("c:\\_temp\\B.out", "wt", stdout) == NULL) throw 2;

	if (freopen("c:\\_temp\\B-small-attempt0.in", "rt", stdin) == NULL) throw 1;
	if (freopen("c:\\_temp\\B-small-attempt0.out", "wt", stdout) == NULL) throw 2;

	//if (freopen("c:\\_temp\\B_test.in", "rt", stdin) == NULL) throw 1;
	//if (freopen("c:\\_temp\\B_test.out", "wt", stdout) == NULL) throw 2;

	//if (freopen("c:\\_temp\\B-large.in", "rt", stdin) == NULL) throw 1;
	//if (freopen("c:\\_temp\\B-large.out", "wt", stdout) == NULL) throw 2;

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