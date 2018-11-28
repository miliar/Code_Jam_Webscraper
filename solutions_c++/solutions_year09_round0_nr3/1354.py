#include <stdio.h>
#include <string>
#include <algorithm>
using namespace std;

int n,res,len,dp[30][510],a,b,mod=10000;
char buff[600];
char data[]="welcome to code jam";

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&n);
	gets(buff);
	for (int i=0;i<n;i++){
		gets(buff);
		len=strlen(buff);
		for (int k=0;k<len;k++){
			if (k>0) b=dp[0][k-1];
			else b=0;
			if (data[0]==buff[k]) dp[0][k]=(b+1)%mod;
			else dp[0][k]=b%mod;
		}
		for (int j=1;j<19;j++)
			for (int k=0;k<len;k++){
				if ((j>0)&&(k>0)) a=dp[j-1][k-1];
				else a=0;
				if (k>0) b=dp[j][k-1];
				else b=0;
				if (data[j]==buff[k]) dp[j][k]=(a+b)%mod;
				else dp[j][k]=b%mod;
			}
		res=dp[18][len-1]%mod;
		printf("Case #%d: %.4d\n",(i+1),res);
	}
	return 0;
}