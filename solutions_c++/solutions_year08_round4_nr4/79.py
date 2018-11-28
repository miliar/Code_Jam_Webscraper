#include "header.h"


void init(){
}

void solve() {
	int k;
	string S;
	cin >> k >> S;
	
	vi p(k);
	REP(i, k) p[i] = i;
	
	int res = INT_MAX;
	
	do {
		string A;
		for (int o = 0; o < (int)S.sz; o += k) {
			REP(i, k) A.pb( S[ o + p[i] ] ); 
		}
		res <?= (unique( all(A) ) - A.begin());
	}while(next_permutation( all(p) ));
	
	cout << res;
}
