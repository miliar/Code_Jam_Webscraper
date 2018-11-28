#include<iostream>
#include<vector>
#include<string>
using namespace std;
long long x[100000];
int y[100000];
int main()
{ int T;
  cin>>T;
  for(int k=0;k<T;k++)
  { long long n,A,B,C,D,x0,y0,M;
    cin>>n>>A>>B>>C>>D>>x0>>y0>>M;
    int cur=0;
    x[cur]=x0;
    y[cur]=y0;
    cur++;
    for(int j=0;j<n-1;j++)
    { x0=(A*x0+B)%M;
      x[cur]=x0;
      y0=(C*y0+D)%M;
      y[cur]=y0;
      cur++;
    }
    int res=0;  
    for(int i=0;i<n;i++)
    for(int j=i+1;j<n;j++)
    for(int m=j+1;m<n;m++)
    if((x[i]+x[j]+x[m])%3==0&&(y[i]+y[j]+y[m])%3==0)
    res++;
    cout<<"Case #"<<k+1<<": "<<res<<"\n";
  }
}
