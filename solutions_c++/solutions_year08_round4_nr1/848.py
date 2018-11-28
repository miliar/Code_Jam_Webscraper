#include <stdio.h>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;
int dp[2002][2002];
int add[1000],quit[1000];
char pal[2001],ch;
int a,b,n,m,res;
int main()
{
res=1<<30;
 scanf("%d%d",&m,&n);
  scanf("%s",pal);  
  for(int r=0;r<m;r++)
  {
    scanf("\n%c%d%d",&ch,&a,&b);    
    add[ch]=a,quit[ch]=b;   
  }
  for(int r=n;r>=0;r--)
   {
     for(int c=n;c>=0;c--)
      {
       dp[r][c]=1<<30;          
         if(r==n && c==n)  
          dp[r][c]=0;
         else
           if( r==n )            
               dp[r][c]=min( dp[r][c+1]+add[pal[c]],dp[r][c+1]+quit[pal[c]] );            
           else
            if( c==n )
            {
             int pos=n-r-1;
              dp[r][c]=min( dp[r+1][c]+ add[ pal[ pos ] ],dp[r+1][c]+quit[ pal[pos] ] );
            } 
            else
            {            
               int pos=n-r-1;                     
               dp[r][c]=min( dp[r+1][c]+ add[ pal[ pos ] ],dp[r+1][c]+quit[ pal[pos] ] );                                     
               dp[r][c]=min( dp[r][c],min(dp[r][c+1]+add[pal[c]],dp[r][c+1]+quit[pal[c]] ));               
               dp[r][c]=min(dp[r][c],dp[r+1][c+1]+ quit[pal[pos]]+quit[pal[c]] );               
               dp[r][c]=min(dp[r][c],dp[r+1][c+1]+ add[pal[pos]]+add[pal[c]] );
               dp[r][c]=min(dp[r][c],dp[r+1][c+1]+ quit[pal[pos]]+add[pal[c]] );
               dp[r][c]=min(dp[r][c],dp[r+1][c+1]+ add[pal[pos]]+quit[pal[c]] );
               if( pal[pos]==pal[c] )
                   dp[r][c]=min( dp[r][c],dp[r+1][c+1] );                   
            }
            if(r+c==n || r+c==n-1)
              res=min(res,dp[r][c]);
      }
   }
  /* for(int r=0;r<=n;r++)
   {
    for(int c=0;c<=n;c++)
      printf("%d ",dp[r][c]);
      printf("\n");
    }*/  
   printf("%d\n",res);
   return 0;
}  
