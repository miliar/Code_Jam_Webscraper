#include <cstdlib>
#include <iostream>

using namespace std;

int main()
{
    typedef unsigned long long int mint;
    mint t,k,n;
    cin>>t;
    for(mint ti=1;ti<=t;ti++)
    {
        cin>>n>>k;
        mint mod=1<<n;
        cout<<"Case #"<<ti<<": ";
        if((k+1)%mod==0)
        {
            cout<<"ON"<<endl;
        }
        else
        {
            cout<<"OFF"<<endl;
        }
    }
    return 0;
}
