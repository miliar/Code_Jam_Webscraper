#include <iostream>
#include <fstream>
#include <algorithm>
#include <climits>
#include <cstdio>
#include <cmath>
#include <cstdlib>




using namespace std;


typedef long long LL;

LL N,D,G;

LL gcd(LL a,LL b)
{
    LL tmp;
    while(b)
    {
        tmp=a%b;
        a=b;
        b=tmp;
    }

    return a;
}



int main()
{
    freopen("A-large (1).in","r",stdin);
    freopen("output.out","w",stdout);


    LL T;
    cin>>T;

    for(LL loop=1;loop<=T;loop++)
    {
        cin>>N>>D>>G;
        LL d,d1;

        if(G==0)
        {
            if(D==0)
            {
                cout<<"Case #"<<loop<<": Possible"<<endl;
            }
            else
            {
                cout<<"Case #"<<loop<<": Broken"<<endl;
            }
            continue;
        }
        if(G==100)
        {
            if(D==100)
            {
                cout<<"Case #"<<loop<<": Possible"<<endl;
            }
            else
            {
                cout<<"Case #"<<loop<<": Broken"<<endl;
            }
            continue;
        }

        LL tmp;
        d=d1=100;
        tmp=gcd(D,d);
        D/=tmp;
        d/=tmp;
        if(d>N)
        {
            cout<<"Case #"<<loop<<": Broken"<<endl;
            continue;
        }
        cout<<"Case #"<<loop<<": Possible"<<endl;



    }












    return 0;
}
