#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>
#include <map>
#include <queue>
#include <stack>
#include <cstring>
#include <cstdlib>
#include <list>
#include <set>
#include <ctime>
#include <list>
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define vi vector<ll>
#define vd vector<double>
#define pii pair<long long,long long>
#define pdd pair<double,double>
#define ll long long
#define INF (1<<30)
using namespace std;

pii V[10007];
ll N, D;

void solve_case(int case_id)
{
    printf("Case #%d: ", case_id);
    ll i, k, ind = 0, span;
    cin >> N;
    for(i = 0; i < N; ++i) cin >> V[i].x >> V[i].y;
    cin >> D;
    if(V[0].x > V[0].y)
    {
        printf("NO\n");
        return;
    }
    // ind - current vine we're holding
    if(2 * V[0].x >= D)
    {
         printf("YES\n");
         return;
    }
    span = V[0].x;
    ll crspan;
    while(ind < N)
    {
        //cout << crswing << ' ' << ind << '\n';
        ll best = -1, j = -1;
        for(i = ind + 1; i < N; ++i)
        {
            if(V[i].x > V[ind].x + span) break;
            ll maxspan = min(V[i].y, V[i].x - V[ind].x);
            if(V[i].x + maxspan >= D)
            {
                printf("YES\n");
                return;
            }
            for(k = i + 1; k < N; ++k) if(V[i].x + maxspan < V[k].x) break;
            if(k == i + 1) continue;
            if(k - 1 > best)
            {
                best = k - 1;
                j = i;
                crspan = maxspan;
            }
        }
        if(j == -1) break;
        ind = j;
        span = crspan;
    }
    printf("NO\n");
}

int main()
{
    int i, t;
    scanf("%d", &t);
    for(i = 1; i <= t; ++i) solve_case(i);
    return 0;
}
