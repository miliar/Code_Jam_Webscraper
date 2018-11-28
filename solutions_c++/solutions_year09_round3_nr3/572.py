#include <iostream>
#include <vector>
#include <map>
#include <cctype>
#include <climits>
#include <sstream>
#include <algorithm>
#include <cassert>

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

int  P, Q;

void init(){

}

int Ps[100];
int Qs[5];

int idxs[5];

int min_c;

void generate_idxs(int i){

    if(i == Q){
        int cnt = 0;

        REP(i,P){
            Ps[i] = 1;
        }

        REP(i,Q){
            
            Ps[idxs[i]] = 0;

            int j = idxs[i] - 1;
            while(j>=0 && Ps[j] > 0){
                cnt++;
                j--;
            }

            j = idxs[i] + 1;
            while(j < P && Ps[j] > 0){
                cnt++;
                j++;
            }
        }

        if(min_c > cnt){
            min_c = cnt;
        }

    } else {
    REP(j,Q){
        int k;
        for(k=0;k<i;k++){
            if(idxs[k] == Qs[j])
                break;
        }
        if(k==i){
            idxs[i] = Qs[j];
            generate_idxs(i+1);
        }
    }
    }
}
void solve_case(int cn){
    init();



    cin >> P >> Q;
    min_c = P * Q;
    
    REP(i,Q){
        cin >> Qs[i];
        Qs[i] -= 1;
    }

    generate_idxs(0);
    
    cout << "Case #" << cn << ": " << min_c << endl;
}
