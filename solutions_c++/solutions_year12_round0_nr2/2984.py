#include <iostream>
#include <string.h>
#include <string>
#include <math.h>
#include <stdio.h>
#include <conio.h>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <list>
#include <vector>
#include <deque>
#include <functional>

#define pii 2*acos(0)
#define max 100

using namespace std;

int main()
{
    vector<double> v;
    list<double> ilist;
    deque<double> ideq;
    int a,b,c,d,count,fcount,i,j,ns,nd,n,t,points[1000][3],ans[100],score[1000];
    char ch[max];
    string str[max];
    //cout<<setprecision(10)<<pii;
    ifstream infile("B-large.in");
    infile>>t;
    for (i=0;i<t;i++)
    {
      fcount=0;
      count=0;
      infile>>n>>ns>>nd;
      for (j=0;j<n;j++)
      {
          infile>>score[j];
          a=score[j]/3;
          b=score[j]%3;
          if (b==0)
          {
              points[j][0]=a;
              points[j][1]=a;
              points[j][2]=a;
          }
          if (b==1)
          {
              points[j][0]=a;
              points[j][1]=a;
              points[j][2]=a+1;
          }
          if (b==2)
          {
              points[j][0]=a;
              points[j][1]=a+1;
              points[j][2]=a+1;
          }

       if (points[j][2]<nd&&points[j][1]<nd&&points[j][0]<nd)
       {
           if (count<ns&&score[j]!=0)
           {
               c=score[j]-nd-(nd-2);
               d=score[j]-nd-(nd+2);
               if (c<=nd&&c>=nd-2)
               {
                   points[j][0]=nd;
              points[j][1]=nd-2;
              points[j][2]=c;
              count++;

               }
               if (d<=nd&&d>=nd+2)
               {
                   points[j][0]=nd;
              points[j][1]=nd+2;
              points[j][2]=d;
                count++;
               }
           }
       }
       if  (points[j][2]>=nd||points[j][1]>=nd||points[j][0]>=nd)
       {
           fcount++;
       }
       //if (i==2)
       //cout<<points[j][0]<<" "<<points[j][1]<<" "<<points[j][2]<<endl;
      }
      ans[i]=fcount;
    }
    infile.close();
    ofstream outfile("o.out");
    for (i=0;i<t;i++)
    {
       outfile<<"Case #"<<i+1<<": "<<ans[i];
       if (i!=t-1)
       {
           outfile<<endl;
       }
    }
    //cout<<n<<"  "<<ns<<"  "<<nd;
    return 0;
}
