#include<cstdio>
#include<string>

#define MAXLEN 500

using namespace std;

int dp[MAXLEN+1][30];

string wlc="welcome to code jam";

int main()
{
  char linech[MAXLEN+1];
  string line;
  int ntp;
  
  scanf("%d",&ntp);  gets( linech );
    
  for(int i=0;i<=MAXLEN;i++) dp[i][0]=1;
  
  for(int tp=0;tp<ntp;tp++)
  {
    gets( linech ); line=linech;    
    
    for(int i=0; i<line.size();i++)
    {      
      int r=i+1;      
      for(int j=0;j<wlc.size();j++)
      {  
        int s=j+1;
        dp[r][s]=dp[r-1][s];
        if(line[i]==wlc[j]) dp[r][s]+=dp[r-1][s-1];
        dp[r][s]%=10000;
      }
    }
    printf("Case #%d: %04d\n", tp+1, dp[line.size()][wlc.size()]);
  }
}
