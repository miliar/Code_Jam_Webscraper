//Using open source library The GNU Multiple Precision Arithmetic Library
//http://gmplib.org/ 

#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <complex>
#include <numeric>
#include <gmp.h> 
#include <stdio.h>
#include <gmpxx.h>

using namespace std;

typedef complex<double> pto;
typedef mpz_class bigInt;

typedef long long LL;
typedef pair<int,int> PII;
typedef pair<int,PII> PIPII;
typedef pair<PII,PII> PIIPII;
typedef pair<LL,LL> PLL;
typedef vector<LL> VLL;
typedef vector<VLL> VVLL;
typedef vector<int> VI;
typedef vector<VI> VII;
typedef vector<bool> VB;
typedef vector<string> VS;

#define REP(i,n) FOR(i,0,n)
#define FOR(i,s,n) for( LL ___n=LL(n), i=LL(s) ; i<___n ; ++i )
#define REPD(i,n) FORD(i,0,n)
#define FORD(i,s,n) for( LL ___s=LL(s), i=LL(n)-1 ; i>=___s ; --i )
#define FOREACH(i,c) for( typeof((c).begin()) i=(c).begin() ; i!=(c).end() ; ++i )
#define ALL(c) (c).begin(), (c).end()
#define SZ(a) ((int)(a).size())
#define PB push_back
#define gbic get_mpz_t

const int mx[] = {-1,0,1,0};
const int my[] = {0,-1,0,1};
const int inf=0x7fffffff;





int main() {
	
	int T;
	cin >> T;
	
	FOR(t, 1, T + 1){
		int N, M;
		LL answer = 0;
		cin >> N >> M;
		set<string> S;
		S.insert("/");
		REP(n, N){
			string s;
			cin >> s;
			FOR(j, 1, s.size()){
				if(s[j] == '/'){
					S.insert(s.substr(0, j));
				}
			}
			S.insert(s);
		}
		REP(m, M){
			string s;
			cin >> s;
			FOR(j, 1, s.size()){
				if(s[j] == '/'){
					if(S.insert(s.substr(0, j)).second == true) answer++;
				}
			}
			if(S.insert(s).second == true) answer++;
		}
		cout<<"Case #"<<t<<": "<<answer<<endl;
	}
				
	    return 0;
}
