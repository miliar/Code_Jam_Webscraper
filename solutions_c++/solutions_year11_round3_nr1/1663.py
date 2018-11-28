#include <vector>
#include <numeric>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <limits>
#include <iomanip>

using namespace std;

#define FOR(i,a,b)		for(int i=(a),_b=(b);i<(_b);++i)
#define FORD(i,a,b)		for(int i=(a),_b=(b);i>(_b);--i)
#define pb			push_back
#define mp			make_pair
#define	all(c)			(c).begin(),(c).end()
#define	tr(c,i)	for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define	present(c,x)		((c).find(x) != (c).end())
#define	cpresent(c,x)		(find(all(c),x) != (c).end())

typedef long long			ll;
typedef unsigned long long	ull;
typedef unsigned char	 	byte;
typedef vector<int>			vi;
typedef pair<int, int>		pii;
typedef pair<ll, ll>		pll;
typedef vector<pii>			vpii;

const int N = 55;
int R,C;
char a[N][N];

bool check(int r, int c)
{
	if (r < 0 || r >= R || c < 0 || c >= C)
		return false;
	return true;
}

bool solve()
{
	FOR(i,0,R) {
		FOR(j,0,C) {
			if (a[i][j] == '#') {
				if (check(i+1,j) && check(i,j+1) && a[i+1][j] == '#' &&
					a[i][j+1] == '#' && a[i+1][j+1] == '#') {
					a[i][j] = '/';a[i][j+1] = '\\';
					a[i+1][j] = '\\';a[i+1][j+1] = '/';
				}
			}
		}
	}
	FOR(i,0,R) {
		FOR(j,0,C) {
			if (a[i][j] == '#')
				return false;
		}
	}
	return true;
}

int main(int argc, char *argv[])
{
#if 0
	freopen(argv[1],"r",stdin);
#endif
#if 1
	ifstream cin(argv[1]);
#endif
#if 1
	ofstream cout(argv[2]);
#endif
	int T;
	cin >> T;
	FOR(t,1,T+1) {
		cin >> R >> C;
		FOR(i,0,R) FOR(j,0,C) cin >> a[i][j];
		if (!solve()) {
			cout << "Case #" << t << ":\nImpossible\n";
		} else {
			cout << "Case #" << t << ":\n";
			FOR(i,0,R) {
				FOR(j,0,C) {
					cout << a[i][j];
				}
				cout << "\n";
			}
		}
	}
	return 0;
}
