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
	FILE *fp = fopen("B.in","r");
	FILE *fp1 = fopen("B.out","w");
	int t,tt,P[2],M[2],bp,bm,ans;
	int i,j,k,n,q;
	char ch,ch1,ch2;
	fscanf(fp,"%d",&tt);
	FOR(t,tt) {
		memset(T,0,sizeof(T));
		memset(D,0,sizeof(D));
		fscanf(fp,"%d",&n);
		FOR(i,n) {
			do { fscanf(fp,"%c",&ch); } while ((ch < 'A') || (ch > 'Z'));
			do { fscanf(fp,"%c",&ch1); } while ((ch1 < 'A') || (ch1 > 'Z'));
			do { fscanf(fp,"%c",&ch2); } while ((ch2 < 'A') || (ch2 > 'Z'));
			T[ch][ch1] = T[ch1][ch] = ch2;
		}
		fscanf(fp,"%d",&n);
		FOR(i,n) {
			do { fscanf(fp,"%c",&ch); } while ((ch < 'A') || (ch > 'Z'));
			do { fscanf(fp,"%c",&ch1); } while ((ch1 < 'A') || (ch1 > 'Z'));
			D[ch][ch1] = D[ch1][ch] = 1;
		}
		fscanf(fp,"%d",&n);
		k = -1;
		for(;n>0;n--) {
			do { fscanf(fp,"%c",&ch); } while ((ch < 'A') || (ch > 'Z'));
			k++;
			A[k] = ch;
			if (k == 0) continue;
			while (k != 0) {
				if (T[A[k]][A[k-1]] != 0) {
					A[k-1] = T[A[k]][A[k-1]];
					k--;
					continue;
				}
				FOR(i,k) if (D[A[k]][A[i]] == 1) {
					k = -1;
				}
				break;
			}
		}
		fprintf(fp1,"Case #%d: [",t+1);
		if (k != -1) fprintf(fp1,"%c",A[0]);
		FOR(i,k) fprintf(fp1,", %c",A[i+1]);
		fprintf(fp1,"]\n");
	}
	fclose(fp);
	fclose(fp1);
	return 0;
}