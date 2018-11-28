#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
    int _t,t;
    long long l,p,c;
    cin>>_t;
    for (t=1;t<=_t;t++)
    {
        cin>>l>>p>>c;
        int res=0;
        long long ima = c;
        while (ima * l < p)
        {
            res ++;
            ima = ima * ima;
        }
        cout<<"Case #"<<t<<": "<<res<<endl;
    }
    return 0;
}
