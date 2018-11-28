#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

int n,m,dp[25];
char s[505],c[25];

int main(){
	strcpy(c,"welcome to code jam");
	scanf("%d",&n);
	gets(s);
	for (int k=1;k<=n;k++){
	gets(s);
	m=strlen(s);
		for (int i=0;i<19;i++) dp[i]=0;
		for (int i=0;i<m;i++)
			for (int j=18;j>=0;j--)
				if (s[i]==c[j]){
					if (j) dp[j]+=dp[j-1];
					else dp[j]++;
				dp[j]%=1000;
				}
	printf("Case #%d: ",k);
		for (int i=1000;i>=1;i/=10) printf("%d",dp[18]/i),dp[18]%=i;
	printf("\n");
	}
	return 0;
}
