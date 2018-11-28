#include <iostream>

using namespace std;
long long x;
long long y;
long long l,p;
long long c;
long long pow(long long base,long long index)
{
    long long ret=1;
    while(index)
    {
        if(index&1)
        {
            ret*=base;
        }
        base*=base;
        index>>=1;
    }
    return ret;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("tout.txt","w",stdout);
    int t;
    cin>>t;
    int cas=1;
    while(t--)
    {
        cin>>l>>p>>c;
        long long temp=1;
        for(x=0;;x++)
        {
            if(l*pow(c,x)>=p)
            {
                break;
            }
        }
        for(y=0;;y++)
        {
            if(pow(2,y)>=x)
                break;
        }
        //printf("Case #%d: %d\n",cas++,ans);
        cout<<"Case #"<<cas++<<": "<<y<<endl;
    }
    return 0;
}
