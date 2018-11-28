#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#define N 11111111
using namespace std;
int p[11],x,x1,x2,s,kol,c[N],d[N],a,b,k,t;
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    p[1]=10;for (int i=2;i<=8;i++)p[i]=p[i-1]*10;
    for (int i=12;i<2000000;i++){
        x=i;s=0;
        while(x>0){x/=10;s++;}
        for (int j=1;j<s;j++){
            x1=i/p[j];x2=i%p[j];
            x2*=p[s-j];
            x=x1+x2;
            if (x>i && (i!=c[kol] || x!=d[kol])){kol++;c[kol]=i;d[kol]=x;}
            }
        }
    cin>>t;
    for (int j=1;j<=t;j++){
        cin>>a>>b;k=0;
        for (int i=1;c[i]<=b;i++)
          if (c[i]>=a && d[i]<=b){k++;}
        cout<<"Case #"<<j<<": "<<k<<endl;}
    return 0;
}
        
            
        
