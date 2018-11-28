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

char T[300][300];
int D[300][300];
int A[300];

int main() {
	FILE *fp = fopen("C.in","r");
	FILE *fp1 = fopen("C.out","w");
	int t,tt;
	int i,j,k,n,q,s;
	fscanf(fp,"%d",&tt);
	FOR(t,tt) {
		fscanf(fp,"%d",&n);
		q = 0;
		s = 0;
		k = 1000000000;
		FOR(i,n) {
			fscanf(fp,"%d",&j);
			if (k > j) k = j;
			q ^= j;
			s += j;
		}
		fprintf(fp1,"Case #%d: ",t+1);
		if (q != 0) fprintf(fp1,"NO\n"); else fprintf(fp1,"%d\n",s-k);
	}
	fclose(fp);
	fclose(fp1);
	return 0;
}