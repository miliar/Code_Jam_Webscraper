#include <cstdio>
#include <string>
#include <cstring>
using namespace std;



const char *want="welcome to code jam";

int dp[2][22];
char s[1000];

inline void gao(int &x,int y) {
	if ((x+=y)>=10000) {
		x-=10000;
	}
}

int main() {
int n,last,now,i,j,z,zz;
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	n=strlen(want);
	for (scanf("%d",&zz),gets(s),z=1;z<=zz;++z) {
		gets(s);
		printf("Case #%d: ",z);
		memset(dp[0],0,sizeof(dp[0]));
		dp[0][0]=1;
		for (i=last=0;s[i];++i,last=now) {
			memcpy(dp[now=1-last],dp[last],sizeof(dp[0]));
			for (j=0;j<n;++j) {
				if ((s[i]==want[j]) && (dp[last][j])) {
					gao(dp[now][j+1],dp[last][j]);
				}
			}
		}
		printf("%04d\n",dp[last][n]);
	}
	return 0;
}
	

