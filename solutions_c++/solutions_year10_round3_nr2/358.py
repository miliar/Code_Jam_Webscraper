#include <iostream>
#include <cmath>
using namespace std;
const double eps=1e-6;

typedef long long LL;

const int N = 1000;

LL p,l,c;
LL result = 0;

    void inputing()
    {
        cin>>l>>p>>c;
    }

    void work()
    {
        LL r;
        r = 0;
        LL temp = l;
        while (temp*c < p)
        {
            temp *= c;
            r ++;
        }
//        cout<<"r = "<<r<<endl;//debug
        result = 0;
//        if ( 1 == r ) return ;
//        r = 8;
        while ( r>0 )
        {
            r = r/2;
            result ++;
        }
    }

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int i,cas;
    scanf("%d",&cas);
    for ( i=1;i<=cas;i++ )
    {
        inputing();
        work();
//        if ( i<10 )
        cout<<"Case #"<<i<<": "<<result<<endl;
//        printf("Case #1: 2",i,result);
    }

    return 0;
}

