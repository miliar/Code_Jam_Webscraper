#include<iostream>
using namespace std;
char str[30]=" welcome to code jam";
int dp[510][20];
char a[510];
void print(int t){
     int temp[4];
     int i;
     for(i=3;i>=0;i--){
                       temp[i]=t%10;
                       t=t/10;
                       }
     for(i=0;i<4;i++)printf("%d",temp[i]);
     printf("\n");
     }
int solve(){
     memset(dp,0,sizeof(dp));
     int i,j;
     int l=strlen(a+1);
     for(i=0;i<=l;i++)dp[i][0]=1;
     for(j=1;j<20;j++){
                       for(i=1;i<=l;i++){
                                        if(a[i]==str[j])dp[i][j]=(dp[i-1][j-1]+dp[i-1][j])%10000;
                                        else dp[i][j]=dp[i-1][j];
                                        }
                       }
     return dp[l][19];
     }
int main(){
    int t;
    scanf("%d",&t);
    gets(a+1);
    int count=1;
    while(t--){
               gets(a+1);
               printf("Case #%d: ",count);
               print(solve());
               count++;
               }
    return 0;
}
