#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<set>
#include<queue>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<functional>
const int INF=(1<<31)-1;
const double EPS=1e-8;
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int ca=1,t,n,k;
    cin>>t;
    //cout<<(1<<4)<<endl;
    //cout<<(1>>4)<<endl;
    while(t--)
    {
      scanf("%d%d",&n,&k);
      int temp=(1<<n);
      k=k%temp; 
      cout<<"Case #"<<ca++<<": "; 
      if(k+1==(1<<n))cout<<"ON"<<endl;      
      else cout<<"OFF"<<endl;             
    }
    //system("pause");
    return 0;
}
