#include <iostream>
#include <fstream>
#include<stdlib.h>
#include<stdio.h>
#include<iostream>
using namespace std;

int main()
{
    int t,i,j,p,n,b[101],k,l;
    ifstream s;
    ofstream o("output1.txt");
    s.open("B-large.in");
    s>>t;
    i=1;
    while(i<=t)
    {
              s>>n;
              s>>p;
              s>>l;
              for(j=0;j<n;++j)s>>b[j];
              k=0;
              for(j=0;j<n;++j)
              {
                              if(b[j]%3==0)
                              {
                                           if(b[j]==0)
                                           {
                                                      if(l==0)++k;
                                                      else continue;
                                                      }
                                           else
                                           {
                                           if(b[j]/3>=l)++k;
                                           else
                                           {
                                               if(b[j]/3+1<=10&&b[j]/3+1>=l&&p>0){++k;--p;}
                                               }
                                              }
                                           }
                                           else if(b[j]%3==1)
                                           {
                                                if(b[j]/3+1>=l)++k;
                                                }
                                                else
                                                {
                                                    if(b[j]/3+1>=l&&b[j]/3+1<=10)++k;
                                                    else 
                                                    {
                                                    if(b[j]/3+2>=l&&b[j]/3+2<=10&&p>0){++k;--p;}
                                                         }
                                                    }
                              }
              o<<"Case #"<<i<<": "<<k<<endl;
              ++i;                               
              }
              s.close();
              o.close();
              system("pause");
              return 0;
    }
