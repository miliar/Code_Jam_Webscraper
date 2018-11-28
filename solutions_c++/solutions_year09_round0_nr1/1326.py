#include <vector>
#include <list>
#include <map>
#include <set>
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
 
using namespace std;
 
#define RP(a,h) for(a=0; a<(h); a++)
#define FR(a,l,h) for(a=(l); a<=(h); a++)
#define GMAX(X, Y) ((X) > (Y) ? (X) : (Y))
#define GMIN(X, Y) ((X) < (Y) ? (X) : (Y))
#define SZ(a) (LL)a.size()
#define ALL(a) a.begin(), a.end()
#define pb push_back
typedef vector <int> VI;
typedef vector <string> VS;
typedef pair<int, int> PII;
#define LL long long

const int INF = 100000000;

bool can[20][200];
int L, D, N;
int ans;
VS a;

void process(string str)
{
	int i = 0, j;
	int cnt = 0;
	while (i < SZ(str))
	{
		if (str[i] == '(')
		{
			FR(j, i+1, SZ(str)-1)
			{
				if (str[j] == ')') break;
				can[cnt][str[j]] = true;
			}
			i = j + 1;
		} else {
			can[cnt][str[i]] = true;
			i++;
		}
		cnt++;
	}

	RP(i, D)
	{
		bool ok = true;
		RP(j, L) if (!can[j][a[i][j]]) { ok=false; break; }
		if (ok) ans++;
	}
}
 
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int tc, testcase, i;
	string str;

	a.clear();
	cin >> L >> D >> N;
	RP(i, D) { cin >> str; a.pb(str); }

	RP(testcase, N)
	{
		cin >> str;
		memset(can, false, sizeof(can));
		ans = 0;
		process(str);
		cout << "Case #" << (testcase+1) << ": " << ans << endl;
	}

	return 0;
}
