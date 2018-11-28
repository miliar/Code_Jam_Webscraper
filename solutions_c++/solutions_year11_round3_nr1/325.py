#include <iostream>
#include <cstdio>
#include <cctype>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <sstream>
#include <fstream>
#include <ctime>
#include <cassert>
#include <cstring>

using namespace std;

#define REP(i,n) FOR(i,0,n)
#define FOR(i,a,b) for(int i = a; i < b; i++)
#define ROF(i,a,b) for(int i=a;i>b;i--)
#define GI ({int t;scanf("%d",&t);t;})
#define GL ({LL t;scanf("%lld",&t);t;})
#define GD ({double t;scanf("%lf",&t);t;})
#define SET(x,a) memset(x,a,sizeof(x))
#define all(a) (a.begin(),a.end())
#define rall(a) (a.rbegin(),a.rend())
#define INF (int)1e9
#define EPS (double)1e-9

typedef unsigned long long ULL;
typedef long long LL;
typedef set <int> si;
typedef pair< int,int > ii;
typedef pair< int, ii > pi;
typedef vector< ii > vii;
typedef vector < vii > vvii;
typedef vector< int > vi;
typedef vector< vi > vvi;

vector<string> board;

int main() {
	int T = GI;
	FOR(t,1,T+1) {
		int R = GI, C = GI;
		board.clear();
		board.resize(R);
		REP(i,R) cin >> board[i];

		REP(i,R-1) {
			REP(j,C-1) {
				if (board[i][j] == '#' && board[i+1][j] == '#' && board[i][j+1] == '#' && board[i+1][j+1] == '#') {
					board[i][j] = board[i+1][j+1] = '/';
					board[i][j+1] = board[i+1][j] = '\\';
				}
			}
		}

		cout << "Case #" << t << ":" << endl;
		bool flag = true;
		REP(i,R) REP(j,C) if (board[i][j] == '#') {
			flag = false;
			break;
		}

		if (flag) {
			REP(i,R) cout << board[i] << endl;
		}
		else cout << "Impossible" << endl;
	}	
	return 0;
}
