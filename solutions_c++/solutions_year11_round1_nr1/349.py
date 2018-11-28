#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
#include <sstream>
#include <string>
#include <stdio.h>
using namespace std;

__int64 N,D,G;

__int64 gcd(__int64 a,__int64 b)
{
    if(a%b==0) return b;
    return gcd(b,a%b);
}
void test()
{
    cin>>N>>D>>G;

    if(G==0)
    {
        if(D==0)
        {
            cout<<"Possible";
            return;
        }
        else
        {
            cout<<"Broken";
            return;
        }
    }
    if(D==0)
    {
        if(G<100&&(100/gcd(100,G))<=N)
        {
            cout<<"Possible";
            return;
        }
        else
        {
            cout<<"Broken";
            return;
        }
    }
    if(G==100)
    {
        if(D==100)
        {
            cout<<"Possible";
            return;
        }
        else
        {
            cout<<"Broken";
            return;
        }
    }
    __int64 d=100/(gcd(100,D));
    __int64 g=100/(gcd(100,G));

    if(d<=N)
    {
                    cout<<"Possible";
                    return;
    }
    cout<<"Broken";

}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int i,T;
    cin>>T;
    for(i=0;i<T;i++)
    {
      cout<<"Case #"<<i+1<<": ";
      test();
      cout<<endl;
    }
    return 0;
}
