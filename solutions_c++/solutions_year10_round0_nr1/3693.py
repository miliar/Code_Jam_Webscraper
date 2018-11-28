#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <deque>
#include <cmath>
#include <iostream>
#include <iomanip>
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
    cin >> tt;

    REP (t, tt)
    {
    	cout << "Case #" << t+1 << ": ";
		int n,k;
		cin >> n >> k;

		int r = (1<<n)-1;
		r = ~r;
		r = r|k;
		if(r == -1)
			cout << "ON";
		else
			cout << "OFF";
		

		cout << endl;
	}

    return 0;
}
