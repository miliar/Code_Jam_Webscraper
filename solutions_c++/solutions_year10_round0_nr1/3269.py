#include <iostream>
#include <math.h>
using namespace std;
int t;
long int N[10000];
long int K[10000];
int main()
    {
          cin>>t;
          int i,j,k;
          for(i=0;i<t;i++)
                          cin>>N[i]>>K[i];
          for(i=0;i<t;i++)
          {
                          long int x=pow(2,N[i]);
                     if((K[i]+1)%x==0)
                                                cout<<"\nCase #"<<i+1<<": "<<"ON";
                     else
                         cout<<"\nCase #"<<i+1<<": "<<"OFF";
          }
    }
