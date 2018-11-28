#include <iostream>
#include <vector>
#include <cstring>
#include <cstdio>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<_b; i++)
#define FORE(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define FORDE(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)

#define REP(i,n) FOR(i,0,n)
#define REPSZ(i,v) REP(i,SZ(v))

#define DEBUG

#define NOP do {} while(0)

#if !defined(DEBUG)

#define dprintf(x...)   NOP
#define DOUT(x)         NOP
#define DCOLL(x)        NOP
#define DARR(x,n)       NOP

#else
#define DC(x) cout << "# "#x" = "
#define dprintf(x,...) printf("# " x "\n", ##__VA_ARGS__)
#define DOUT(x) DC(x) << x << endl;
#define DCOLL(x) do { DC(x); \
        FOREACH(it,x){ cout << *it << " "; } \
        cout << endl; } while(0)
#define DARR(x,n) do { DC(x);                     \
        REP(i,n) { cout << x[i] << " "; } \
        cout << endl; } while(0)
#endif

typedef long long ll;
typedef std::vector<ll> VL;
typedef std::vector<VL> VVL;

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
    int L,P,C;
    cin >> L >> P >> C;

    int i = 0;
    ll max_m = C * L;
    
    while(max_m < P){
        
        REP(j, (1<<i))
            max_m *= C;
        i++;

    }
    cout << "Case #" << cn << ": " << i << endl;
}
