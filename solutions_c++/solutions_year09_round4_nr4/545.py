#include<iostream>
#include<vector>
#include<cmath>
using namespace std;
int x[100],y[100],r[100];
long double minrad(int a,int b,int c)
{ long double res= max(r[a]*1.0,(sqrt((x[b]-x[c])*(x[b]-x[c])+(y[b]-y[c])*(y[b]-y[c]))+r[b]+r[c])*1.0/2);
  return res;
  //cout<<a<<" "<<b<<" "<<c<<" "<<r[a]<<" "<<r[b]<<" "<<r[c]<<" "<<res<<"\n";
}
int main()
{ int T;
  cin>>T;
  for(int t=0;t<T;t++)
  { int N;
    cin>>N;
    for(int i=0;i<N;i++)
    cin>>x[i]>>y[i]>>r[i];
    if(N==1)
    cout<<"Case #"<<t+1<<": "<<r[0]<<"\n";
    else if(N==2)
    cout<<"Case #"<<t+1<<": "<<max(r[0],r[1])<<"\n";
    else
    { long double r1=minrad(0,1,2);
      //cout<<r1<<" ";
      r1=min(r1,minrad(1,0,2));
            //cout<<r1<<" ";
      r1=min(r1,minrad(2,0,1));
            //cout<<r1<<" ";
      cout<<"Case #"<<t+1<<": "<<r1<<"\n";
    }
  }
}
