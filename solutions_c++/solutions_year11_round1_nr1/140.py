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
	int i,j,m,n,k;
	FILE* fp = fopen("A.in","r");
	FILE* fp1 = fopen("A.out","w");
	int t,tt;
	fscanf(fp,"%d",&tt);
	lint N;
	FOR(t,tt) {
		fscanf(fp,"%lld %d %d",&N,&i,&j);
		fprintf(fp1,"Case #%d: ",t+1);
		if ((j == 0) && (i != 0)) { fprintf(fp1,"Broken\n"); continue; }
		if ((j == 100) && (i != 100)) { fprintf(fp1,"Broken\n"); continue; }
		if (N < 100) {
			SFOR(k,1,N+1) if ((k*i) % 100 == 0) break;
			if (k == N+1) { fprintf(fp1,"Broken\n"); continue; }
		}
		fprintf(fp1,"Possible\n");
	}
	fclose(fp1);
	fclose(fp);
	return 0;
}