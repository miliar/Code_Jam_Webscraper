#include<stdio.h>
#include<cstdlib>
#include<string.h>
#include<stdlib.h>
const int inf=1000;
char eng[15][110];
char qu[110];
int dp[110][15],s,q;
FILE *fin,*fout;
int min(int a,int b)
{
   if(a<b) return a;    
   return b; 
}
int main()
{
  int t,index;
  scanf("%d",&t);
  for(index=1;index<=t;index++)
  {
       int i,j,k,l;          
       scanf("%d",&s);getchar();   
       for(i=1;i<=s;i++) 
       {     
       gets(eng[i]);
       //puts(eng[i]); 
       //putchar('\n');
       }
       for(i=0;i<110;i++) for(j=0;j<15;j++) if(i) dp[i][j]=inf; else dp[i][j]=0;
       
       scanf("%d",&q); getchar();
       for(j=1;j<=q;j++)
       {
           gets(qu);                
           for(i=1;i<=s;i++)
           {
               if(strcmp(eng[i],qu)) 
               {
                  dp[j][i]=min(dp[j][i],dp[j-1][i]);
               }
               else
               {
                   for(k=1;k<=s;k++)    
                   if(strcmp(eng[k],qu))  dp[j][k]=min(dp[j][k],dp[j-1][i]+1);                                 
               }                 
                            
           }            
       }    
       int ans=inf;
       for(i=1;i<=s;i++)
       if(dp[q][i]<ans) ans=dp[q][i];
       printf("Case #%d: %d\n",index,ans);
   } 
system("pause");
return 0;    
}
