// GCJ '08 
// Question B
// Solution by sql_lall
#include <map>
#include <cmath>
#include <queue>
#include <deque>
#include <string>
#include <vector>
#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

int nCases;

long long axbmodc(long long a,long long b,long long c){ return a ? (axbmodc(c % a, (a - b % a) % a, a) * c + b) / a : 0; }
long long gcd(long long a,long long b){ return b ? gcd(b, a % b) : a; }

void solve(){
    long long N, M, A;
    cin >> N >> M >> A;
    for(long long x1 = max(A/M - 1, 1LL); x1 <= N; x1++)
        for(long long y1 = 0; y1 <= M; y1++){
            //A + ... / M <= x1
            long long init = axbmodc(y1, ((x1 - A % x1) + x1) % x1, x1);
            long long incr = N / gcd(y1, x1);
            for(long long x2 = init; x2 <= N; x2 += incr){
                if((A + x2 * y1) % x1) continue;
                long long y2 = (A + x2 * y1) / x1;
                if(y2 > M) break;
                cout << "0 0 " << x1 << " " << y1 << " " << x2 << " " << y2 << endl;
                return;
            }
        }
    cout << "IMPOSSIBLE" << endl;
    return;            
}

int main(){
    cin >> nCases;
    for(int c = 1; c <= nCases; c++){
        cout << "Case #" << c << ": ";
        solve();
    }
}
