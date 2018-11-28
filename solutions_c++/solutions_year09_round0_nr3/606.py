#include<cstdio>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<cstring>
#include<cstdlib>

using namespace std;

int n,len;
char wel[20]="welcome to code jam";
char st[510];

main(){
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	cin>>n;
	char buf[10];
	gets(buf);
	for(int i=1;i<=n;++i){
//		scanf("%s",st);
		gets(st);
		len=strlen(st);
		vector<vector<int> > dp(len,vector<int>(19,0));
		for(int j=0;j<len;++j){
			for(int k=0;k<19;++k)if(wel[k]==st[j]){
				if(!k)dp[j][k]=1;
				else{
					for(int l=0;l<j;++l)dp[j][k]+=dp[l][k-1],dp[j][k]%=10000;
				}
			}
		}
/*		for(int j=0;j<len;++j){
			for(int k=0;k<19;++k){
				cout<<dp[j][k]<<" ";
			}
			cout<<endl;
		}
*/		int ans=0;
		for(int j=0;j<len;++j)ans=(ans+dp[j][18])%10000;
		printf("Case #%d: %04d\n",i,ans);
	}
}
