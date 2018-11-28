#include <string>
#include <cstring>
#include <vector>
#include <cmath> 
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
 
using namespace std;
 
#define REP(a,n) for(int a=0; a<(n); ++a)
#define FOR(a,b,c) for(int a=(b); a<=(c); ++a)
#define FORD(a,b,c) for(int a=(b); a>=(c); --a)
#define INIT(a, v) __typeof(v) a = (v)
#define FOREACH(a, v) for (INIT(a, (v).begin()); a!=(v).end(); ++a)
 
template<class T>
inline int size(const T&t){return t.size();}
 
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef long long LL;

#define INF 1000000000
#define PB push_back
#define MP make_pair
 
//////////////////////////////////////////

inline bool czy(int A, int B) {
    if (A<B)
        swap(A, B);
    if (A==B)
        return false;
    if (A%B && czy(B, A%B))
        return A/B>1;
    return true;
}

int A1, A2, B1, B2;

int pocz[1000001];
int kon [1000001];

int main() {
    pocz[1] = kon[1] = 1;
    pocz[2] = 2; kon[2] = 3;
    FOR(x, 3, 1000000) {
        pocz[x] = pocz[x-1];
        while (czy(x, pocz[x]))
            ++pocz[x];
        kon[x] = kon[x-1];
        while (!czy(x, kon[x]+1))
            ++kon[x];
    }
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        scanf("%d%d%d%d", &A1, &A2, &B1, &B2);
        LL suma = 0;
        
        FOR(A, A1, A2)
            if (pocz[A]>B2 || kon[A]<B1)
                suma += B2-B1+1;
            else {
                int p = max(B1, pocz[A]);
                int k = min(B2, kon[A]);
                suma += B2-B1+1-(k-p+1);
            }
        printf("Case #%d: %Ld\n", tt+1, suma);
    }
}


