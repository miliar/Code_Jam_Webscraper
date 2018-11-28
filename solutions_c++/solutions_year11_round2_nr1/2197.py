#include<stdio.h>
FILE *f1=fopen("A-large.in","r");
FILE *f2=fopen("zzrpi.out","w");
char adj[100][100];
double nmt[100];
double nwn[100];
double sum[100];
double owp[100];
double soo[100];
int n;
void rd()
{
 int i,j;
 char x;
 for(i=0;i<n;i++)
 {
   nmt[i]=0;    
   nwn[i]=0;
    fscanf(f1,"%c",&x);
   for(j=0;j<n;j++)
   {
    fscanf(f1,"%c",&adj[i][j]);
    if(adj[i][j] == '.')
    continue;
    nmt[i]++;
    
      if(adj[i][j] == '1')
       nwn[i]++;
   }
   
 }
}
void fowp()
{
 int i,j;
 for(i=0;i<n;i++)
 {
  sum[i]=0;
   for(j=0;j<n;j++)
   {
      if(adj[i][j] == '.')
      continue;
      sum[i]+=(nwn[j]- (adj[j][i]-48) )/(nmt[j]-1) ;
   }
  owp[i]=sum[i]/nmt[i];
 // printf("owp[%d] = %lf",i,owp[i]);
 }
 
}
void foo()
{
 int i,j;
 for(i=0;i<n;i++)
 {
   soo[i]=0;
   for(j=0;j<n;j++)
   {
      if(adj[i][j] == '.')
       continue;
      soo[i]+=owp[j];
   }
    // printf("oowp[%d] = %lf",i,soo[i]/nmt[i]);
 }
}
void rpi()
{
 int i;
 for(i=0;i<n;i++)
  fprintf(f2,"%.12lf\n",(0.25*nwn[i]/nmt[i])+ (0.5*owp[i]) + (0.25*soo[i]/nmt[i]) );
}
int main()
{
 int t,a,i,j;
 fscanf(f1,"%d",&t);
 for(a=0;a<t;a++)
 {
   fscanf(f1,"%d",&n);
   fprintf(f2,"Case #%d:\n",a+1);
   rd();
  // printf("wp[%d] = %lf",i,nwn[i]/nmt[i]);
   fowp();
   foo();
   rpi();
 }
    
    //fscanf(f1,"%*d");
}
 
  /*for(i=0;i<n;i++)
  {
 //    scanf("%c",&x);
    for(j=0;j<n;j++)
    {
     printf("%c",adj[i][j]);
     //if()
    }
    printf("\n");
  }*/
