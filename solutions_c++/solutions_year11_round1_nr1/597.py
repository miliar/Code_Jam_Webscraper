#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <set>
using namespace std;

typedef long long ll;

ll gcd(ll a,ll b) {
    if(b == 0) return a;
    return gcd(b, a%b);
}

int main() {
    int pd,pg,t;
    ll n;

    cin>>t;
    for(int i=0; i<t; ++i) {
        cin>>n>>pd>>pg;

        if((pd == 0 && pg > 0) || (pg == 0 && pd > 0)) {
            cout<<"Case #"<<i+1<<": Broken"<<endl;
            continue;
        }

        ll k = gcd(100,pd);
//        cout<<pd<<" "<<k<<endl;
        ll m = 100/k;

        if(m > n || (pg == 100 && pd != 100)) {
            cout<<"Case #"<<i+1<<": Broken"<<endl;
            continue;
        }
        cout<<"Case #"<<i+1<<": Possible"<<endl;
    }
}
