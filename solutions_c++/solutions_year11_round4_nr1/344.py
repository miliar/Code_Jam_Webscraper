#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <set>
#include <map>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<pii> vp;
typedef vector<vi> vvi;

const int N = 100010;
const int M = 55;
const int K = 200010;
const int LIT = 2500;
const int INF = 1 << 30;
const int ABS(int x) {while(x < 0) x = -x; return x;}

#define mp make_pair
#define pb push_back
#define fst first
#define snd second

struct node {int lt, rt, v;}dta[N];
int x, s, r, t, n, num;

bool cmp(node a, node b) {return a.v < b.v;}

void init()
{
    cin>>x>>s>>r>>t>>n;
    num = 0;
    for(int i = 0; i < n; i++)
    {
        cin>>dta[i].lt>>dta[i].rt>>dta[i].v;
        num += dta[i].rt - dta[i].lt;
    }
    if(num != x)
    {
        dta[n].lt = 0, dta[n].rt = x - num, dta[n].v = 0;
        n++;
    }
    sort(dta, dta + n, cmp);
}

void solve(int tcase)
{
    double res = 0.0, bnd = t;
    for(int i = 0; i < n; i++)
    {
        if(bnd > 0)
        {
            double tmp = (dta[i].rt - dta[i].lt) / (r + dta[i].v * 1.0);
            if(tmp < bnd)
            {
                res += tmp;
				bnd -= tmp;
            }
            else
            {
                res += bnd;
                tmp = (dta[i].rt - dta[i].lt) - (r + dta[i].v*1.0) * bnd;
				res += tmp / (s + dta[i].v);
				bnd = 0;
            }
        }
        else
        {
            res += (dta[i].rt - dta[i].lt) / (s + dta[i].v * 1.0);
        }
    }
    printf("Case #%d: %.10lf\n", tcase, res);
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("ASout.txt", "w", stdout);
    int T;
    cin>>T;
    
    for(int i = 1; i <= T; i++)
    {
        init();
        solve(i);
    }
    //while(1);
}
