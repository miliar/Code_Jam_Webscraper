#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
using namespace std;
/*---------------------------------------------------------*/
#define INF 123456789
#define SI(A) ((int)(A).size())
#define ALL(A) A.begin(),A.end()
#define CL(A,v) memset(A, v, sizeof(A))
#define FOR(i,a,b) for ( int i = (a); i <= (b); ++i )
#define REP(i,N) for ( int i = 0; i < N; ++i )
#define IT(T,A,i) for ( T::iterator i = (A).begin(); i != (A).end(); ++i )
#define BIT(mask,i) ((mask) & (1 << (i)))
/*---------------------------------------------------------*/
int lowbit(int set) { return (set^(set-1))&set; }
int countbit(int set) { return (set==0)?0:(1+countbit(set-lowbit(set))); }
/*---------------------------------------------------------*/
template<class T> void print(vector<T> A,int n=-1){if(n==-1||n>A.size())n=A.size();cout<<"{";for (int i=0;i<n;i++)cout<<A[i]<<" ";cout<<"}"<<endl;}
template<class T> void print(T A[],int n){cout<<"{";for (int i=0;i<n;i++)cout<<A[i]<<" ";cout<<"}"<<endl;}
/*---------------------------------------------------------*/
typedef vector<int> VI;
typedef vector<string> VS;
typedef double LD;
typedef long long LL;
/*---------------------------------------------------------*/
const int maxn = 123;
int cr, cc, a[maxn][maxn];
const int DIR[4][2] = {
    {-1, 0},
    {0, -1},
    {0, 1},
    {1, 0}
};

void read()
{
    scanf("%d%d", &cr, &cc);
    REP(r, cr) REP(c, cc)
        scanf("%d", &a[r][c]);
}

vector<VI> adj;

void flow(int r0, int c0)
{
    int r1, c1, r2, c2, m = INF;
    REP(dir, 4)
    {
        r1 = r0 + DIR[dir][0];
        c1 = c0 + DIR[dir][1];
        if (r1 < 0 || r1 >= cr || c1 < 0 || c1 >= cc) continue;
        if (a[r1][c1] < m)
            m = a[r2 = r1][c2 = c1];
    }
    if (m >= a[r0][c0])
        return;
    adj[r0 * cc + c0].push_back(r2 * cc + c2);
    adj[r2 * cc + c2].push_back(r0 * cc + c0);
}

char mark[maxn * maxn];

void dfs(int a, char m)
{
    if (mark[a] != ' ') return;
    mark[a] = m;
    REP(i, SI(adj[a]))
        dfs(adj[a][i], m);
}

void solve()
{
    adj = vector<VI>(cr * cc);
    REP(r, cr) REP(c, cc)
        flow(r, c);

    char m = 'a';
    CL(mark, ' ');
    mark[cr * cc] = 0;
    REP(i, cr * cc) if (mark[i] == ' ')
        dfs(i, m++);
}

int main()
{
    int ct;
    scanf("%d", &ct);
    for (int t = 1; t <= ct; ++t)
    {
        read();
        solve();
        printf("Case #%d:\n", t);
        REP(r, cr) REP(c, cc)
            printf("%c%c", mark[r * cc + c], c < cc - 1 ? ' ' : '\n');
    }
    return 0;
}

