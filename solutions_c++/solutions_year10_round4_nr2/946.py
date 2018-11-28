#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
using namespace std;

const int N = 3000;
const int M = 1000010;

int num[2510][2510];
int edgecnt,p[M];
int n, number;

struct Line
{
    int a, b, next, cnt;
    Line(){}
    Line(int a,int b,int next):a(a),b(b),next(next){}
}Lines[M];
void addedge(int a,int b) {Lines[edgecnt] = Line(a,b,p[a]); p[a] = edgecnt++;}

void init()
{
    scanf("%d", &n);
    number = 1;
    edgecnt = 0;
    memset(p, -1, sizeof(p));
    int k = 0;
    
    for(int i = n; i >= 0; i--)
    {
        for(int j = 0; j < (1<<i); j++)
        {
            scanf("%d",&num[i][j]);
        }
    }
}

int ans;
int dfs(int t)
{
    int res = 1<<29;
    bool f = 0;
    for(int i = p[t]; i != -1; i = Lines[i].next)
    {
        f = 1;
        int t1 = dfs(Lines[i].b);
        res = min(res, t1);
    }
    if(f)
    {
        res--;
        if(res < 0) ans++;
    }
    else
    {
        res = Lines[t].cnt;
    }
    return res;
}

void solve(int tcase)
{
    for(int i = 0; i < n+1; i++)
    {
        for(int j = 0; j < (1<<i); j++)
        {
            if(i == n)
            {
                Lines[number].cnt = num[i][j];
            }
            else
            {
                addedge(number, number*2);
                addedge(number, number*2+1);
                Lines[number].cnt = 0;
            }
            number++;
        }
    }
    ans = 0;
    dfs(1);
    printf("Case #%d: %d\n", tcase, ans);
}

int main()
{
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int T;
    cin>>T;
    for(int i = 1; i <= T; i++)
    {
        init();
        solve(i);
    }
}
