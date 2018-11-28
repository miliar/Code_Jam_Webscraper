#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main()
{   int _t,t,n,k;
    cin>>_t;
    for (t=1;t<=_t;t++)
    {
        cout<<"Case #"<<t<<": ";
        cin>>n>>k;
        if ((k+1)%(1<<n)==0) cout<<"ON"; else cout<<"OFF";
        cout<<endl;
    }
    return 0;
}
