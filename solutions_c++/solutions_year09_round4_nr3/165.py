#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
using namespace std;

const int N = 210;
const int M = 33;

struct Node {int a[M];}Lines[N];

bool operator< (Node x,Node y)
{
    return x.a[0] > y.a[0];
}

int vis[N];
int n,m;
int maps[N][N];
int link[N];

bool check(int x,int y)
{
    for(int i = 0; i < m; i++) if(Lines[x].a[i] <= Lines[y].a[i]) return 0;
    return 1;
}

bool Find(int a)
{
    for(int i = 0; i < n; i++)
    {
        if(!vis[i] && maps[a][i])
        {
            int tmp = link[i];
            link[i] = a;
            vis[i] = 1;
            if(tmp == -1 || Find(tmp)) return 1;
            link[i] = tmp;
        }
    }
    return 0;
}

void solve(int ca)
{
    scanf("%d%d",&n,&m);
        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j < m; j++)
                scanf("%d",&Lines[i].a[j]);
        }
        sort(Lines,Lines+n);
        memset(maps,0,sizeof(maps));
        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j < n; j++)
            {
                if(check(i,j)) maps[i][j] = 1;
            }
        }

        memset(link,-1,sizeof(link));
        int res = 0;

        for(int i = 0; i < n; i++)
        {
            memset(vis,0,sizeof(vis));
            if(Find(i)) res++;
        }

        printf("Case #%d: %d\n",ca, n - res);
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    cin>>T;

    for(int ca = 1; ca <= T; ca++)
    {
        solve(ca);
    }
}
