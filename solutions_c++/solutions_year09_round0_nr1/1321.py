#include <iostream>

#define CLEAR(x,c) memset(x,c,sizeof(x))

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)

using namespace std;

static void solve_case(int i);

const int MAX_L = 15;
const int MAX_D = 5000;
const int ALFABET_SIZE = ('z' - 'a') + 1;

int N, L, D;

char dictionary[MAX_D][MAX_L];

int main(void){
    cin >>  L >> D >> N;
    string word;
    REP(i,D){
	REP(j,L){
	    char c;
	    cin >> c;
	    dictionary[i][j] = c;
	}
    }

    for(int i = 0; i < N; i++){
	solve_case(i+1);
    }

    return 0;
}

void solve_case(int cn){
    bool pattern [ALFABET_SIZE][MAX_L] = {false};
    int result = 0;
    char c;
    REP(i,L){
	cin >> c;
	if(c != '('){
	    pattern[c-'a'][i] = 1;
	} else {
	    cin >> c;
	    while(c != ')'){
		pattern[c-'a'][i] = 1;
		cin >> c;
	    }
	}
    }
  

    REP(i,D){
	bool acc = true;
	REP(j,L){
	    acc &= pattern[(dictionary[i][j] - 'a')][j];
	}
	if(acc)
	    result++; 
    }

    cout << "Case #" << cn << ": " << result << endl;
}
