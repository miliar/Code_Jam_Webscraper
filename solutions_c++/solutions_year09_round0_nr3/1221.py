#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w+", stdout);

    int tt;
    char ss[1024];
    gets(ss);
    sscanf (ss, "%d", &tt);

    REP (t, tt)
    {
    	cout << "Case #" << t+1 << ": ";

		gets (ss);
		string s = ss;

		string S = "welcome to code jam";

		VVI r(s.size ()+1, VI(S.size ()+1));

		r[0][0] = 1;

		REP (i, s.size ())
			REP (j, S.size ()+1) {
				r[i][j]%=10000;

				r[i+1][j] += r[i][j];

				if (j<S.size ())
					if (s[i] == S[j])
						r[i+1][j+1] += r[i][j];
		}

		int res = r[s.size ()][S.size ()]%10000;

		if (res<1000)
			cout << "0";
		if (res<100)
			cout << "0";
		if (res<10)
			cout << "0";
		cout << res << endl;
    }


    return 0;
}
