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

bool SQ(lint q) {
	if ((lint)(sqrt(q*1.0)+0.00001)*(lint)(sqrt(q*1.0)+0.00001) == q) return true;
	return false;
}

lint T[100];

int main() {
	lint i,j;
	FILE* fp = fopen("D.in","r");
	FILE* fp1 = fopen("D.out","w");
	int t,tt;
	fscanf(fp,"%d",&tt);
	T[0] = 1;
	FOR(i,62) T[i+1] = T[i]*2;
	char buf[100];
	lint A[100],sa;
	lint sp;
	lint q,w;
	FOR(t,tt) {
		fprintf(fp1,"Case #%d: ",t+1);
//		printf("Case #%d: ",t+1);
		fscanf(fp,"%s",buf);
//		scanf("%s",buf);
		sa = strlen(buf);
//		if (t != 3) continue;
		sp = 0;
		FOR(i,sa) {
			if (buf[i] == '?') { A[sa-i-1] = -2; sp++; } else A[sa-i-1] = buf[i]-'0';
		}
		FOR(j,T[sp]) {
			q = w = 0;
			FOR(i,sa) if (A[i] == -2) {
				if ((j & T[w]) != 0) q += T[i];
				w++;
			} else q += A[i]*T[i];
			if (SQ(q)) {
				printf("%lld\n",q);
				FORD(i,sa) if ((q & T[i]) != 0) fprintf(fp1,"1"); else fprintf(fp1,"0");
				fprintf(fp1,"\n");
				break;
			}
		}
	}
	fclose(fp);
	fclose(fp1);
    return 0;
}