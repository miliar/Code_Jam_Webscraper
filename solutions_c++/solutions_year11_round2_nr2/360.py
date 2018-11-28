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

const int maxn = (1<<20);
int n, c, d, a[maxn];

void solve_case(int case_id)
{
    printf("Case #%d: ", case_id);
    int i, j, p, v;
    cin >> c >> d;
    n = 0;
    int ind = 0;
    for(i = 0; i < c; ++i)
    {
        cin >> p >> v;
        n += v;
        for(j = 0; j < v; ++j) a[ind++]= p;
    }
    bool good = true;
    for(i = 1; i < n; ++i)
        if(a[i] - a[i - 1] < d) good = false;

    if(good)
    {
        printf("0.0\n");
        return;
    }

    ll lb = 0, rb = 2LL, med;
    for(i = 0; i < 62; ++i) rb *= 2LL;
    for(int cntr = 0; cntr < 500; ++cntr)
    {
        med = (lb + rb) / 2; // med / 2 ни е броя секунди, изминали от началото
        double time = med / 2.0;
        double cr = (ll)a[0] - time, exp;
        bool good = true;
        for(i = 1; i < n; ++i)
        {
            exp = cr + d; // трябва поредния вендор да е поне там
            if((ll)a[i] + time < exp)
            {
                good = false;
                break;
            }
            if((ll)a[i] >= exp) cr = max(exp, (ll)a[i] - time);
            else cr = exp;
        }
        if(!good) lb = med;
        else rb = med;
    }
    double ans = rb / 2.0;
    cout << ans << '\n';
}

int main()
{
    int i, t;
    scanf("%d", &t);
    for(i = 1; i <= t; ++i) solve_case(i);
    return 0;
}

