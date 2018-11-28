#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <sstream>
using namespace std;

#define VV vector
#define PB push_back
#define ll long long
#define ld long double
#define REP(i,n) FOR(i,0,(n)-1)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FORE(a,b) for(VAR(a,(b).begin()),VAR(_b,(b).end());a!=_b;++a)
#define VAR(a,b) __typeof(b) a=(b)
#define SS(a) ((int)((a).size()))
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))
#define VI VV<int>
#define VS VV<string>
int COND = 1;
#define DB(x) { if (COND > 0) { COND--; REP (xxx, 1) cerr << __LINE__ << " " << #x << " " << x << endl; cerr.flush(); } }
//--

long A[19];
int go() {
	return 0;
}

int solve() {
    CLR(A, 0);
	string l;
	getline(cin,l);
	REP(i, 500) {
		char c = l[i];
		if(c==0)break;
		switch(c){
			case 'w': {A[0]++; break;}
			case 'e': {A[1]=(A[1]+A[0])%10000; A[6]=(A[6]+A[5])%10000; A[14]=(A[14]+A[13])%10000; break;}
			case 'l': {A[2]=(A[2]+A[1])%10000; break;}
			case 'c': {A[3]=(A[3]+A[2])%10000; A[11]=(A[11]+A[10])%10000; break;}
			case 'o': {A[4]=(A[4]+A[3])%10000; A[9]=(A[9]+A[8])%10000; A[12]=(A[12]+A[11])%10000; break;}
			case 'm': {A[5]=(A[5]+A[4])%10000; A[18]=(A[18]+A[17])%10000; break;}
			case ' ': {A[7]=(A[7]+A[6])%10000; A[10]=(A[10]+A[9])%10000; A[15]=(A[15]+A[14])%10000; break;}
			case 't': {A[8]=(A[8]+A[7])%10000; break;}
			case 'd': {A[13]=(A[13]+A[12])%10000; break;}
			case 'j': {A[16]=(A[16]+A[15])%10000; break;}
			case 'a': {A[17]=(A[17]+A[16])%10000; break;}
		}
	}
    return A[18];
}

int main(int argc, char ** argv) { ios::sync_with_stdio(false);
    COND = argc >= 2 && argv[1][0] == 'q' ? (int)1e9 : 0;
    int T; cin >> T;
	string t;
	getline(cin,t);
    FOR (c, 1, T) {
        printf("Case #%d: %04d\n", c, solve());
    }
    return 0;
}
