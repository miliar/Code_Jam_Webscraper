#include<iostream>
using namespace std;

long long d[13];
long long mm[17];
long long hhh(long long h)
{
    long long an=1;
    while(1)
    {
        if(h/10==0)return an;
        h/=10;
        an++;
    }
}
long long bbb(long long x,long long h)
{
    return x/10+d[h-1]*(x%10);
}
bool mmm(long long f)
{
    for(long long i=1;i<=mm[0];i++)
    {
        if(mm[i]==f)return 0;
    }
    return 1;
}
int main()
{
long long t;
cin>>t;
long long a,b;
d[0]=1;
for(long long i=1;i<=7;i++)d[i]=d[i-1]*10;
for(long long i=1;i<=t;i++)
{
    cin>>a>>b;
    long long an=0;
    for(long long i=a;i<=b;i++)
    {
        long long h=hhh(i);
        long long x=i;
        mm[0]=1;
        mm[1]=x;
        for(long long j=1;j<h;j++)
        {
            x=bbb(x,h);
            if(x/d[h-1]!=0&&a<=x&&x<=b&&i<x&&mmm(x))
            {
            mm[++mm[0]]=x;
            an++;
            }
        }
    }
    cout<<"Case #"<<i<<": "<<an<<endl;
}
return 0;
}
