#include<iostream>
using namespace std;
int main()
{int i,t,p,a[100],n,s,sur=0,x,min1,all=0;
    cin>>t;
    x=t;
    while(t--)
    {all=0;
    sur=0;
              cin>>n;
              cin>>s;
              cin>>p;
              for(i=0;i<n;i++)
              cin>>a[i];
                    min1=p*3-4;
    for(i=0;i<n;i++)
    {
                    if(p<=a[i])
                    {
                    if(a[i]>=min1)
                    {
                                 all++;
                    }
                    if(a[i]==min1||a[i]==min1+1)
                    {
                                              sur++;
                    }
                    }
    }
    cout<<"Case #"<<(x-t)<<": "<<(all-sur)+(sur>s?s:sur)<<"\n";
}
}
   
