
// Headers {{{
#include<iostream>
#include<cstdio>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<utility>
#include<sstream>
#include<cstring>
using namespace std;
#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define FORD(I,A,B) for(int I=(A);I>=(B);I--)
#define REP(I,N) for(int I=0;I<(N);I++)
#define VAR(V,init) __typeof(init) V=(init)
#define FORE(I,C) for(VAR(I,(C).begin());I!=(C).end();I++)
#define CLR(A,v) memset((A),v,sizeof((A)))
#define ALL(X) (X).begin(),(X).end()
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define SIZE(x) (int)(x.size())
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef long long LL;
typedef long double LD; 
typedef vector<string> VS;
// }}}

const int max_s = 111; 
const int inf = (1<<30); 
int h[max_s][max_s], res[max_s][max_s]; 
char ret[max_s][max_s]; 
int W,H,TC; 

int dfs(int a, int b) { 
    int dy[] = {-1,0,0,1}; 
    int dx[] = {0,-1,1,0}; 

    int y, x, mn = h[a][b]; 
    res[a][b] = -1; 
    REP(i,4) mn = min(h[a+dy[i]][b+dx[i]], mn); 

    REP(i,4) { 
        y = a + dy[i]; 
        x = b + dx[i]; 
        if (h[y][x] < h[a][b] && h[y][x] == mn) { 
            res[a][b] = dfs(y, x); 
            break; 
        } 
    } 
    if (res[a][b] == -1) { 
        res[a][b] = a * (max_s) + b; 
    } 
    return res[a][b]; 
} 

map<int,char> M; 

int main()
{
    scanf("%d", &TC); 
    FOR(T,1,TC) { 
        scanf("%d%d",&H,&W); 
        REP(i,H+2) REP(j,W+2) h[i][j] = inf; 
        FOR(i,1,H) FOR(j,1,W) scanf("%d",&h[i][j]); 
        CLR(res,-1); 
        FOR(i,1,H) FOR(j,1,W) if (res[i][j] == -1) { 
            dfs(i,j);            
        } 
        M.clear(); 
        char st = 'a'; 

        FOR(i,1,H) FOR(j,1,W) { 
            if (!M.count(res[i][j])) { 
                M[res[i][j]] = st; 
                ++st; 
            } 
            ret[i][j] = M[res[i][j]]; 
        } 
        printf("Case #%d:\n",T); 
        FOR(i,1,H) { 
            FOR(j,1,W) printf("%c ",ret[i][j]); 
            puts(""); 
        }       
    } 

	return 0;
}

