#include <stdio.h>
#include <algorithm>
#include <string>
using namespace std;
int dp[1000][1000];
char pal[10000];
string jam="welcome to code jam";
int main()
{
    int n;
    gets(pal);
    sscanf(pal,"%d",&n);
    for(int j=0;j<n;j++)
     {
            memset(dp,0,sizeof(dp));
            int res=0;
        gets(pal);
         string s=pal;  
         for( int r=0;r<s.size();r++ )     
           if(  s[r]==jam[0] )
              dp[r][0]++;
         for( int r=0;r<s.size();r++ )     
          {
             for(  int c=1;c<jam.size();c++ )   
              {
                  if( s[r]==jam[c]  )
                   {
                      for(int j=0;j<r;j++)                 
                       dp[r][c]=(dp[r][c]+dp[j][c-1])%10000;
                       if( c==jam.size()-1 )
                        res=(res+dp[r][c])%10000;
                   }
              }
          }
         sprintf(pal,"%d\n",res);
         string ss=pal;
         while(ss.size()<=4)
          ss="0"+ss;
        printf("Case #%d: %s\n",j+1,ss.c_str());
     }
}
