#include <iostream>
#include <iterator>
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

void init(){

}

void solve_case(int cn){
    init();
    string input;
    cin >> input;

    map<char,unsigned> m;
    int act = 0;

    m.insert(MP(input[0],1));

    FOR(i,1,input.size()){
        if(m.find(input[i]) == m.end()){
            m.insert(MP(input[i],act++));
            if(act == 1)
                act = 2;
        }
    }

    unsigned int base = m.size();
    unsigned long long answer = 0UL;

    if(base == 1)
        base = 2;

    REPSZ(i,input){
        answer  *= base;
        answer  += m[input[i]];
    }

    cout << "Case #" << cn << ": " << answer << endl;
}
