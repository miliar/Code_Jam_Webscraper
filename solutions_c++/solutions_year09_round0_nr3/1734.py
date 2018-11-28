#include<iostream>
#include<string>
#define MAX 600
using namespace std;
char str[MAX];
__int64 num[20][MAX];
const char word[20]="welcome to code jam";
int main(){
	//freopen("C-small-attempt2.in","r",stdin);
	//freopen("C-small-attempt2.out","w",stdout);
	
	int n,t=0;
	int i,j,k;
	scanf("%d",&n);
	gets(str);
	while(n--){
		t++;
		gets(str);
		memset(num,0,sizeof(num));
		int len=strlen(str);
		for(i=len-1;i>=0;i--){
			if(str[i]=='m'){
				num[1][i]=1;
			}
		}
		for(i=2;i<=19;i++){
			for(j=len-i;j>=0;j--){
				if(str[j]==word[19-i]){
					for(k=j+1;k<=len-i+1;k++)num[i][j]+=num[i-1][k];
				}
			}
		}
		printf("Case #%d: ",t);
		__int64 temp=0;
		for(i=0;i<len;i++)if(str[i]=='w')temp+=num[19][i];
		if(temp/10==0)printf("000%I64d\n",temp);
		else if(temp/100==0)printf("00%I64d\n",temp);
		else if(temp/1000==0)printf("0%I64d\n",temp);
		else printf("%I64d\n",temp%10000);
	}
	return 0;
}