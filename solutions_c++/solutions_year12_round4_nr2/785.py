#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <memory>
#include <vector>
#include <string>
#include <bitset>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <climits>
#include <cstring>
#include <cstdio>
#include <cmath>
#define sz(a) ((int)(a).size())
#define foreach(i, v) for(__typeof((v).begin()) i=(v).begin(); i!=(v).end(); i++)
using namespace std;
typedef long long llong;
typedef pair<int, int> Item;

const int Maxn = 1000+10;
const int INF = 0x7f7f7f7f;
const double eps = 1e-10;
const double pi = acos(-1.0);
inline int realcmp(double a, double b){ return (a>b+eps) ? 1 : ((a+eps<b)?-1:0); }

int n;
int a[Maxn];
double x[Maxn], y[Maxn], r[Maxn], w, h;

bool check()
{
    double bx = 0, by = 0, my = r[a[0]];

    x[a[0]] = y[a[0]] = 0;
    for(int i = 1; i < n; i++)
    {
        if(bx + r[a[i]] + r[a[i - 1]] > w + eps)
        {
            by = my;
            bx = 0;
            x[a[i]] = 0;
            y[a[i]] = my + r[a[i]];
            my = max(my, y[a[i]] + r[a[i]]);
        }
        else
        {
            bx = x[a[i]] =  bx + r[a[i]] + r[a[i - 1]];
            if(by > eps) y[a[i]] = by + r[a[i]];
            else y[a[i]] = 0;
            my = max(my, y[a[i]] + r[a[i]]);
        }
        if(y[a[i]] > h)
            return false;
    }
    return true;
}

int main()
{
    int cas;
    ios::sync_with_stdio(0);
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);

    cin>>cas;
    for(int c=1; c<=cas; c++)
    {
        cin>>n>>w>>h;
        for(int i=0; i<n; i++)
            cin>>r[i];

        for(int i=0; i<n; i++)
            a[i] = i;
        printf("Case #%d: ", c);
        do
        {
            if( check() )
            {
                for(int i=0; i<n; i++)
                    printf("%.1lf %.1lf ", x[i], y[i]);
                printf("\n");
                break;
            }
        } while( next_permutation(a, a+n));
    }

    return 0;
}
