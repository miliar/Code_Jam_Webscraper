#include<string>
#include<iostream>
#include<sstream>
#include<assert.h>
#include<cstdio>
#include<map>
#include<algorithm>
#include<bitset>
#include<cmath>
#include<queue>
#include<functional>


using namespace std;

long long X[800];
long long Y[800];
int n;

long long solve()
{
    sort(X,X+n);
    sort(Y,Y+n, greater<long long>() );
    long long r=0;
    for (int i=0;i<n;i++) r+=X[i]*Y[i];
    return r;
}

//=========================================================
// I/O:
//
int main()
{
    int T; cin>>T;
    for (int i=1;i<=T;i++)
    {
        cin>>n;
        for (int j=0;j<n;j++) cin>>X[j];  
        for (int j=0;j<n;j++) cin>>Y[j];
        long long r=solve();
        cout<<"Case #"<<i<<": "<<r<<endl;
    }
    return 0;
}
