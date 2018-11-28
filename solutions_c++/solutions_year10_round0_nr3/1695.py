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

const int MAX_N = 1000;
int GROUPS[MAX_N];
int FROM[MAX_N];
int GEN[MAX_N];
int TO[MAX_N];
long long ACC[MAX_N];
int N;

int main(void){
    int N;
    cin >> N;
    for(int i = 0; i < N; i++){
        solve_case(i+1);
    }
    return 0;
}
void advance(int& idx){
    idx++;
    if(idx == N)
        idx = 0;
}

void solve_case(int cn){
    int R, k;
    cin >> R >> k >> N;
    REP(i,N){
        cin >> GROUPS[i];
        TO[i] = -1;
        FROM[i] = -1;
        ACC[i] = 0;
        GEN[i] = -1;
    }
    

    int idx = 0;
    long long total = 0;
    GEN[idx] = 0;
    REP(i, R){
        long long acc = 0;
        assert(GROUPS[idx] <= k);
        acc += GROUPS[idx];
        int old_idx = idx;
        advance(idx);
        while(idx != old_idx && (acc + GROUPS[idx] <= k)){
            acc += GROUPS[idx];
            advance(idx);
        }
        // we are full

        // we cycle
        if(FROM[idx] != -1 && i+1 != R){
            assert(GEN[old_idx] == i);
            int c = GEN[old_idx] - GEN[idx] + 1;
            int a = GEN[idx];
            long long int a_val = ACC[idx];
            long long int c_val = (ACC[old_idx] + acc) - a_val;

            int rep = (R - a) / c;
            int rest = (R-a - rep*c);
                
            int rest_end = idx;
            REP(j,rest){
                rest_end = TO[rest_end];
            }
            long long int rest_val = ACC[rest_end] - ACC[idx];
            
            total = a_val + rep * c_val + rest_val;
            
            // {
            //     DOUT(R); DOUT(k); DOUT(N);
            //     cout << "GROUPS: ";
            //     REP(i, N)
            //         cout << GROUPS[i] << " ";
            //     cout << endl;
            // }

            // cout << "Cycle detected for i=" << i 
            //      << " idx=" << idx 
            //      << " acc=" << acc
            //      << "\n";
            // {
            //     cout << "FROM: ";
            //     REP(i, N)
            //         cout << FROM[i] << " ";
            //     cout << endl;
            // }
            // {
            //     cout << "TO: ";
            //     REP(i, N)
            //         cout << TO[i] << " ";
            //     cout << endl;
            // }
            // {
            //     cout << "ACC: ";
            //     REP(i, N)
            //         cout << ACC[i] << " ";
            //     cout << endl;
            // }
            // {
            //     cout << "GEN: ";
            //     REP(i, N)
            //         cout << GEN[i] << " ";
            //     cout << endl;
            // }

            // cout << "R(" << R << ") factorised as " << a 
            //      << " + " << rep << "*" << c << " + " << rest
            //      << endl;
            // cout << total << " = " 
            //      << a_val << " + " << rep << "*" << c_val
            //      << " + " << rest_val 
            //      << endl;

            break;
        }

        FROM[idx] = old_idx;
        TO[old_idx] = idx;
        ACC[idx] = ACC[old_idx] + acc;
        GEN[idx] = i+1;
        total += acc;
        assert(ACC[idx] == total);

    }

    cout << "Case #" << cn << ": " << total << endl;
}
