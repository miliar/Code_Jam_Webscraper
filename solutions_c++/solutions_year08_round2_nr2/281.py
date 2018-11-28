#include <cstdio>
#include <vector>
#include <set>

using namespace std;

#define REP(a, b) for(int a=0; a<(b); a++)
#define FOR(a, b, c) for(int a=(b); a<=(c); a++)
#define FORD(a, b, c) for(int a=(b); a>=(c); a--)
#define ABS(a) ((a) < 0 ? -(a) : (a))
#define MP make_pair
#define F first
#define S second

typedef long long ll;

bool found[1001];
bool prime[1001];
vector<int> factors;

void dfs(int v, int a, int b) {
    found[v] = true;
    REP(i, factors.size())
        if (v%factors[i]==0)
            for (int j = (a%factors[i]==0 ? a : a-a%factors[i]+factors[i]); j <= b; j += factors[i])
                if (!found[j])
                    dfs(j, a, b);
}

int main() {
    REP(i, 1001) prime[i] = true;
    prime[0]=prime[1] = false;
    FOR(i, 2, 1000) if(prime[i])
    for (int j = i*2; j<=1000; j+=i) prime[j] = false;

    int z;
    scanf("%d", &z);
    FOR(zz, 1, z) {
        int a, b, p;
        scanf("%d%d%d", &a, &b, &p);
        factors.clear();
        FOR(i, p, b) if(prime[i]) factors.push_back(i);
        FOR(i, a, b) found[i] = false;
        int ret = 0;
        FOR(i, a, b) if (!found[i]) { dfs(i, a, b); ret++; }
        
        printf("Case #%d: %d\n", zz, ret);
    }
    return 0;
}
