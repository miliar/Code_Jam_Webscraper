#include <cstdio>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <numeric>
#include <iostream>
#include <algorithm>

using namespace std;

#define REP(i,n) for(int i=0;i<(n);i++)
#define all(x) x.begin(),x.end()
#define sz(x) int((x).size())
#define pb  push_back
#define mp make_pair

//Extras
#define SI(x) scanf("%d", &x)
#define SLL(x) scanf("%lld", &x)
#define SD(x) scanf("%lf", &x)

typedef long long LL;

#define gt(x) ((x)>=0)

void processor()
{
    int n, surprise, L, tmp;
    /*
    n - no. of scores
    surprise - no. of surprising triplets
    L - min. score
    */
    vector <int> V;
    scanf("%d%d%d", &n, &surprise, &L);
    REP(i,n)
        scanf("%d", &tmp),
        V.pb(tmp);
    sort(V.rbegin(), V.rend());
    int ans = 0;
    REP(i,n)
        if(V[i] - L >= 2 * L - 2 && gt(V[i] - L))
            ans++;
        else
        {
            if(surprise == 0)
                break;
            if(V[i] - L <= 2 * L - 3 && V[i] - L >= 2 * L - 4 && gt(V[i]-L))
                ans++,
                surprise--;
        }
    printf("%d\n", ans);
}

int main()
{
    int t;
    SI(t);
    REP(tcases,t)
    {
        printf("Case #%d: ", tcases+1);
        processor();
    }
}
