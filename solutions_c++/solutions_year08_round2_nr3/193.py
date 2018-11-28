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

struct position {
    uint p;
    uint card;
};

uint idx[1000];
uint positions[10000000];

int main() {
    uint tests;

    
    scanf("%d", &tests);
    for (uint t = 1; t <= tests; t++) {
        uint n;
        uint K;
        scanf("%d", &K);
        scanf("%d", &n);
        
        FOR(i, 1, n) {
            scanf("%d", &idx[i]);
        }
        
        queue<int> q;
        FOR(i, 1, K) {
            q.push(i);
        }
        
        FOR(i, 1, K) {
            uint cpos;
            
            REP(j, i-1 % q.size()) {
                q.push(q.front());
                q.pop();
            }
            
            positions[q.front()] = i;
            q.pop();
        }
        
        printf("Case #%d: ", t);
        FOR(i, 1, n) {
            printf("%d ", positions[idx[i]]);
        }
        printf("\n");
    }

    return 0;
}
