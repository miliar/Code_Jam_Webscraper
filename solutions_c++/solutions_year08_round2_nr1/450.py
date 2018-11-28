#include<stdio.h>
#include<cstdlib>
#include<stdlib.h>
const int MAX=150;
__int64 fx[MAX],fy[MAX];
__int64 n,A,B,C,D,M,x,y,N;
FILE *fout;
int main()
{
    int i,j,k;
    fout=fopen("a.out","w");
    scanf("%I64d",&N);
   for(int index=1;index<=N;index++)
   {
      fprintf(fout,"Case #%d: ",index);
      scanf("%I64d%I64d%I64d%I64d%I64d%I64d%I64d%I64d",&n,&A,&B,&C,&D,&x,&y,&M); 
      fx[0]=x;fy[0]=y;         
      for(int i=1;i<n;i++)
      {
      fx[i]=(A*x+B)%M;        
      fy[i]=(C*y+D)%M;
      x=fx[i];
      y=fy[i];   
      //printf("%d %d\n",x,y);     
      }       
      
      int ans=0;
      for(i=0;i<n;i++)for(j=i+1;j<n;j++) for(k=j+1;k<n;k++)
      {
          if(!((fx[i]+fx[j]+fx[k])%3)&&!((fy[i]+fy[j]+fy[k])%3))                               
          ans++;                               
      } 
      fprintf(fout,"%d\n",ans);
              
    }
    
system("pause");
return 0;    
}
