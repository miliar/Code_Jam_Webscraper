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

int main() {
	FILE *fp = fopen("A.in","r");
	FILE *fp1 = fopen("A.out","w");
	int t,tt,P[2],M[2],bp,bm,ans;
	int i,j,k,n,q;
	char ch;
	fscanf(fp,"%d",&tt);
	FOR(t,tt) {
		fscanf(fp,"%d",&n);
		M[0] = M[1] = ans = 0;
		P[0] = P[1] = 1;
		FOR(i,n) {
			do { fscanf(fp,"%c",&ch); } while ((ch != 'B') && (ch != 'O'));
			fscanf(fp,"%d",&k);
			if (ch == 'B') j = 0; else j = 1;
			q = max(abs(P[j] - k)-M[j],0)+1;
			M[1-j] += q;
			ans += q;
			P[j] = k;
			M[j] = 0;
		}
		fprintf(fp1,"Case #%d: %d\n",t+1,ans);
	}
	fclose(fp);
	fclose(fp1);
	return 0;
}