#include<iostream>
using namespace std;
int N,today,all;
int gcd(int a,int b)
{
    if (a>b) return gcd(b,a); else
    if (a==0) return b; else return gcd(b%a,a);
    
}
string Solve()
{
    int a,b;
    int k=gcd(today,100);
    if (today==0) k=0; else
    {
        a=100/k;
    }
    if (today==0 && all==100) return "Broken"; else
    if (today==0) return "Possible";
    if (a>N) return "Broken";
    
    if (all==0 && today>0) return "Broken"; else
    if (all==100 && today<100) return "Broken"; else
    return "Possible";    
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    
    int t;
    long long tmp;
    scanf("%d",&t);
    for (int i=1;i<=t;++i)
    {
        cin>>tmp>>today>>all;
        if (tmp>100) N=100; else N=tmp;
        cout<<"Case #"<<i<<": "<<Solve()<<endl;
    }
    return 0;
}
