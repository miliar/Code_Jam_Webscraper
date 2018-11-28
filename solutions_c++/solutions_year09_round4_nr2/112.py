#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define MST(a,b) (memset(a,b,sizeof(a)))
#define DB(x) (cout<<#x<<": "<<x<<endl)
#define PB push_back
#define MP make_pair
#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;


int R, C, F;
int D;
int cnt;

bool vis[16][8][32][1<<12];
char Map[64][64];

void Out(char M[][64])
{
     int i, j;
     for(i=1;i<=R;++i){for(j=1;j<=C;++j)putchar(M[i][j]);printf("\n");}
}
bool dfs(int r, int c, char  M[][64], int d)
{//printf("// %d %d\n", r, c);
  
     if(c < 1 || c > C) return 0;
     if(M[r][c] == '#') return 0;
     if(d > D) return 0;
     
     int f = 0;
     while(r < R && M[r+1][c] == '.') r++, ++f;
     if(f > F) return 0;
     if(r >= R) 
     {
        /*printf(":\n");
          Out(M); 
          printf("== %d %d\n", r, c);*/
          return 1;
     }
    
      cnt++;
  
     int mk = 0, i;
     for(i = 1; i <= C; ++i)
     {
           if(M[r][i] == '.') mk = mk << 1;
           else mk = (mk << 1) | 1;
     }     
     for(i = 1; i <= C; ++i)
     {
           if(M[r+1][i] == '.') mk = mk << 1;
           else mk = (mk << 1) | 1;
     }     
     
 
     if(vis[r][c][d][mk]) return 0;
     
     vis[r][c][d][mk] = 1;

  

     //if(M[r+1][c] == '#')
     {

         if(dfs(r, c-1, M, d)) return 1;
         if(dfs(r, c+1, M, d)) return 1;
     }
     
     if(c > 1 && M[r+1][c-1] == '#' && M[r][c-1] == '.')
     {
         M[r+1][c-1] = '.';

         if(dfs(r, c, M, d+1)) return 1;
         M[r+1][c-1] = '#';
     }
     
     if(c < C && M[r+1][c+1] == '#' && M[r][c+1] == '.')
     {
         M[r+1][c+1] = '.';

         if(dfs(r, c, M, d+1)) return 1;
         M[r+1][c+1] = '#';
     }
     return 0;
}
int main()
{
    int t, Case;
    int i, j;
    int lastCnt;
    bool f;
    freopen("B_S4.in", "r", stdin);
    freopen("B_S4.out", "w", stdout);
    scanf("%d", &t);
    for(Case = 1; Case <= t; ++Case)
    {
        scanf("%d%d%d", &R, &C, &F);
        memset(Map, 0, sizeof(Map));

        for(i = 1; i <= R; ++i)
            scanf("%s", Map[i]+1);
        f=0;
        lastCnt = -1;
        for(D = 0;; D++)
        {
            memset(vis, 0, sizeof(vis));
            cnt = 0;
            if(dfs(1, 1, Map, 0))
            {
                f =  1;
                break;
            }
            if(cnt == lastCnt) break;
            lastCnt = cnt;
        }
        
        if(f)      
        printf("Case #%d: Yes %d\n", Case, D);
        else printf("Case #%d: No\n", Case);
    }
}
/*
5 8 3
........
########
...#.###
####..##
###.##..
2 2 1
.#
##
3 3 1
...
###
###
3 2 1
..
#.
..
2 2 1
..
..
2 2 2
..
..
4 3 1
...
###
###
###
8 6 7
....##
####..
######
......
######
######
.#####
######
5 6 7
....##
####..
######
......
######
8 4 1
...#
####
####
####
###.
####
#.##
####
6 6 1
......
######
######
######
######
######
7 6 1
......
######
######
######
######
######
*/
