#include <iostream>
#include <string>
#include <cmath>
#include <climits>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <ctime>
#include <iomanip>
#include <map>
using namespace std;

long long T,L,t,N,C,p;
long long a[10000010];
long long b[10000010];
int gcd(int a,int b)
{
    int t;
    while(b!=0)
    {
        t = b;
        b = a %b;
        a = t;
    }
    return a;
}
int main(){
    freopen("data.in","r",stdin);
    freopen("out.txt","w",stdout);
    long long i,j,k;
    scanf("%I64d",&T);
    for(k=1;k<=T;k++)
    {
        cout<<"Case #"<<k<<": ";
        cin>>L>>t>>N>>C;
        for(i=0;i<C;++i)
        {
            cin>>a[i];
            a[i]<<=1;
        }
        long long sum=0,tot;
        for(i=0,j=0;sum<t&&j<N;i=(i+1)%C,++j)
            sum+=a[i];
        if(sum>=t)
        {
            tot=sum;
            p=0;
            b[p++]=sum-t;
            for(;j<N;i=(i+1)%C,++j)
            {
                tot+=a[i];
                b[p++]=a[i];
            }
            if(p<=L)
            {
                cout<<tot/2<<endl;
            }
            else
            {
                sort(b,b+p);
                sum=0;
                for(i=p-1;i>=p-L;--i)
                    sum+=b[i];
                cout<<sum/2+tot-sum<<endl;
            }
        }
        else
        {
            cout<<sum<<endl;
        }
    }
    return 0;
}
