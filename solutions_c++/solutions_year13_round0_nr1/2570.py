#include <algorithm>
#include <numeric>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <complex>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef set<int> se;
typedef pair<int,int> pii;
typedef long long int tint;

#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define decl(v, c) typeof(c) v = c
#define forall(i, c) for(decl(i, c.begin()); i!=c.end(); ++i)
#define rall(c) (c).rbegin(), (c).rend()
#define all(c) (c).begin(), (c).end()
#define D(a) << #a << "=" << a << " "


#define si(a) int((a).size())
#define pb push_back
#define mp make_pair


char T[4][4];


inline bool checkRow(int r,char c) {
    forn(j,4) if (T[r][j] != c) return false;
    return true;
}

inline bool checkCol(int col,char c) {
    forn(i,4) if (T[i][col] != c) return false;
    return true;
}

inline bool checkDiag(char c) {
    bool res = true;
    forn(i,4) if (T[i][i] != c) res = false;

    if (res) return true;

    res = true;

    forn(i,4) if (T[3-i][i] != c) res = false;

    return res;
}

inline bool checkNotOver() {
    forn(i,4) forn(j,4) if (T[i][j] == '.') return true;
    return false;
}

int main () {
	freopen("in.in","r",stdin);
	freopen("out.txt","w",stdout);

    int tt;
    cin >> tt;
    string res;
    int ti,tj;

    forn(caso,tt) {
        res = "";
        forn(i,4) forn(j,4) {
            cin >> T[i][j];
            if (T[i][j] == 'T') {
                ti = i; tj = j;
                T[i][j] = 'X';
            }
        }


        forn(i,4) if (checkRow(i,'X'))  res = "X won";
        forn(i,4) if (checkCol(i,'X'))  res = "X won";
        forn(i,4) if (checkDiag('X'))  res = "X won";

        T[ti][tj] = 'O';
        forn(i,4) if (checkRow(i,'O'))  res = "O won";
        forn(i,4) if (checkCol(i,'O'))  res = "O won";
        forn(i,4) if (checkDiag('O'))  res = "O won";

        if (res == "" && checkNotOver()) res = "Game has not completed";

        res = (res =="" ? "Draw":res);

        cout << "Case #"<<caso+1<<": "<<res<<endl;

    }

  return 0;

}


