#include <iostream>
#include <sstream>
#include <algorithm>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>

#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define debuging

#ifdef debuging
#define FIN  {freopen("new.in" , "r" , stdin) ;}
#define FOUT {freopen("new.out" , "w" , stdout) ;}
#define OUT(x)  {cout<< #x << "  : " << x <<endl ;}
#define ERR(x)  {cout<<"#error: "<< x ; while(1) ;}
#endif

#ifndef debuging
#define FIN  ;
#define FOUT ;
#define OUT(x)  ;
#define ERR(x)  ;
#endif

#define rep(i,a,b) for(int i=(a);i<(int)(b);i++)
#define REP(i,n) rep(i,0,(n))
#define SZ(x) (int)((x).size())
#define CLR(a) memset((a),0,sizeof (a))
#define all(c) (c).begin(), (c).end()
#define iter(c) __typeof((c).begin())
#define contains(c, e) (find(all(c), (e)) != (c).end())
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb(e) push_back(e)
#define mp(a, b) make_pair(a, b)

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> vint;
typedef set<int> sint;
typedef pair<int, int> pint;

const int maxint = -1u >> 2;
const double eps = 1e-8;
const double pi = acos(-1.0);

const int mn = 600;

char a[mn][mn];

int cmp(double x) {
	if (x < -eps)
		return -1;
	return x > eps;
}
int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	int Tn;
	scanf("%d", &Tn);
	for (int Tc = 1; Tc <= Tn; ++Tc) {
		int ans = 0;
		int R, C, D;
		scanf("%d%d%d", &R, &C, &D);
		for (int i = 0; i < R; ++i) {
			scanf("%s",a[i]);
			for (int j = 0; j < C; ++j) {
				a[i][j]-='0';
			}
		}
		for (int l = 3; l <= min(R, C); ++l) {
			for (int i = 0; i < R - l + 1; ++i)
				for (int j = 0; j < C - l + 1; ++j) {
					double cx = (i + l - 1 + i) / 2.0;
					double cy = (j + l - 1 + j) / 2.0;
					double fx = 0, fy = 0;
					for (int p = i; p < i + l; ++p)
						for (int q = j; q < j + l; ++q)
							if ((p != i && p != i + l - 1) || (q != j && q != j
									+ l - 1)) {
								fx += (a[p][q] + D) * (p - cx);
								fy += (a[p][q] + D) * (q - cy);
							}
					if (cmp(fx) == 0 && cmp(fy) == 0)
						if (ans < l)
							ans = l;
				}
		}

		printf("Case #%d: ", Tc);
		// output statement(s);
		if (!ans)
			puts("IMPOSSIBLE");
		else
			printf("%d\n", ans);
	}

	return 0;
}
