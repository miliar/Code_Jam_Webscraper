#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

#define FOR(A, I, B) for(int A = (int)I; A < (int)B; A++)
#define SZ(A) (int)(A).size()
#define vs vector<string>
#define vi vector<int>
#define pb push_back
#define pii pair<int, int>
#define ll long long
#define ERRO 1e-12
#define DEQ(X,Y) ( fabs((X) - (Y)) < ERRO)

int n;
ll times[5];

ll GCD(ll a, ll b)
{   
    if(b == 0LL)
        return a;

    return GCD(b, a%b);
}

ll solve()
{
    ll gcd = -1LL;

    FOR(i, 0, n)
        FOR(j, i + 1, n){
            ll diff = abs(times[i] - times[j]);
            if(gcd == -1LL) gcd = diff;
            else gcd = GCD(gcd, diff);
        }

    if(times[0]%gcd == 0LL) return 0LL;

    return gcd - (times[0]%gcd);
}

int main()
{
    int cases;
    scanf("%d", &cases);

    FOR(testcase, 1, cases + 1){
    
        int nn;
        scanf("%d", &nn);

        int t;
        n = 0;
        FOR(i, 0, nn){
            scanf("%d", &t);
            bool e = true;
            FOR(j, 0, n) 
                if(times[j] == (ll)t){e = false; break;} 
            if(e)
                times[n++] = (ll)t;
        }

        printf("Case #%d: %lld\n", testcase, solve());
    }
    return 0;
}

