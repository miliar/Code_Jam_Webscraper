/* Author: Sandeep */

/* 1. Did u interpret the qns correctly ?
   2. Is your i/o correct ?
   3. Int overflow, double precesion
   4. Array size correct ?
   5. Clearing/resetting vector, map etc.
   6. Stack ovrflow
   7. Global/local conflict
   8. Check for obvious typo(most imp)
   9. Think about edge cases
*/

#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cstring>
#include <memory.h>
#include <cassert>

using namespace std;

#define ford(i, a, b, c)        for(int i=(a); i<(b); i+=(c))
#define fori(i, a, b)           ford(i,a,b,1)
#define rep(i, n)               fori(i,0,n)
#define ifor(i, a, b)           for(int i=(a); i>=(b); i--)
#define iter(i, a)              for(typeof((a).begin()) i=(a).begin(); i!=(a).end(); i++)
#define si(x)                   ((int)x.size())
#define SS                      ({int x;scanf("%d",&x);x;})
#define pb                      push_back
#define mp                      make_pair
#define all(a)                  a.begin(),a.end()
#define fill(a, v)              memset(a, v, sizeof(a))
#define inf                     (int)1e9
#define linf                    (long long)1e18
#define V                       vector
#define S                       string
#define XX                      first
#define YY                      second
#define P(v)                    rep(i, si(v)) cout<<v[i]<<" "; puts("")

typedef V<int> vi;
typedef V<S> vs;
typedef long long ll;
typedef pair<int,int> pii;

ll powModN(ll a, ll b, ll c) {
    ll res = 1;
    while (b){
        if (b%2) res= (res*(ll)a)%c;
        b/=2;
        a=(a*(ll)a)%c;
    }
    return res;
}

/* Program Body starts here */

bool checkRows (char board[4][5], char check) {
	rep(row,4) {
		bool wins = true;
		rep(i,4) {
			if(!(board[row][i]==check || board[row][i] =='T')) {
				wins = false;
				break;
			}
		}
		if(wins) {
			return true;
		}
	}
	return false;
}

bool checkColumns (char board[4][5], char check) {
	rep(col,4) {
		bool wins = true;
		rep(i,4) {
			if(!(board[i][col]==check || board[i][col] =='T')) {
				wins = false;
				break;
			}
		}
		if(wins) {
			return true;
		}
	}
	return false;
}

bool checkDiagonals (char board[4][5], char check) {
	bool returnVal = true;
	rep(i,4) {
		if(!(board[i][i]==check || board[i][i]=='T')) {
			returnVal = false;
			break;
		}
	}
	if(returnVal) {
		return returnVal;
	}
	returnVal = true;
	rep(i,4) {
		if(!(board[i][3-i]==check || board[i][3-i]=='T')) {
			returnVal = false;
			break;
		}
	}
	return returnVal;
}

string main2 () {
	char board[4][5];
	rep(i,4) {
		cin>>board[i];
	}
	/* Check X wins */
	if (checkRows(board,'X') || checkColumns(board,'X') || checkDiagonals(board,'X')) {
		return "X won";
	}
	if (checkRows(board,'O') || checkColumns(board,'O') || checkDiagonals(board,'O')) {
		return "O won";
	}
	rep(i,4) {
		rep(j,4) {
			if(board[i][j]=='.') {
				return "Game has not completed";
			}
		}
	}
	
	return "Draw";
}

int main () {
	int T;
	cin >> T;
	rep(i,T) {
		cout<<"Case #"<<i+1<<": "<<main2()<<endl;
	}
}