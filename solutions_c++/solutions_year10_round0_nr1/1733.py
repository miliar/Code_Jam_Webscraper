#include <iostream>
#include <vector>
#include <map>
#include <cctype>
#include <climits>
#include <sstream>
#include <algorithm>
#include <cassert>
#include <cstring>

#define ALL(v) (v).begin(),(v).end()
#define SORT(x) sort(ALL(x))
#define UNIQUE(x) (SORT(x), (x).resize(unique(ALL(x))-x.begin()))
#define REVERSE(x) reverse(ALL(x))
#define CLEAR(x) memset(x,0,sizeof(x))

#define SZ(v) ((int)(v).size()) 
#define PB push_back 
#define MP make_pair 

#define FOR(i,a,b) for(int i=(a),_b=(b); i<_b; i++)
#define FORE(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define FORDE(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)

#define REP(i,n) FOR(i,0,n)
#define REPSZ(i,v) REP(i,SZ(v)) 

#define DOUT(x) cout << #x << " = " << x << endl;

using namespace std;

static void solve_case(int i);

int main(void){
    int N;
    cin >> N;
    for(int i = 0; i < N; i++){
        solve_case(i+1);
    }
    return 0;
}

void solve_case(int cn){
    int N, K;

    cin >> N >> K;
    
    bool powered = ((K + 1) % (1UL<<N) == 0);

    cout << "Case #" << cn << ": " <<
        (powered ? "ON" : "OFF")
         << endl;
}
