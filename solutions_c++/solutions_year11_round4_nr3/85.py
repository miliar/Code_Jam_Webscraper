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
#define mp make_pair

#define FOR(i,n) SFOR(i,0,n)
#define SFOR(i,m,n) for(i=m;i<n;i++)
#define FORD(i,n) for(i=n-1;i>=0;i--)

int A[1001000];
lint P[1000000];
int sp;

int main() {
	int i,j;
	lint N;
	memset(A,0,sizeof(A));
	A[0] = A[1] = 1;
	FOR(i,1001000) if (A[i] == 0) {
		j = 2;
		while (i*j < 1001000) { A[i*j] = 1; j++; }
	}
	sp = 0;
	FOR(i,1001000) if (A[i] == 0) { P[sp] = i; sp++; }
	FILE *fp = fopen("B.in","r");
	FILE *fp1 = fopen("B.out","w");
	int t,tt;
	fscanf(fp,"%d",&tt);
	int ans;
	lint q;
	FOR(t,tt) {
		fscanf(fp,"%lld",&N);
		ans = 0;
		if (N != 1) ans++;
		FOR(i,sp) if (P[i]*P[i] <= N) {
			j = 0;
			q = P[i]*P[i];
			while (q <= N) { q *= P[i]; ans++; }
		}
		fprintf(fp1,"Case #%d: %d\n",t+1,ans);
	}
	fclose(fp);
	fclose(fp1);
	return 0;
}