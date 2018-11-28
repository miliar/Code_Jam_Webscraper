#include <iostream>
#include <cstring>
using namespace std;
char s[100];
int dp[1000][100];
int main(){
    int TC;
    freopen("wel.in","r",stdin);
    freopen("wel.out","w",stdout);
    char key[20]="welcome to code jam";
    
    scanf("%d\n",&TC);
    for (int ii=1;ii<=TC;ii++){
    printf("Case #%d: ",ii);    
        
    gets(s);
    int x=strlen(s);
    //cout<<s<<endl;
    for (int i=0;i<=1000;i++)
     for (int j=0;j<=99;j++)
     dp[i][j]=0;
     
     
    for (int i=0;i<x;i++)
    if(s[i]==key[0]) dp[i][0]=1;
    
    
    for (int i=1;i<=18;i++){
        int total=0;
        for (int j=0;j<x;j++){
            if (s[j]==key[i-1]) {total+=dp[j][i-1];total%=10000;}
            if (s[j]==key[i]) {dp[j][i]+=total;dp[j][i]%=10000; }
            
            }
        }
    int ans=0;
    for (int i=0;i<x;i++){
        ans+=dp[i][18];
        ans%=10000;
        }
        if (ans/1000==0) cout<<"0";
        if (ans/100==0) cout<<"0";
        if (ans/10==0) cout<<"0";
        
        cout<<ans<<endl;}
        
   // system("pause");
    }
