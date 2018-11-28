#include<iostream>
#include<cstdio>
#include<fstream>

inline int dig(int x)
{
    if(x<10) return 1;
    else if (x<100) return 2;
    else if (x<1000) return 3;
}
int p10[]={1,10,100,1000};
using namespace std;
int main()
{
    int a,b,c,d,t,i,j,k,l,ans,m,n,o,p,x,y,z,q,w,e,r;
    ifstream fin("C-small.in");
    ofstream fout("C-small.out");
    fin>>t;
    for(i=1;i<=t;i++)
    {
        fin>>a>>b;
        if(b==1000)b--;
        ans=0;
        for(l=a;l<=b;l++)
        {
            d=dig(l);
            if(d==1)continue;
            else if (d==2)
            {
                x=((l%10)*10+(l/10));
                if(l<x)
                if(a<=x&&x<=b)
                ans++;
            }
            else if (d==3)
            {
                x=((l/10)%10)*p10[2]+(l%10)*10+l/p10[2];
                y=(l%10)*p10[2]+(l/100)*10+(l/10)%10;
                if(l<x)
                if(a<=x&&x<=b)
                ans++;
                if(l<y)
                if(a<=y&&y<=b)
                ans++;
            }
        }
        fout<<"Case #"<<i<<": "<<ans<<"\n";
    }
    cout<<t;
    return 0;
}
