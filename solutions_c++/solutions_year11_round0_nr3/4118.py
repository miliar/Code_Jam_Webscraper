#include <stdio.h>
#include<iostream>


using namespace std;
int t,tt,n,i,ans,sum,minans,num[10000];
FILE *in,*out;

int main()
{
    in=freopen("C-large.in","r",stdin);
    out=freopen("C-large.out","w",stdout);
    cin>>t;
    tt=t;
    while (tt)
    {
          cin>>n;
          minans=10000000;
          sum=0;
          ans=0;
          for (i=0;i<n;i++)
          {
              cin>>num[i];
              if (num[i]<minans)
                 minans=num[i];
              sum+=num[i];
              ans=ans^num[i];
          }
          if (ans)
             cout<<"Case #"<<t-tt+1<<": NO"<<endl;
          else
              cout<<"Case #"<<t-tt+1<<": "<<sum-minans<<endl;
          tt--;
    }
    return 0;
}
