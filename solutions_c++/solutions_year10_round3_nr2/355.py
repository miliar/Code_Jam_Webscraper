#include <iostream>
#include <cmath>

using namespace std;

int logsufit(long long a, long long b)
{
    int wynik=0;
    long long liczba=1;
    while (liczba<b)
    {
        liczba*=a;
        ++wynik;
    }
    return wynik;
}

int main()
{
    ios_base::sync_with_stdio(0);
    
    int T;
    cin>>T;
    for (int test=1; test<=T; ++test)
    {
        int L,P,C;
        cin>>L>>P>>C;
        int wynik=logsufit(2,logsufit(C,int(ceil(double(P)/L)+0.01)));
        cout<<"Case #"<<test<<": "<<wynik<<endl;
    }
    return 0;
}
