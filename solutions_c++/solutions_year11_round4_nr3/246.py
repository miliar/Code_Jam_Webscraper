#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<deque>
#include<set>
using namespace std;
#define ll long long
#define VI vector<ll>
#define VS vector<string>
#define PI pair<int,int>
#define MP make_pair
#define PB push_back

int main() {

int T; cin>>T;


VI primes;

for (int i=2;i<1000001;i++) {
    bool ok=true;
    for (int j=2;j*j<=i;j++) {
        if (i%j==0) { ok=false; break;}
    }    
    if (ok) primes.PB(i);
}


for (int t=0;t<T;t++) {
    ll n;
    cin>>n;
    int ret=1;
    
/*    VI a = VI(n+1,0);
    for (int i=n;i>=1;i--) if (a[i]==0) {
        ret--;
        for (int j=1;j<=i;j++) if (i%j==0) a[j]=1;    
    }*/
    for (int i=0;i<primes.size();i++) if (primes[i]<=n) {
        ll pom=primes[i];
        while (pom<=n) { ret++; pom*=primes[i];}    
    }
    
    for (int i=0;i<primes.size();i++) if (primes[i]<=n) ret--;
    if (n==1) ret=0;
    
    cout<<"Case #"<<t+1<<": "<<ret<<endl;
}
    
}
