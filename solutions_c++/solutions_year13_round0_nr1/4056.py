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

const int MX = 25;

int main(int argc, char *argv[])
{
#ifndef ONLINE_JUDGE
	freopen(argv[1],"r",stdin);
#endif
#ifndef ONLINE_JUDGE
	ifstream cin(argv[1]);
#endif
#if 1
	ofstream cout(argv[2]);
#endif
	int T;
	cin >> T;
	string s[4];
	FOR(t,1,T+1) {
		bool xwon = false, owon = false, draw = false, gamenotcompleted = false;
		int cnt;
		cin >> s[0] >> s[1] >> s[2] >> s[3];
		cout << "Case #" << t << ": ";
		FOR(i,0,4) {
			cnt = 0;
			FOR(j,0,4) if (s[i][j] == 'X' || s[i][j] == 'T') ++cnt;
			if (cnt == 4) {
				xwon = true;
				break;
			}
		}
		if (xwon) { cout << "X won\n"; continue; }
		FOR(j,0,4) {
			cnt = 0;
			FOR(i,0,4) if (s[i][j] == 'X' || s[i][j] == 'T') ++cnt;
			if (cnt == 4) {
				xwon = true;
				break;
			}
		}
		if (xwon) { cout << "X won\n"; continue; }
		cnt = 0;
		FOR(i,0,4) if (s[i][i] == 'X' || s[i][i] == 'T') ++cnt;
		if (cnt == 4) { cout << "X won\n"; continue; }
		cnt = 0;
		FOR(i,0,4) if (s[i][3-i] == 'X' || s[i][3-i] == 'T') ++cnt;
		if (cnt == 4) { cout << "X won\n"; continue; }

		FOR(i,0,4) {
			cnt = 0;
			FOR(j,0,4) if (s[i][j] == 'O' || s[i][j] == 'T') ++cnt;
			if (cnt == 4) {
				owon = true;
				break;
			}
		}
		if (owon) { cout << "O won\n"; continue; }
		FOR(j,0,4) {
			cnt = 0;
			FOR(i,0,4) if (s[i][j] == 'O' || s[i][j] == 'T') ++cnt;
			if (cnt == 4) {
				owon = true;
				break;
			}
		}
		if (owon) { cout << "O won\n"; continue; }
		cnt = 0;
		FOR(i,0,4) if (s[i][i] == 'O' || s[i][i] == 'T') ++cnt;
		if (cnt == 4) { cout << "O won\n"; continue; }
		cnt = 0;
		FOR(i,0,4) if (s[i][3-i] == 'O' || s[i][3-i] == 'T') ++cnt;
		if (cnt == 4) { cout << "O won\n"; continue; }

		FOR(i,0,4) FOR(j,0,4) if (s[i][j] == '.') { gamenotcompleted = true; break; }
		if (gamenotcompleted) cout << "Game has not completed\n";
		else cout << "Draw\n";
	}
	return 0;
}
