#include <iostream>
#include <cmath>
using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define read(x) int x; scanf("%d",&x);
typedef long long int64;

int A[1000],B[1000];

void solve() {
	read(n);
	int i,j;
	REP(i,n) cin >> A[i] >> B[i];
	int64 y = 0;
	REP(i,n) REP(j,n) if (j>i) {
		if (A[j]<A[i] && B[j]>B[i]) y++;
		if (A[j]>A[i] && B[j]<B[i]) y++;
	}	
	cout << y;
}

int main() {
	read(t);
	for (int i=1;i<=t;i++) {
		printf("Case #%d: ",i);
		solve();
		printf("\n");
	}
	return 0;
}
