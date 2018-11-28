#include <iostream>
#include <vector>

#define REP(i,n) FOR(i,0,n)
#define FOR(i,a,b) for ( int i = a; i < b; i++)

using namespace std;

int main() {
    int t, n, k, i;
    vector<bool> power, state;

    cin >> t;

    REP(i,t) {
        cin >> n >> k;

        power.clear(); state.clear();
        power.resize(n); state.resize(n);
        REP(j,n) {
            power[j] = 0;
            state[j] = 0;
        }
        power[0] = 1;

        REP(j,k) {
            REP(p,n) {
                if (power[p]) {
                    if(state[p] == 0) state[p] = 1;
                    else state[p] = 0;
                }
            }
            FOR(p,1,n) {
                power[p] = (power[p-1] && state[p-1])? 1 : 0 ;
            }
        }

        cout << "Case #" << i+1 << ": ";
        if (power[n-1] && state[n-1]) cout << "ON";
        else cout << "OFF";
        cout << endl;
    }

    return 0;
}
