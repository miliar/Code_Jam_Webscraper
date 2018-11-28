#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <utility>
using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PII;
typedef long long LL;

#define REP(i, n) for(int i=0; i<n; ++i)
#define ST first
#define ND second
#define PB push_back
#define VAR(v,n) __typeof__(n) v=(n)
#define FE(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define ALL(c) (c).begin(),(c).end()

/*
    * if n < 1,373,653, it is enough to test a = 2 and 3;
    * if n < 9,080,191, it is enough to test a = 31 and 73;
    * if n < 4,759,123,141, it is enough to test a = 2, 7, and 61;
    * if n < 2,152,302,898,747, it is enough to test a = 2, 3, 5, 7, and 11;
    * if n < 3,474,749,660,383, it is enough to test a = 2, 3, 5, 7, 11, and 13;
    * if n < 341,550,071,728,321, it is enough to test a = 2, 3, 5, 7, 11, 13, and 17.
*/

LL TESTS[] = {2, 3, 5, 7, 11, 13, 17, 0};


LL multiply(LL a, LL b, LL mod){
//    return (a * b) % mod;
    if (a == 0 || b == 0) return 0;

    LL r = (multiply(a, b/2ULL, mod) * 2ULL) % mod;

    if ( b % 2ULL ) return (r + a) % mod;
    return r % mod;
}

LL power(LL a, LL d, LL mod){
    if ( d == 0 ) return 1LL;
    LL s = power(a, d/2LL, mod);
    if ( d & 1LL ) {
        return multiply( multiply(a, s, mod), s, mod);
    }
    return multiply(s, s, mod);
}

bool is_prime(LL n){
  //  if (n % 100000 == 0) cout << n << endl;

    if ( n <= 1ULL ) return false;
    if ( n % 2ULL == 0 ) return (n == 2ULL);

    LL s = 0;
    while( ( (n - 1ULL) & (1ULL << s) ) == 0 ) s++;

    //cout << "s: " << s << endl;

    LL d = (n-1ULL) >> s;

    //cout << "d: " << d << endl;

    for(LL* a = TESTS; (*a) && (n > (*a)); ++a){
    //    cout << "swiadek " << *a << endl;
        if (  power(*a, d, n) != 1ULL  ){

            //cout << "test1 pass" << endl;

            bool pass = false;

            REP(r, s) {
                //cout << *a << "^" << (1LL << r) * d << " mod " << n << " = " <<  power(*a, (1LL << r) * d , n ) << endl;
                if ( power(*a, (1ULL << r) * d , n ) == n-1ULL ) {
                    pass = true;
                    break;
                }
                //cout << "pass: " << r << endl;
            }

            //cout << "ten swiadek ok" << endl;
            if (! pass) return false;


        }
    }
    return true;
}

bool prime[ 1400000 ];


long long testcase(){
    long long a; scanf("%lld", &a);
    if ( a == 1 ) return 0;
    
    long long r = 0;
    unsigned long long p = 2;
    //cout << a << endl;
    for( ; p*p <= a; p++ ) {
      //  cout << "spr " << p << endl;
        if ( prime[ p ] ) {
       // cout << p << endl;
        unsigned long long tmp = p*p;
        while( tmp <= a ){
            r ++;
            tmp *= p;
        }
    }
    }
    return r + 1;
}

int main(){
int z; scanf("%d", &z);
REP(i, 1400000) prime[i] = false;
for(int i=2; i<1100000; i++) prime[i] = is_prime(i);
//cout << "policzone" << endl;

REP(i, z){
    printf("Case #%d: %lld\n", i+1, testcase());
}
return 0;
}

