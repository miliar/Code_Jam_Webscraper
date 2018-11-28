#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<string>
#include<vector>
#include<math.h>

using namespace std;

FILE *in=fopen("a-small.in","r");
//FILE *in=fopen("a-large.in","r");


FILE *out=fopen("a-small.out","w");
//FILE *out=fopen("a-large.out","w");

int T;
int n;
vector < int > v1,v2;

int main()
{
    char ch;
    int tcase,i,j,t,sum;
    string str;
    
    str="";
    
    fscanf(in,"%d",&T);

    for(tcase=1;tcase<=T;tcase++)
    {
           fscanf(in,"%d",&n);
           //vector 1
           v1.resize(n);
           v2.resize(n);
           for(i=0;i<n;i++)
           {
                           fscanf(in,"%d",&v1[i]);
           }
           // vector 2
           for(i=0;i<n;i++)
           {
                           fscanf(in,"%d",&v2[i]);
           }
           //sort v1
           for(i=0;i<n-1;i++)
           {
                  for(j=i+1;j<n;j++)
                  {
                          if(v1[j]<v1[i])
                          {
                                         t=v1[j];
                                         v1[j]=v1[i];
                                         v1[i]=t;
                          }
                  }
           }
           
           //sort v2
           for(i=0;i<n-1;i++)
           {
                  for(j=i+1;j<n;j++)
                  {
                          if(v2[j]>v2[i])
                          {
                                         t=v2[j];
                                         v2[j]=v2[i];
                                         v2[i]=t;
                          }
                  }
           }
           
           //process
           
           sum=0;
           for(i=0;i<n;i++)
           {
                           sum+=v1[i]*v2[i];
           }
           fprintf(out,"Case #%d: %d\n",tcase,sum);
          
    }
    //cout<<"HIIIIII"<<endl;
    //cin>>ch;
    return 0;
}
