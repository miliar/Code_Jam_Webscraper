#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <utility>
#include <complex>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <string.h>
using namespace std;

#define REP(i,n) for(long long i=0;i<long long(n);++i)
#define FOR(i,a,b) for(long long i=a;i<=b;++i)

int main () {
    long long t; cin >> t;
    for (long long cas=1;cas<=t;++cas) {
        long long n, k;
        cin >> n >> k;
        cout << "Case #" << cas<<": "; 
        bool ok=1;
        for (long long i=0;ok and i<n;++i) {
            if (k%2==0) ok=0;
            k/=2;
        }
        cout <<(ok?"ON":"OFF") << endl;
    }
}
