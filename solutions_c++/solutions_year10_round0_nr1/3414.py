#include<iostream>
using namespace std;
#define forn(i,n) for(int i = 0; i < n;i++)
main()
{
    int t;
    cin>>t;
    forn(kk,t)
    {
        long long n,k;
        cin>>n>>k;
        long long to = 1;
        forn(i,n-1)
            to = to *2+1;
        to++;
        cout<<"Case #"<< kk+1<<": ";

        if (k % to == to-1)
            cout<<"ON"<<endl;
        else
            cout<<"OFF"<<endl;
    }
}
