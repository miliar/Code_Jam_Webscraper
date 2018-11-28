//{{{
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <utility>
#include <queue>
#include <sstream>
using namespace std;
 
typedef long long ll;
typedef pair<int,int> ii;
#define size(x) ((int)(x).size())
#define all(x) (x).begin(),(x).end()
#define pb(x) push_back(x)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i) 
#define REP(i,n) FOR(i,0,(n)-1) 
//}}}

int R, C;
char board[100][100];

bool fillit() {
    REP(i,R) REP(j,C) if( board[i][j] == '#' ) {
        if( i+1 >= R ) return false;
        if( j+1 >= C ) return false;
        if( board[i][j+1] != '#' ) return false;
        if( board[i+1][j] != '#' ) return false;
        if( board[i+1][j+1] != '#' ) return false;
        board[i][j] = '/';
        board[i][j+1] = '\\';
        board[i+1][j] = '\\';
        board[i+1][j+1] = '/';
    }

    REP(i,R) REP(j,C) if( board[i][j] == '#' ) return false;
    return true;
}

int main() {
    // freopen("inp","r",stdin);
    int tn;
    scanf("%d", &tn);

    FOR(cc,1,tn) {
        cin >> R >> C;
        REP(i,R) cin >> board[i];
        printf("Case #%d:\n", cc);
        if( !fillit() ) {
            printf("Impossible\n");
        }
        else {
            REP(i,R) cout << board[i] << endl;
        }
    }
}

