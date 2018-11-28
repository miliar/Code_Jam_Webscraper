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

int main() {
	int i,j,k,p;
	FILE *fp = fopen("A.in", "r");
	FILE *fp1 = fopen("A.out", "w");
	fscanf(fp, "%d", &k);
	FOR(i,k) {
		fscanf(fp,"%d%d",&j,&p);
		if (((p+1)>>j)<<j == p+1) fprintf(fp1, "Case #%d: ON\n", i+1); else fprintf(fp1, "Case #%d: OFF\n", i+1);
	}
	fclose(fp);
	fclose(fp1);
	return 0;
}