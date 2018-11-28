#include <cstdio>
#include <cstring>

int N,S,Q;
int dp[101][1002];
int qq[1005];
char ss[101][105];

inline int min(int a,int b)
{
	if(a < b) return a;
	return b;
}

void add(char *temp,int s)
{
	for(int i=0;i<S;++i) if(strcmp(temp,ss[i]) == 0) {
		qq[s] = i;
		break;
	}
}

int rec(int i,int j)
{
//	fprintf(stderr,"%d %d %d\n",i,j,qq[j]);
	if(dp[i][j] >= 0) {
//		fprintf(stderr,"dp[%d][%d] = %d\n",i,j,dp[i][j]);
		return dp[i][j];
	}
	if(i == qq[j]) {
		int mm = Q + 1;
		for(int k=0;k<S;++k) if(k != i) mm = min(mm,rec(k,j));
		dp[i][j] = mm + 1;
//		fprintf(stderr,"dp[%d][%d] = %d\n",i,j,dp[i][j]);
		return mm + 1;
	}
	dp[i][j] = rec(i,j+1);
//	fprintf(stderr,"dp[%d][%d] = %d\n",i,j,dp[i][j]);
	return dp[i][j];
}

int main()
{
	scanf("%d\n",&N);
	for(int nn = 1;nn <= N; ++nn) {
		memset(dp,-1,sizeof(dp));
		scanf("%d\n",&S);
		for(int i=0;i<S;++i) {
			char ch = getc(stdin);
			int cc = 0;
			while(ch != '\n') {
				ss[i][cc] = ch;
				cc++;
				ch = getc(stdin);
			}
			ss[i][cc] = 0;
			//fprintf(stderr,"%s\n",ss[i]);
		}
		scanf("%d\n",&Q);
		for(int i=0;i<Q;++i) {
			char ch = getc(stdin);
			int cc = 0;
			char temp[105];
			while(ch != '\n') {
				temp[cc] = ch;
				cc++;
				ch = getc(stdin);
			}
			temp[cc] = 0;
			//fprintf(stderr,"%s\n",temp);
			add(temp,i);
		}
		int mm = Q + 1;
		for(int i=0;i<S;++i) dp[i][Q] = 0;
		for(int i=0;i<S;++i) mm = min(mm,rec(i,0));
		printf("Case #%d: %d\n",nn,mm);
	}
	return 0;
}
