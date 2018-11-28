#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;
#define M 500
#define N 10000
char ckj[M+5]="welcome to code jam";
char sou[M+10];
int len;

struct dot{
	int w,h;
} dp[M+10];

int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int ca,c;
	int i,j,k;
	len=strlen(ckj);

	scanf("%d",&ca);
	gets(sou);
	for(c=1;c<=ca;c++){
		gets(sou);
		memset(dp,-1,sizeof(dp));

		int lenr=strlen(sou);
		for(i=0;i<lenr;i++){
			if(sou[i]==ckj[0]){
				dp[i].w=1;
				dp[i].h=0;
			}
		}

		for(i=1;i<len;i++){			
			for(j=0;j<lenr;j++){
				if(sou[j]==ckj[i]){

					int sum=0;
					for(k=0;k<j;k++){
						if(dp[k].h==i-1){
							sum=sum+dp[k].w;
							sum=sum%N;
						}
					}

					dp[j].h=i;
					dp[j].w=sum;
				}
			}
		}

		int res=0;
		for(i=0;i<lenr;i++){
			if(dp[i].h==len-1){
				res+=dp[i].w;
				res=res%N;
			}
		}
		printf("Case #%d: %04d\n",c,res);
	}
	return 0;
}