#include <cstdio>
#include <cstring>

using namespace std;

char s[]="welcome to code jam";
char buff[505];
const int M=10000;
int dp[505][20];

int ls;

int solve(int i,int pos){
    //printf("%d %d\n",i,pos);
    if(dp[i][pos]==-1){
        dp[i][pos]=0;
        if(buff[i]==s[pos]){
            if(pos==0) dp[i][pos]=1;
            else for(int j=i-1;j>=0;j--)
                dp[i][pos]=(dp[i][pos]+solve(j,pos-1))%M;
        }
    }
    return dp[i][pos];
}

int main(){
    ls=strlen(s);
    gets(buff);
    
    int test;
    sscanf(buff,"%d",&test);
    for(int t=1;t<=test;t++){
        gets(buff);
        memset(dp,-1,sizeof(dp));
        int res=0;
        for(int i=0,sb=strlen(buff);i<sb;i++)
            res=(res+solve(i,ls-1))%M;  
        printf("Case #%d: %04d\n",t,res);
    }
    
    return 0;
}
