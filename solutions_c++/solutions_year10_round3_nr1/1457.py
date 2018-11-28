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

#define INPUT_FILE "A-small-attempt0.in.txt"
//#define INPUT_FILE "A-large.in.txt"
#define OUTPUT_FILE "A.out.txt"

//#define INPUT_FILE "B-small-attempt0.in.txt"
//#define INPUT_FILE "B-large.in.txt"
//#define OUTPUT_FILE "B.out.txt"

//#define INPUT_FILE "C-small-attempt0.in.txt"
//#define INPUT_FILE "C-large.in.txt"
//#define OUTPUT_FILE "C.out.txt"

#define MAX_NUM_CABLES 2
//#define MAX_NUM_CABLES 1000

int main()
{
	freopen(INPUT_FILE, "r", stdin);
	freopen(OUTPUT_FILE, "w+", stdout);
	
    int t,n;
	int a[MAX_NUM_CABLES];
	int b[MAX_NUM_CABLES];
    cin >> t;

    REP (i, t)
    {
        cout << "Case #" << (i+1) << ": ";
		cin >> n;		
		
		if (n==1)
		{
			cin >> a[0] >> b[0];
			cout << 0 << endl;
			continue;
		}
		
		REP (j, n)
		{
			cin >> a[j] >> b[j];
		}
		if ((a[0]>a[1] && b[0]<b[1]) || (a[0]<a[1] && b[0]>b[1]))
		{
			cout << 1;
		}
		else
		{
			cout << 0;
		}
        cout << endl;
    }
	
	return 0;
}
