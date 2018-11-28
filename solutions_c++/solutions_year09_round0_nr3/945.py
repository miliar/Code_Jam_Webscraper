#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<string>
#include<iostream>
using namespace std;

int dp[505][25],t;
string str="welcome to code jam";

int main() {
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    scanf("%d\n",&t);
    for (int i=0; i<t; i++) {
        string s;
        getline(cin,s);
        memset(dp,0,sizeof(dp));
        if (s[0]=='w') dp[0][1]=1;
        for (int j=0; j<s.length(); j++) {
            dp[j][0]=1; 
            
            //printf("%c: ",s[j]);
            if (j==0) continue;
            for (int k=0; k<19; k++) {
                if (str[k]==s[j]) {
                   dp[j][k+1]=dp[j-1][k]+dp[j-1][k+1];
                   dp[j][k+1]%=10000;
                   }
                   else dp[j][k+1]=dp[j-1][k+1];
                //printf("%d ",dp[j][k]);
                }
            //printf("\n");
            }
        printf("Case #%d: ",i+1);
        int ans=dp[s.length()-1][19],dig=0,ti;
        ti=ans;
        while (ti>0) { dig++; ti/=10; }
        if (ans==0) dig=1;
        for (int i=0; i<4-dig; i++) printf("0");
        printf("%d\n",ans);
        }
    
}
