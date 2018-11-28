#include<stdio.h>

//int ai[100],bi[100];
int cal(int ai[],int bi[],int n)
{
int count=0;
 for(int i=0;i<(n-1);i++)
 {
   int x=ai[i]; int y=bi[i];
   for(int j=(i+1);j<n;j++)
   {
   if( x < ai[j] && y > bi[j] ) {count++; }        
   if( x > ai[j] && y < bi[j] ) {count++; }      
   }       
        
 }

return count;
}


int main()
{
freopen("A-large.in","rt",stdin);
freopen("A-large.out","wt",stdout);    

int tests,i;
i=1;
scanf("%d",&tests);    
 while(i<=tests)
 { 
 int n;
 scanf("%d",&n);
 int ai[n],bi[n];
 for(int j=0;j<n;j++)
  {
  scanf("%d %d",&ai[j],&bi[j]);       
  }
  int result=cal(ai,bi,n);
  printf("Case #%d: %d\n",i,result);
 i++;    
 }    
    
    
return 0;    
}
