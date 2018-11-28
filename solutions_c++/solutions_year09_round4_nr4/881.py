#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <string>
#include <vector>
#include <math.h>
#include <queue>
#include <stack>
#include <map>

#define abs(a) (a>=0)?a:(-a)
#define maxi(a,b) (a>b)?a:b

using namespace std;

int main()
{
   int p,q,g,i,j,c,n,x[20],y[20],r[20];
   double d,t[20],ans,temp;
   FILE * pf = fopen("D-small.in","r");
   FILE * rf = fopen("dans.in","w");
   fscanf (pf,"%d",&c);
   for (i=0; i<c; i+=1)
   {
      fscanf (pf,"%d",&n);
      for (j=0; j<n; j+=1)
      {
         fscanf (pf,"%d%d%d",&x[j],&y[j],&r[j]);
      }
      if (n==2)
      {
         fprintf(rf,"Case #%d: %d\n",i+1,maxi(r[0],r[1]));
         
      }
      else if (n==1) fprintf(rf,"Case #%d: %d\n",i+1,r[0]);
      else {
      p=0; q=1; g=0;
      if (r[p]>=r[q])
      {
temp=(x[p]-x[q])*(x[p]-x[q]) + (y[p]-y[q])*(y[p]-y[q]);
         d=sqrt(temp);
         //cout<<"dei  "<<temp<<endl;
         if (r[p]>d+r[q]){t[g]=2*r[p];}
         else t[g]=d+r[p]+r[q]; 
      }
      else
      {
         temp=(x[p]-x[q])*(x[p]-x[q]) + (y[p]-y[q])*(y[p]-y[q]);
         d=sqrt(temp);
        // cout<<"dei  "<<temp<<endl;
         if (r[q]>d+r[p]){t[g]=2*r[q];}
         else t[g]=d+r[p]+r[q]; 
      }
      t[g]=maxi(2*r[2],t[g]);
      p=1; q=2; g++;
      if (r[p]>=r[q])
      {
temp=(x[p]-x[q])*(x[p]-x[q]) + (y[p]-y[q])*(y[p]-y[q]);
         d=sqrt(temp);
        // cout<<"dei  "<<temp<<endl;
         if (r[p]>d+r[q]){t[g]=2*r[p];}
         else t[g]=d+r[p]+r[q]; 
      }
      else
      {
temp=(x[p]-x[q])*(x[p]-x[q]) + (y[p]-y[q])*(y[p]-y[q]);
         d=sqrt(temp);
        // cout<<"dei  "<<temp<<endl;
         if (r[q]>d+r[p]){t[g]=2*r[q];}
         else t[g]=d+r[p]+r[q]; 
      }
      t[g]=maxi(2*r[0],t[g]);
      p=0; q=2; g++;
      if (r[p]>=r[q])
      {
temp=(x[p]-x[q])*(x[p]-x[q]) + (y[p]-y[q])*(y[p]-y[q]);
         d=sqrt(temp);
        // cout<<"dei  "<<temp<<endl;
         if (r[p]>d+r[q]){t[g]=2*r[p];}
         else t[g]=d+r[p]+r[q]; 
      }
      else
      {
temp=(x[p]-x[q])*(x[p]-x[q]) + (y[p]-y[q])*(y[p]-y[q]);
         d=sqrt(temp);
         //cout<<"dei  "<<temp<<endl;
         if (r[q]>d+r[p]){t[g]=2*r[q];}
         else t[g]=d+r[p]+r[q]; 
      }
      t[g]=maxi(2*r[1],t[g]);
      g++;
      ans=t[0];
      for (j=0; j<g; j+=1)
      {
        // cout<<"hello   "<<t[j]<<endl;
         if (t[j]<ans) ans=t[j];
      }
      fprintf(rf,"Case #%d: %lf\n",i+1,ans/2.0);
   }
   }
   return 0;
}
