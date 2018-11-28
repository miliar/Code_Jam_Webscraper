#include <stdio.h>
#include <math.h>
#include <iostream>
#include <algorithm>
using namespace std;


/*
*/
bool myfunction (int i,int j) { return (i<j); }

int main()
{
int nn;
FILE *in = fopen("B.in","r");
FILE *out = fopen("B.out","w");
fscanf(in,"%d",&nn);

for (int ca=0;ca<nn;ca++)
{
int l,t,n,c;
fscanf(in,"%d %d %d %d",&l,&t,&n,&c);
int d[n],e[n];

for (int i=0;i<c;i++)
    fscanf(in,"%d",&d[i]);

for (int i=c;i<n;i++)
    d[i]=d[i%c];
    
int sum=0,lastsum=0;
for (int i=0;i<n;i++)
    {
    lastsum=sum;
    sum+=2*d[i];
    if (sum<t)
       e[i]=0;
       
    else if (lastsum<t)
         e[i]=sum-t;
    else e[i]=2*d[i];
    } 

sort(&e[0],&e[n],myfunction);

double usetrit=0;
double del;
for (int i=n-1;i>=0;i--)
    {
    if (l>0)
       {
       if (e[i]>0) 
          {
          del=e[i];
          usetrit+=del/2;
          l--;
          }
       else i=-2;
       }
    else i=-2;     
    }

int cas=0;
for (int i=0;i<n;i++)
    cas+=d[i]*2;
cas-=usetrit;


    fprintf(out,"Case #%d: %d\n",ca+1,cas);


}
   fclose(out);          
return 0;
}
