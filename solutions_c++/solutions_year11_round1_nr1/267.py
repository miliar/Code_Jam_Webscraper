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

bool exact(int i, int p)
{
    return fabs(round((double)i * ((double) p / 100.0)) - ((double)i * ((double) p / 100.0))) < 1e-9;
}

int main()
{
    int t;
    scanf("%d", &t);
    FOR(testcase, 0, t){
        ll n;
        int pd, pg;
        scanf("%lld %d %d", &n, &pd, &pg);

        bool possible = true;

        if(pd == 100 && pg == 0) possible = false;
        if(pd == 0 && pg == 100) possible = false;
        
        if(pg == 100 && pd < 100) possible = false;
        if(pg == 0 && pd > 0) possible = false;

        if(n <= 10000LL){
            int nn = (int)n;
            bool can = false;
            FOR(i, 1, nn + 1) if(exact(i, pd)) can = true;
            if(!can) possible = false;
        }

        printf("Case #%d: ", testcase + 1);
        if(possible) printf("Possible\n");
        else printf("Broken\n");
    }
    return 0;
}

