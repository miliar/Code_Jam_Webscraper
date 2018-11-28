#include <iostream>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

#define FOR(i,a,b) for(int i = a ; i < b ; i++)

#define FORI(i,b,a) for(int i = b - 1 ; i >= a ; i--)

#define LL long long
#define ULL unsigned long long
#define UI unsigned int

#define VI vector<int>
#define VS vector<string>

#define pb push_back

int gcd(int a,int b) {
    if(a%b == 0) return b;
    else return gcd(b,a%b);
}

int N,L,H;

bool isMatched(int n,VI v) {
    FOR(i,0,v.size()) {
        if(v[i] % n != 0 && n % v[i] != 0) return false;
    }
    return true;
}    

int main() {
    int tc,T;
    cin>>tc;
    FOR(T,1,tc+1) {
        printf("Case #%d: ",T);
        cin>>N>>L>>H;
        bool b = false;
        VI v(N);
        FOR(i,0,N) cin>>v[i];
        sort(v.begin(),v.end());
        FOR(i,L,H+1) {
            if(isMatched(i,v)) {
                cout << i << endl;
                b = true;
                break;
            }
        }             
        if(!b) cout << "NO" << endl;
    }
    return (0);
}
