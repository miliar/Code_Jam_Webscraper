#include <stdio.h>
#include <math.h>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
int t;
FILE *in = fopen("A-large.in","r");
FILE *out = fopen("A-large.out","w");
fscanf(in,"%d",&t);

int n;
for (int ca=0;ca<t;ca++)
    {
    fscanf(in,"%d",&n);
    int o[n+1];
    int oo[n+1];
    int b[n+1];
    int bb[n+1];
    
    o[0]=1;
    b[0]=1;
    
    char h;
    int u;
    for (int i=1;i<n+1;i++)
        {
        fscanf(in,"%c %c",&h,&h);
        fscanf(in,"%d",&u);
        if (h=='O') 
           {
           o[i]=u;
           b[i]=-1;
           }
        else 
             {
             o[i]=-1;
             b[i]=u;
             }
        }
    
    int sec=0;
    int on=1;
    int bn=1;
    for (int i=0;i<n+1;i++)
        {
        if (o[i]==-1)
           {
           bb[bn]=b[i];
           bn++;
           }
        if (b[i]==-1)
           {
           oo[on]=o[i];
           on++;
           }
        }
        
    int bi=1;
    int oi=1;
    int dt;
    for (int i=0;i<n;i++)
        {
        if (o[i+1]==-1)
           {
           dt=b[i+1]-b[i];
           if (dt<0) dt*=-1;
           dt++;
           
           bi++;
           
           if (oo[oi]>o[i])
              {
              if (oo[oi]>o[i]+dt)
                 o[i+1]=o[i]+dt;
              else 
                   o[i+1]=oo[oi];
              }
           else
               {
               if (oo[oi]<o[i]-dt)
                 o[i+1]=o[i]-dt;
              else 
                   o[i+1]=oo[oi];
               }
           }
        else
           {
           dt=o[i+1]-o[i];
           if (dt<0) dt*=-1;
           dt++;
           
           oi++;
           
           if (bb[bi]>b[i])
              {
              if (bb[bi]>b[i]+dt)
                 b[i+1]=b[i]+dt;
              else 
                   b[i+1]=bb[bi];
              }
           else
               {
               if (bb[bi]<b[i]-dt)
                 b[i+1]=b[i]-dt;
              else 
                   b[i+1]=bb[bi];
               }
           }
        sec+=dt;
        }
    
    
    //printf("Case #%d: %d\n",ca+1,sec);
    fprintf(out,"Case #%d: %d\n",ca+1,sec);
   }
             
return 0;
}
