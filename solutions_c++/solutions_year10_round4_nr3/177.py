#include <stdio.h>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <cstring>
using namespace std;
#define REP(i,n) for (int i=0; i<(n); ++i)
#define FOR(i,a,b) for (int i=(a); i<=(b); ++i)
#define FORD(i,a,b) for (int i=(a); i>=(b); --i)
#define FORE(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define debug(x) cerr << #x << " = " << x << "\n";
#define debugv(x) cerr << #x << " = "; FORE(it,(x)) cerr<< *it <<","; cerr<<"\n";
#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define CLR(x) memset(x,0,sizeof x)
#define xx first
#define yy second
typedef long long int lli;
typedef pair<int, int> P;
typedef vector<int> vi;

#define ZAK 107
int T,C,R,X1,X2,Y1,Y2;
bool pl[2][ZAK][ZAK];

int main(){
	cin >> T;
	FOR(cas,1,T){
        CLR(pl);
        cin >> R;
        while(R--){
            cin >> X1 >> Y1 >> X2 >> Y2;
            FOR(x,X1,X2) FOR(y,Y1,Y2) pl[0][x+1][y+1]=true;
        }
            int res = 0;
            while(true){
                bool kon = true;
                REP(i,ZAK) REP(j,ZAK) if(pl[res%2][i][j]) kon = false;
                if(kon) break;
                res++;
                int z = (res+1)%2;
                REP(i,ZAK) REP(j,ZAK) pl[res%2][i][j] = ((pl[z][i-1][j]&pl[z][i][j-1]) | (pl[z][i][j]&(pl[z][i-1][j]|pl[z][i][j-1])));
            }
		cout << "Case #" << cas << ": " << res << endl;
	}
	return 0;
}
