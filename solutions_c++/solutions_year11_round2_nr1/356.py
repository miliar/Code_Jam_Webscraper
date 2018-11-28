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

const int maxn = 128;

void solve_case(int case_id)
{
    printf("Case #%d:\n", case_id);
    int i, j, k, N;
    char A[maxn][maxn];
    double wp[maxn], owp[maxn], oowp[maxn];
    cin >> N;
    for(i = 0; i < N; ++i)
        for(j = 0; j < N; ++j) cin >> A[i][j];

    for(i = 0; i < N; ++i)
    {
        int won = 0, played = 0;
        for(j = 0; j < N; ++j)
        {
            if(A[i][j] != '.') ++played;
            if(A[i][j] == '1') ++won;
        }
        wp[i] = won / (double)played;
    } // calc WP

    for(i = 0; i < N; ++i)
    {
        double totwp = 0.0;
        int ops = 0;
        for(j = 0; j < N; ++j)
        {
            if(i == j) continue;
            if(A[i][j] == '.') continue; // samo oponentite
            ++ops;
            int won = 0, played = 0;
            for(k = 0; k < N; ++k)
            {
                if(k == i) continue; // bez igrite sresthu nas
                if(A[j][k] != '.') ++played;
                if(A[j][k] == '1') ++won;
            }
            totwp += won / (double)played;
        }
        owp[i] = totwp / (double) ops;
    }

    for(i = 0; i < N; ++i)
    {
        double tot = 0; // average owp of opponents
        int ops = 0;
        for(j = 0; j < N; ++j)
        {
            if(A[i][j] == '.') continue;
            ++ops;
            tot += owp[j];
        }
        oowp[i] = tot / (double) ops;
    }
    for(i = 0; i < N; ++i)
    {
        double ans = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
        printf("%.10lf\n", ans);
    }
}

int main()
{
    int i, t;
    scanf("%d", &t);
    for(i = 1; i <= t; ++i) solve_case(i);
    return 0;
}
