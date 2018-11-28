#include <stdio.h>
#include <algorithm>
#include <vector>
#include <math.h>

#define pb push_back

using namespace std;

int T, L, N, t, C;

vector<int> A;
vector<int> D;

bool mycomp (int i, int j) { 
	return (i > j);
}

void solve(int test) {
	int i, j, ok = 1;
	unsigned long long rez = 0;
	
	for (i = 0; i < N; i++) {
		if (rez + 2 * D[i % C] > t && rez < t) {
			A.pb(D[i % C] - (t - rez) / 2);
		}

		if (rez > t) {
			A.pb(D[i % C]);
		}
		
		rez += 2 * D[i % C];
	}

	sort (A.begin(), A.end(), mycomp);

	for (i = 0; i < L; i++) {
		rez -= A[i];
	}
	
	printf("Case #%d: %llu\n", test, rez);	
}

int main () {
	
	int i,j,val;
	char c;
	
	scanf ("%d",&T);
	
	for (i =0; i < T; i++) {
		
		A.clear();
		D.clear();

		scanf("%d %d %d %d", &L, &t, &N, &C);
		
		for (j=0; j<C; j++) {
			scanf("%d", &val);
			D.pb(val);
		}
		solve(i+1);
		
	}
	
}
