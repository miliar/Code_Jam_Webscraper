#include <iostream>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <numeric>

#include <cstdio>
#include <cmath>
#include <cctype>
#include <cstring>

#include <string>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>

using namespace std;

#define FOREACH(iter, cont) for(__typeof((cont).begin()) iter = (cont).begin(); iter != (cont).end(); iter++)
#define REP(i, end) for(int i = 0; i < (end); i++)
#define CLEAR(arr) memset(arr, 0, sizeof(arr))
#define ALL(cont) (cont).begin(),(cont).end()

const int maxn = 501;

int w[maxn][maxn];
long long s[maxn][maxn];
long long sr[maxn][maxn];
long long sc[maxn][maxn];

int main() {
    int cases;
    cin >> cases;
    for (int cs = 1; cs <= cases; cs++) {
	int n, m, d;
	cin >> n >> m >> d;
	for (int r = 1; r <= n; r++)
	    for (int c = 1; c <= m; c++) {
		char ch;
		cin >> ch;
		w[r][c] =  ch-'0';
	    }


	CLEAR(s);
	CLEAR(sr);
	CLEAR(sc);
	REP(r, n)
	    REP(c, m) {
		s[r+1][c+1] = w[r+1][c+1]+s[r+1][c]+s[r][c+1]-s[r][c];
		sr[r+1][c+1] = w[r+1][c+1]*(r+1)+sr[r+1][c]+sr[r][c+1]-sr[r][c];
		sc[r+1][c+1] = w[r+1][c+1]*(c+1)+sc[r+1][c]+sc[r][c+1]-sc[r][c];
	    }

	int res = 0;
	REP(r, n)
	    REP(c, m)
		for (int k = 3; r+k <= n && c+k <= m; k++) {
		    long long a = s[r+k][c+k]-s[r][c+k]-s[r+k][c]+s[r][c];
		    long long ar = sr[r+k][c+k]-sr[r][c+k]-sr[r+k][c]+sr[r][c];
		    long long ac = sc[r+k][c+k]-sc[r][c+k]-sc[r+k][c]+sc[r][c];

		    a -= w[r+1][c+1]+w[r+1][c+k]+w[r+k][c+1]+w[r+k][c+k];
		    ar -= w[r+1][c+1]*(r+1)+w[r+1][c+k]*(r+1)+w[r+k][c+1]*(r+k)+w[r+k][c+k]*(r+k);
		    ac -= w[r+1][c+1]*(c+1)+w[r+1][c+k]*(c+k)+w[r+k][c+1]*(c+1)+w[r+k][c+k]*(c+k);
		    if (2*ar == (2*r+k+1)*a && 2*ac == (2*c+k+1)*a)
			res = max(res, k);
		}

	cout << "Case #" << cs << ": ";
	if (res == 0)
	    cout << "IMPOSSIBLE" << endl;
	else
	    cout << res << endl;
    }
}
