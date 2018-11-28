#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <set>
using namespace std;

const int N = 1010;
const int M = 33;
const int inf = 1 << 30;

int n;
double x[N], y[N], r[N];

double dist(int a, int b)
{
    return sqrt((x[a]-x[b]) * (x[a]-x[b]) + (y[a]-y[b]) * (y[a]-y[b]));
}

void solve(int ca)
{
    cin>>n;
    double res = 0;

    for(int i= 1; i <= n; i++)
    {
            cin>>x[i]>>y[i]>>r[i];
    }

    if(n == 1)
    {
        res = r[1];
    }
    else if(n == 2)
    {
        if(r[1] > r[2])
            res = r[1];
        else
            res = r[2];
    }
    else
    {
        res = inf;

        for(int i = 1; i <= 3; i++)
        {
            for(int j = 1; j <= 3; j++)
            {
                double mid = dist(i, j);
                double tmp = mid + r[i] + r[j];
                res = min(res, tmp);
            }

        }
    }


    printf("Case #%d: %lf\n", ca, res);
}

int main()
{
    freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int T;
    cin>>T;

    for(int ca = 1; ca <= T; ca++)
    {
        solve(ca);
    }
}
