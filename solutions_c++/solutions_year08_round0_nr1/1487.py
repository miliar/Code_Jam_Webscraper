#include<cstdlib>
#include<cstring>
#include<cstdio>

#define MAXS 105
#define MAXL 105
#define MAXQ 1005
#define INFTY 9999

using namespace std;

char names[MAXS][MAXL], name[MAXL];
int dp[MAXQ][MAXS], q[MAXQ], S, Q;

int main() {
	FILE *fin = fopen("A.in","r"), *fout = fopen("A.out","w");
	int K;
	fscanf(fin,"%d",&K);
	for(int k = 1; k<=K; k++) {
		for(int i = 0; i<MAXS; i++) {
			for(int j = 0; j<MAXL; j++) {
				names[i][j]=0;
			}
			for(int j = 0; j<MAXQ; j++) {
				dp[j][i]=0;
			}
		}
		fscanf(fin,"%d\n",&S);
		for(int i = 0; i<S; i++) {
			fgets(names[i],MAXL,fin);
		}
		fscanf(fin,"%d\n",&Q);
		for(int i = 0; i<Q; i++) {
			fgets(name,MAXL,fin);
//			printf("%s",name);
			for(int j = 0; j<S; j++) {
				if(!strcmp(name,names[j])) {
					q[i]=j;
					break;
				}
			}
//			printf("%d\n",q[i]);
		}
		for(int j = 0; j<S; j++) {
			dp[0][j]=0;
		}
		dp[0][q[0]]=INFTY;
		for(int i = 1; i<Q; i++) {
			for(int j = 0; j<S; j++) {
				if(q[i]==j) {
					dp[i][j]=INFTY;
				} else {
					dp[i][j]=dp[i-1][j];
					for(int k = 0; k<S; k++) {
						if(dp[i-1][k]+1 < dp[i][j])
							dp[i][j] = dp[i-1][k]+1;
					}
				}
//				printf("%d\t",dp[i][j]);
			}
//			printf("\n");
		}
		int ans = INFTY;
		for(int j = 0; j<S; j++) {
			if(dp[Q-1][j]<ans) ans = dp[Q-1][j];
		}
		fprintf(fout,"Case #%d: %d\n",k,ans);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
