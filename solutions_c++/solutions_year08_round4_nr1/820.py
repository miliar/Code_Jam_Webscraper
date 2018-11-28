#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <memory.h>

const int max=1000000;

int n,m,v,i,j,k,br;
int c[110000];
int a[110000][2];
bool sme[110000];

int min(int a,int b)
{
 if (a<b) return a; else return b;   
}

int main()
{
 freopen("A-large.in","r",stdin);
 freopen("zadatak.out","w",stdout);   
 
 scanf("%d",&n);
 for (br=1;br<=n;br++)
 {
   scanf("%d%d",&m,&v);
   for (i=1;i<=(m-1)/2;i++)
   {
    scanf("%d",&(c[i]));
    scanf("%d",&j);
    if (j==1) sme[i]=true; else sme[i]=false;
   }
   for (i=(m-1)/2+1;i<=m;i++)
   {
    scanf("%d",&(c[i]));
    if (c[i]==0) 
    {
     a[i][0]=0;
     a[i][1]=max;
    }
    else
    {
     a[i][0]=max;
     a[i][1]=0;    
    }
   }
   for (i=(m-1)/2;i>=1;i--)
   {
     j=i*2; k=i*2+1;
     a[i][0]=max; a[i][1]=max;
     if (c[i]==1)
     {
      a[i][0]=min(a[i][0],a[j][0]+a[k][0]);           
      a[i][0]=min(a[i][0],a[j][1]+a[k][0]);           
      a[i][0]=min(a[i][0],a[j][0]+a[k][1]);           
      a[i][1]=min(a[i][1],a[j][1]+a[k][1]);           
     }
     else
     {    
      a[i][0]=min(a[i][0],a[j][0]+a[k][0]);           
      a[i][1]=min(a[i][1],a[j][1]+a[k][0]);           
      a[i][1]=min(a[i][1],a[j][0]+a[k][1]);           
      a[i][1]=min(a[i][1],a[j][1]+a[k][1]);           
     }
     if (sme[i])
     {
      if (c[i]==0)
     {
      a[i][0]=min(a[i][0],a[j][0]+a[k][0]+1);           
      a[i][0]=min(a[i][0],a[j][1]+a[k][0]+1);           
      a[i][0]=min(a[i][0],a[j][0]+a[k][1]+1);           
      a[i][1]=min(a[i][1],a[j][1]+a[k][1]+1);           
     }
     else
     {    
      a[i][0]=min(a[i][0],a[j][0]+a[k][0]+1);           
      a[i][1]=min(a[i][1],a[j][1]+a[k][0]+1);           
      a[i][1]=min(a[i][1],a[j][0]+a[k][1]+1);           
      a[i][1]=min(a[i][1],a[j][1]+a[k][1]+1);           
     }          
     }  
   }
   printf("Case #%d: ",br);
   if (a[1][v]>=max) printf("IMPOSSIBLE\n");  
     else printf("%d\n",a[1][v]);  
 }
 
 return 0;
}
