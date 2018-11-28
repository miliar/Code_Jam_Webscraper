#include<iostream>
#include<algorithm>
using namespace std;


int dp[510][20];

char pattern[]="welcome to code jam";

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	char str[510];
	int T;
	scanf("%d",&T);
	getchar();
	int Case=1;
	while(T--){
		gets(str);
		memset(dp,0,sizeof(dp));
		int len=strlen(pattern);
		int ans=0;
		for(int i=0;str[i]!='\0';i++){
			if(str[i]=='w'){dp[i][0]=1;continue;}
			for(int j=1; j<len;j++){
				if(str[i]==pattern[j]){
					for(int k=i-1;k>=0;k-- ){
						dp[i][j]+=dp[k][j-1];
						dp[i][j]%=10000;
					}
				}
			}
			ans+=dp[i][len-1];
			ans%=10000;
		}
		printf("Case #%d: %04d\n",Case,ans);
		Case++;
	}
	return 0;
}

