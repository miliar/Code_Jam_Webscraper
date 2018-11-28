#include <iostream>

using namespace std;

int main()
{
    int t, c;
    freopen("A-large.in", "r" ,stdin);
    freopen("A-large.out", "w" ,stdout);
    cin>>t;
    for(c=1;c<=t;c++)
    {
        long long n, k;
        cin>>n>>k;
        long long div=1<<n;
        cout<<"Case #"<<c<<": ";
        if(!((k+1)%div)) cout<<"ON"<<endl;
        else cout<<"OFF"<<endl;
    }
    return 0;
}
