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

#define FOR(A, B) for(int A = 0; A < (int)B; A++)
#define SZ(A) (int)(A).size()
#define vs vector<string>
#define vi vector<int>
#define ll long long
#define ERRO 1e-12
#define DEQ(X,Y) ( fabs((X) - (Y)) < ERRO)

ll x[900], y[900];

bool cmp(int a, int b)
{
    return a > b;
}

int main()
{
    int t, n;
    scanf("%d", &t);
    FOR(caso, t){
        scanf("%d", &n);

        FOR(i, n){
            int xx;
            scanf("%d", &xx);
            x[i] = (ll)xx;
        }
        
        FOR(i, n){
            int yy;
            scanf("%d", &yy);
            y[i] = (ll)yy;
        }
        sort(x, x + n);
        sort(y, y + n, cmp);

        ll resp = 0;
        FOR(i, n)
            resp += x[i]*y[i];
        printf("Case #%d: %lld\n", caso + 1, resp);
    }
    return 0;
}

