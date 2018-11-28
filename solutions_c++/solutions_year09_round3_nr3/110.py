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
#define vi vector<int>
#define pb push_back
#define ll long long
#define ERRO 1e-12
#define DEQ(X,Y) ( fabs((X) - (Y)) < ERRO)

#define INF 1000000000

int p, q;
vector<int> release;
map<pair<int, int>, int > dp;

int solve(int left, int right)
{
    if(left >= right) return 0;

    if(dp.count(make_pair(left, right)))
        return dp[make_pair(left, right)];

    int resp = INF;
    FOR(i, 0, SZ(release)) if(release[i] >= left && release[i] <= right) {
        resp = min(resp, solve(left, release[i] - 1) + solve(release[i] + 1, right) + (right - left));
    }

    if(resp == INF) resp = 0;
    dp[make_pair(left, right)] = resp;

    return resp;
}

int main()
{
    int t;
    scanf("%d", &t);
    FOR(test, 0, t){
        scanf("%d %d", &p, &q);
        release.clear();
        FOR(i, 0, q){
            int tmp;
            scanf("%d", &tmp);
            release.push_back(tmp);
        }

        dp.clear();
        printf("Case #%d: %d\n", test + 1, solve(1, p));
    }
    return 0;
}

