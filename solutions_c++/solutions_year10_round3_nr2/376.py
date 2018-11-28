#include<iostream>
#include<math.h>
#include <ext/hash_map>
using namespace std;
int main()
{
    FILE * fin=fopen("c:/in.txt","r");
    FILE * fout=fopen("c:/out.txt","w");
    int t;
    fscanf(fin,"%d",&t);
    for(int a=1;a<=t;a++)
    {
       double l,p,c;
       fscanf(fin,"%lf %lf %lf",&l,&p,&c);
       int cc=0;
       while(l*c<p)
       {
                   
                   cc++;
                   int d=sqrt(l*p);
                   double m,n;
                   m=d;m*=d+1;
                   n=l;n*=p;
                   if(n-m>0) d=d+1;
                   m=d;m*=d;
                   if(n-m>0) l=d; else p=d;
                             
       }
       fprintf(fout,"Case #%d: %d\n",a,cc);
    }
    fclose(fout);
    fclose(fin); 
}
