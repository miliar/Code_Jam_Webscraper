#include <iostream>
#include <cstdlib>
#include <string>
#include <sstream>

using namespace std;

string pat = "welcome to code jam";
int dp[501][20];
string s;

int recnt()
{
    int l = s.size();
    if(l<19)return 0;
    for(int i=0;i<=l;i++)dp[i][0]=1;
    if(s[0]=='w')dp[0][1]=1;
    for(int i=1;i<l;i++){
    for(int j=1;j<=19;j++){
      dp[i][j]=dp[i-1][j];
      if(s[i]==pat[j-1]){
        dp[i][j]+=dp[i-1][j-1];
        dp[i][j]%=10000;
      }
    }
    }
   return dp[l-1][19];
}
int main(int argc, char const* argv[])
{
    int t,i=1,val;
    scanf("%d",&t);
    getline(cin,s);
    while (t--) {
      memset(dp,0,sizeof dp);
      getline(cin,s);
      printf("Case #%d: ",i);
      val = recnt();
      { 
        int r=val,cnt=0;
        while(r){cnt++;r/=10;}
        if(cnt<4){cnt=4-cnt;while(cnt--)printf("0");}
        if(val)printf("%d\n",val);
        else printf("\n");
      }
      i++;
    }
    return 0;
}
