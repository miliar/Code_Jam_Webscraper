#include<stdio.h>
#include<stdlib.h>
#include<string.h>

main()
{
 FILE *fp,*of;
 char inp[32];
 int t,n,j,c,i,k;
 scanf("%s",inp);
 fp=fopen(inp,"r");
 of=fopen("test.out","w");
 fscanf(fp,"%d",&t);
 
 for(i=1;i<=t;i++)
 {
  fscanf(fp,"%d%d",&n,&k);
  //c=pow(2,n); 
  c=1;
  for(j=1;j<=n;j++) c*=2;
  k%=c;
  if(k==c-1)
   fprintf(of,"Case #%d: ON\n",i);
  else
   fprintf(of,"Case #%d: OFF\n",i); 
 }
 fclose(fp);
 fclose(of);
 return 0;
}
 
