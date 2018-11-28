#include <stdio.h>
#include <algorithm>
#include <vector>
#include <math.h>

#define pb push_back

using namespace std;

int T,N;

vector<int> A;
vector<char> C;

unsigned long long solve() {
	int i,j,o,b;
	unsigned long long sec, osec, bsec;
	
	o = b = 1;
	sec = osec = bsec = 0;

	for (i = 0 ; i < A.size(); i++) {
		if (C[i] == 'O') {
			sec += (sec - osec >= abs(A[i] - o)) ? 1 : abs(A[i] - o) - (sec - osec) + 1; 
			o = A[i];
			osec = sec;
		}
		else {
			sec += (sec - bsec >= abs(A[i] - b)) ? 1 : abs(A[i] - b) - (sec - bsec) + 1; 
			b = A[i];
			bsec = sec;			
		}
	}
	return sec;
}

int main () {

	int i,j,val;
	char c;
	
	scanf ("%d",&T);
	
	for (i =0; i < T; i++) {
		A.clear();
		C.clear();
		
		scanf("%d", &N);
		
		for (j=0; j<N; j++) {
			scanf(" %c %d", &c, &val);
			A.pb(val);
			C.pb(c);
		}
		
		unsigned long long rez = solve();
		printf("Case #%d: %llu\n", i+1, rez);
	}
	
}