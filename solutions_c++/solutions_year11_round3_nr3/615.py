#include <stdio.h>
#include <algorithm>
#include <vector>
#include <math.h>

#define pb push_back

using namespace std;

unsigned long long T, L, N, H;

vector<int> A;

void solve(int test) {
	int j, ok = 1;
	unsigned long long i;
	
	for (i = L; i <= H; i++) {
		ok = 1;
		for (j = 0; j < A.size(); j++) {
			if (A[j] % i != 0 && i % A[j] != 0) {
				ok = 0;
				break;
			}
		}
		
		if (ok) {
			printf("Case #%d: %llu\n", test, i);	
			return;
		}
	}
	
	printf("Case #%d: NO\n", test);	
}

int main () {
	
	int i,j,val;
	char c;
	
	scanf ("%llu",&T);
	
	for (i =0; i < T; i++) {
		
		A.clear();

		scanf("%llu %llu %llu", &N, &L, &H);
		
		for (j=0; j<N; j++) {
			scanf("%d", &val);
			A.pb(val);
		}
		solve(i+1);
		
	}
	
}
