#include<stdio.h>
#include<stdlib.h>
FILE *f1 = fopen("A-large.in","r");
FILE *f2 = fopen("zzzzzzz.out","w");//stdout;
int n;

void prb(int ord)
{
    fscanf(f1,"%d",&n);
    int i,dst,bmv=0,omv=0,rs=0,pb=1,po=1;
    char r;
    for(i=0;i<n;i++)
    {
     fscanf(f1,"%c",&r);
     fscanf(f1,"%c%d",&r,&dst);
     if(r == 'B')
     {
      if(bmv == 0)
       rs+=omv;
      if(abs(pb-dst) > omv)
      bmv+=(abs(pb-dst)-omv);
      bmv++;
      omv = 0;
      pb=dst;
     }
     else
     {
      if(omv == 0)
      rs+=bmv;
      if(abs(po-dst) > bmv)
      {
      omv+=(abs(po-dst)-bmv);
      }
      omv++;
      bmv = 0;
      po=dst;
     }
      //printf("%c %d\n",r,b);
    }
     if(omv == 0)
      rs+=bmv;
     if(bmv == 0)
      rs+=omv;
   fprintf(f2,"Case #%d: %d\n",ord,rs);  
}

int main()
{
    int t,i;
    fscanf(f1,"%d",&t);
    for(i=1;i<=t;i++)
    prb(i);
    //scanf("%*d");
}

