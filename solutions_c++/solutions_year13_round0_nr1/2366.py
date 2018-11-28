//c++  #pragma comment(linker, "/STACK:1024000000,1024000000")
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <map>
#include <set>
#define rep(i,a,b) for(int i=a;i<=b;i++)
#define INF (1<<29)
#define eps (1e-5)
#define pb push_back
using namespace std;
/*
struct Edge{
    int v,next,w;
}edge[MAXN*3];
int E,list[MAXN];
void init() {memset(list,E=-1,sizeof(list)); }
void add(int u,int v,int w)
{
    edge[++E].v=v; edge[E].w=w; edge[E].next=list[u]; list[u]=E;
}
*/
int input()
{
    int a,k=1; char c;
    while ( (c=getchar())>'9' || c<'0')
        if (c=='-') k=-1;
    a=c-'0';
    while ( (c=getchar())<='9' && c>='0') a=a*10+c-'0';
    return a*k;
}
char s[6][6];

bool judge(char x)
{
    rep(i,0,3)
    {
        bool f=true;
        rep(j,0,3) f&=(s[i][j]=='T' || s[i][j]==x);
        if (f) return true;
        f=true;
        rep(j,0,3) f&=(s[j][i]=='T' || s[j][i]==x);
        if (f) return true;
    }
    bool f=true;
    rep(i,0,3) f&=(s[i][i]=='T' || s[i][i]==x);
    if (f) return true;

    f=true;
    rep(i,0,3) f&=(s[i][3-i]=='T' || s[i][3-i]==x);
    if (f) return true;

    return false;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a_l.out","w",stdout);
    int T,cas=0;
    scanf("%d",&T);
    while (T--)
    {
        rep(i,0,3) scanf("%s",s[i]);
        printf("Case #%d: ",++cas);
        if (judge('X')) puts("X won");
        else
        if (judge('O')) puts("O won");
        else
        {
            bool f=false;
            rep(i,0,3) rep(j,0,3) f|=(s[i][j]=='.');
            if (f) puts("Game has not completed");
            else puts("Draw");
        }
    }
    //system("pause");
    return 0;
}
