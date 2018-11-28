#include<iostream>
#include<cstdio>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<utility>
#include<sstream>
#include<cstring>
using namespace std;

typedef long long ll;
typedef unsigned int uint;

#define FOR(I,A,B) for(uint I=(A);I<=(B);I++)
#define REP(I,N) for(uint I=0;I<(N);I++)
#define VAR(V,I) typeof(I) V=(I)
#define FOREACH(I,C) for(VAR(I,(C).begin());I != (C).end(); I++)

#define all(X) (X).begin(),(X).end()
#define pb push_back
#define mp make_pair
#define fi first
#define se second

#define INTPINF  2147483647
#define INTNINF  2147483648
#define UINTINF  4294967295
#define LLPINF   9223372036854775807
#define LLNINF   9223372036854775808
#define ULLINF   18446744073709551615

typedef vector<int> VI;
typedef pair<int,int> PII;
typedef long long ll;
typedef vector<string> VS;

#define X 0
#define Y 1

int main() {
    uint tests;
    ll n, A, B, C, D, x0, y0, M;
    
    ll trees[100000][2];
    
    scanf("%d", &tests);
    for (uint t = 1; t <= tests; t++) {
        scanf("%lld %lld %lld %lld %lld %lld %lld %lld", &n, &A, &B, &C, &D, &x0, &y0, &M);
        REP(i, n) {
            trees[i][X] = x0;
            trees[i][Y] = y0;
            x0 = (A * x0 + B) % M;
            y0 = (C * y0 + D) % M;
        }
        
        uint count = 0;
        FOR(i, 0, n-3) {
            FOR (j, i+1, n-2) {
                FOR (k, j+1, n-1) {
                    if ((trees[i][X] + trees[j][X] + trees[k][X]) % 3 == 0) {
                        if ((trees[i][Y] + trees[j][Y] + trees[k][Y]) % 3 == 0) {
                            count++;
                        }
                    }
                }
            }
        }
        
        printf("Case #%d: %d\n", t, count);
    }

    return 0;
}
