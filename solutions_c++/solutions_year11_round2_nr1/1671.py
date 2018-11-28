#include <iostream>
#include <iomanip>
#include <cctype>

#include <algorithm>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<_b; i++)
#define FORE(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define FORDE(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)

#define REP(i,n) FOR(i,0,n)
#define REPSZ(i,v) REP(i,SZ(v)) 


using namespace std;

static void solve_case(int i);

const int MAX_N = 100;

int main(void){
    int N;
    cin >> N;
    for(int i = 0; i < N; i++){
        solve_case(i+1);
    }
    return 0;
}

void solve_case(int cn){
    int matrix[MAX_N][MAX_N];
    int w[MAX_N];
    int op[MAX_N];

    int n;
    cin >> n;

    string line;
    int sum;
    int opp;
    REP(i,n){
	sum = 0;
	opp = 0;
	cin >> line;
	REP(j,n){
	    matrix[i][j] = line[j];
	    if(line[j] == '1'){
		sum++;
	    }
	    if(line[j] != '.'){
		opp++;
	    }
	}
	w[i] = sum;
	op[i] = opp;
    }
    

    double owp[MAX_N];

    REP(i, n){
	double s = 0;
	REP(j,n){	    
	    if(matrix[i][j] != '.'){
		int val = 1;
		if(matrix[i][j] == '1')
		    val = 0;
		s += (w[j] - val)/ (double)(op[j] - 1);
	    }
	}
	owp[i] = s / op[i];
    }
    
    double oowp[MAX_N];
    REP(i,n){
	double s2 = 0;
	REP(j,n){
	    if(matrix[i][j] != '.'){
		s2 += owp[j]; 
	    }
	}
	oowp[i] = s2 / op[i];
    }
    
    cout << "Case #" << cn << ": " << endl;

    
    REP(i,n){
	double rpi = ( w[i] / (float)op[i]) / 4;
	rpi += owp[i] / 2;
	rpi += oowp[i] / 4;
	cout << setprecision(11) << rpi << endl;
    }

}
