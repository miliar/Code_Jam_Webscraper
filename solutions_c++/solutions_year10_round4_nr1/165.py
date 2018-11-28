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
#define X first
#define Y second
typedef long long int lli;
typedef pair<int, int> P;
typedef vector<int> vi;

#define MAXN 707
#define STALA 307
int T,N,d[MAXN][MAXN];
bool ok[2][MAXN];

int main(){
	cin >> T;
	FOR(cas,1,T){
        //in
        cin >> N; N--;
        CLR(d);
        FOR(i,-N,N){
            int z = min(abs(-N-i), abs(N-i));
            for(int j=-z; j<=z; j+=2){
                cin >> d[STALA+i][STALA+j];
                d[STALA+i][STALA+j]++;
            }
        }
/*        FOR(i,-N,N){
            FOR(j,-N,N)
                cout << d[STALA+i][STALA+j];
                cout << endl;
        }*/
        //sol
        REP(i,MAXN) ok[0][i]=ok[1][i]=true;
        FOR(k,-N,N)
            FOR(i,-N,N)
                FOR(j,-N,N) if(d[STALA+i][STALA+j]){
                    int w = d[STALA + i + 2*(k-i)][STALA + j];
                    if(w != 0 && w != d[STALA + i][STALA + j]) ok[0][STALA+k] = false;
                    w = d[STALA + i][STALA + j + 2*(k-j)];
                    if(w != 0 && w != d[STALA + i][STALA + j]) ok[1][STALA+k] = false;
                }
        int res=MAXN,r0=MAXN,r1=MAXN;
        FOR(k,-N,N) if(ok[0][STALA+k]) r0 = min(r0, abs(k));
        FOR(k,-N,N) if(ok[1][STALA+k]) r1 = min(r1, abs(k));
//        cout << r0 << "  "<< r1 << endl;
        res = N + 1 + r0 + r1;
        //out
		cout << "Case #" << cas << ": " << res*res-(N+1)*(N+1) << endl;
	}
	return 0;
}
