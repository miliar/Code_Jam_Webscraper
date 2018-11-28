#include <iomanip>
#include <iostream>
#include <string>

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)

using namespace std;

static void solve_case(int i);

int main(void){

    int N;
    string w;
    cin >> N;
    getline(cin,w);
    for(int i = 0; i < N; i++){
	solve_case(i+1);
    }

    return 0;
}

const int MOD = 10000;
const int MAX_S = 500;
const int W_SIZE= 19;

const char * WELCOME = "welcome to code jam";

short T[W_SIZE][MAX_S];

void solve_case(int cn){
    string w;
    getline(cin,w);

    int S = w.size();
    REP(j,S){
	T[W_SIZE-1][j] = (w[j] == 'm') ? 1 : 0;
    }

    FORD(i,W_SIZE-2,0){

	FORD(j,S-1,0){
	    if(WELCOME[i] != w[j]){
		T[i][j] = 0;
	    } else {
		int sum = 0;
		for(int k = j+1; k < S; k++){
		    sum += T[i+1][k];
		}
		T[i][j] = sum % MOD;
	    }
	}
    }

    int result = 0;
    REP(i,S){
	result += T[0][i];
    }
    result %= MOD;

    cout << "Case #" << cn << ": " << setw(4) << setfill('0') << result << endl;
}
