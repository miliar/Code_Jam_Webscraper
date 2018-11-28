#include<iostream>
#include<stdio.h>
#include<cmath>

using namespace std;

long long n;
int t,tt,pd,pg,tmpd,tmpg,facd,facg,k;
FILE *in,*out;

int gcd(int a,int b)
{
    if (a%b==0 || a==b) return b;
    return gcd(b,a % b);
}

int main()
{
    in=freopen("A-large.in","r",stdin);
    out=freopen("A-large.out","w",stdout);
    cin>>t;
    tt=t;
    while (tt)
    {
        cin>>n>>pd>>pg;
        if ((pg==100 && pd<100 )||(pg==0 && pd>0) )
            cout<<"Case #"<<t-tt+1<<": Broken"<<endl;
        else if ((pg==100 && pd==100)||(pg==0 && pd==0))
            cout<<"Case #"<<t-tt+1<<": Possible"<<endl;
        else
        {
            tmpd=gcd(100,pd);
            tmpg=gcd(100,pg);
            pd/=tmpd;
            pg/=tmpg;
            facd=100/tmpd;
            facg=100/tmpg;
            if (n>=facd)
                cout<<"Case #"<<t-tt+1<<": Possible"<<endl;
            else
                cout<<"Case #"<<t-tt+1<<": Broken"<<endl;
        }
        tt--;
    }
    return 0;
}
