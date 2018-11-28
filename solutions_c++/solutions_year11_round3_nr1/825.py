#include <stdio.h>
#include <math.h>
#include <iostream>
#include <algorithm>
using namespace std;


/*
*/

int main()
{
int n;
char c;
FILE *in = fopen("A.in","r");
FILE *out = fopen("A.out","w");
fscanf(in,"%d",&n);

int ni,nj;
for (int ca=0;ca<n;ca++)
    {
    fscanf(in,"%d %d",&nj,&ni);
    
    bool b[nj][ni];
    for (int j=0;j<nj;j++)
    {
    fscanf(in,"%c",&c);
    for (int i=0;i<ni;i++)
        {
        fscanf(in,"%c",&c);
        if (c=='.') 
           b[j][i]=false;
        else b[j][i]=true;
        }       
    }
    
    int sum=0;
    bool possible=true;
    char d[nj][ni];
    for (int j=0;j<nj;j++)
    for (int i=0;i<ni;i++)
        d[j][i]='.';
        
    for (int j=0;j<nj;j++)
    for (int i=0;i<ni;i++)
        {
        if (b[j][i]) sum++;
        }
    if (sum%4==0)
       {
       for (int j=0;j<nj;j++)
       for (int i=0;i<ni;i++)
           {
           if (b[j][i]) 
              {
              if ((i<ni-1)&&(j<nj-1))
                        {
                        if ((b[j+1][i])&&(b[j][i+1])&&(b[j+1][i+1]))
                           {
                           b[j][i]=false;
                           b[j+1][i]=false;
                           b[j][i+1]=false;
                           b[j+1][i+1]=false;
                           d[j][i]='/';
                           d[j][i+1]='\\';
                           d[j+1][i]='\\';
                           d[j+1][i+1]='/';
                           }
                        else {
                             possible=false;
                             j=nj;
                             i=ni;
                             }
                        }
              else {
                   possible=false;
                   j=nj;
                   i=ni;
                   }
              }
           }
       }
    else possible=false;
    
    fprintf(out,"Case #%d:\n",ca+1);
    if (possible)
       {
       for (int j=0;j<nj;j++)
       {
       for (int i=0;i<ni;i++)  
           fprintf(out,"%c",d[j][i]);
       fprintf(out,"\n");
       }         
       }
    else fprintf(out,"Impossible\n");
    
    }
   fclose(out);          
return 0;
}
