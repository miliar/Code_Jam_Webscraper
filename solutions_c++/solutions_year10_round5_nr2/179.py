#include <stdio.h>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <utility>
#include <math.h>

using namespace std;

#define lint long long

#define sz size()
#define pb push_back

#define FOR(i,n) SFOR(i,0,n)
#define SFOR(i,m,n) for(i=m;i<n;i++)
#define FORD(i,n) for(i=n-1;i>=0;i--)

int A[100000];
int B[200];

int main() {
	int t,tt,i,j,k,p,q;
	int N;
	lint L;
	int x1, x2, y1, y2, DD;
	FILE *fp = fopen("B.in", "r");
	FILE *fp1 = fopen("B.out", "w");
	fscanf(fp, "%d", &tt);
	FOR(t,tt) {
		fscanf(fp,"%lld%d",&L,&N);
		lint ans = 0;
		FOR(i,N) fscanf(fp,"%d",&B[i]);
		sort(B, B + N);
		ans += ((L - B[N-1]*B[N-1])/B[N-1]);
		L -= ((L - B[N-1]*B[N-1])/B[N-1])*B[N-1];
		FOR(i,L+1) A[i] = 1000000000;
		A[0] = 0;
		FOR(i,L) FOR(j,N) A[i+B[j]] = min(A[i] + 1, A[i+B[j]]);
		if (A[L] >= 1000000) fprintf(fp1,"Case #%d: IMPOSSIBLE\n", t+1); else
		fprintf(fp1,"Case #%d: %lld\n", t+1, ans + A[L]);
	}
	fclose(fp);
	fclose(fp1);
	return 0;
}