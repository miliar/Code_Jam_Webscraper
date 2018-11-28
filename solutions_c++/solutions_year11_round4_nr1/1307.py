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
#define vi vector<int>
#define vd vector<double>
#define pii pair<int,int>
#define pdd pair<double,double>
#define ll long long
#define INF (1<<30)
using namespace std;
vector<pair<double, double> > A;
void solve_case(int case_id)
{
    printf("Case #%d: ", case_id);
    double X, S, R, N;
    double t;
    int i, j;
    cin >> X >> S >> R >> t >> N;
    double p, q, r, rem = X;
    double diff = R - S;
    A.clear();
    for(i = 0; i < N; ++i)
    {
        cin >> p >> q >> r;
        A.pb(mp(r + S, q- p));
        rem -= q - p;
    }
    A.pb(mp(S, rem));
    sort(A.begin(), A.end());
    double ans = 0.0, needed, dist;
    for(i = 0; i < A.size(); ++i)
    {
        needed = A[i].y;
        dist = t * (A[i].x + diff);
        if(needed <= dist)
        {
            ans += needed / (A[i].x + diff);
            t -= needed / (A[i].x + diff);
        }
        else
        {
            t = 0;
            ans += dist / (A[i].x + diff);
            ans += (needed - dist) / A[i].x;
        }
    }
    printf("%.8lf\n", ans);
}

int main()
{
    int i, t;
    scanf("%d", &t);
    for(i = 1; i <= t; ++i) solve_case(i);
    return 0;
}
