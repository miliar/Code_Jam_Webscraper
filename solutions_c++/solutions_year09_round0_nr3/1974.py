#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <cmath>
#include <memory.h>

using namespace std;

#define FOR(i,a,b) for(int i=a; i<b; ++i)
#define RFOR(i, a, b) for(int i=b-1; i>=a; --i)
#define FILL(a, val) memset(a, val, sizeof(a))

#define pb push_back
#define sz(c) (int)c.size()
#define all(c) c.begin(),c.end()

#define mp make_pair
#define X first
#define Y second

typedef long int Int;
typedef vector<int> VI;
typedef pair<int, int> PII;

const int INF = 1000000000;
const double PI = acos(-1.0);

string p = ".welcome to code jam.";

int res[509][30];
bool is[509][30];

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int n;
	scanf("%d\n", &n);

	string s;
	FOR(t, 0, n){
		getline(cin, s);
		s = "." + s + ".";
		int m = sz(s);
		FILL(res, 0);
		FILL(is, 0);
		res[0][0] = 1;
		is[0][0] = true;
		FOR(i, 1, m)
		{
			res[i][0] = 0;
			is[i][0] = false;
		}

		FOR(i, 0, m)
			FOR(j, 1, sz(p))
					if (p[j] == s[i])
						FOR(ii, 0, i)
							if (is[ii][j-1])
							{
								res[i][j] = (res[i][j] + res[ii][j-1])%10000;
								is[i][j] = true;
							}

		printf("Case #%d: %04d\n", t+1, res[m-1][sz(p)-1]);
	}
	return 0;
}