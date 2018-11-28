#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <cctype>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

const int MAXS = 10;
char str[MAXS][MAXS], cho[MAXS][MAXS], cnt[MAXS][MAXS];
const int dr[] = {-1, 1, 0, 0, 1, -1, 1, -1}, dc[] = {0, 0, 1, -1, 1, -1, -1, 1};
int T, R, C, ans;



void solve(int r, int c)
{
    if(r == R)
    {
        bool flag = true;
        memset(cnt, 0, sizeof(cnt));
        //simulation
        for(int i = 0; i < R; i++)
            for(int j = 0; j < C; j++)
            {
                int chod, nr, nc;
                char ch = str[i][j];
                
                if(ch=='|')
                    chod = 0;
                else if(ch=='-')
                    chod = 2;
                else if(ch=='\\')
                    chod = 4;
                else
                    chod = 6;
                
                chod += cho[i][j];
                nr = i+dr[chod], nc = j+dc[chod];
                nr = (nr+R)%R, nc = (nc+C)%C;
                ++cnt[nr][nc];
            }
        
        for(int i = 0; i < R; i++)
            for(int j = 0; j < C; j++)
                if(cnt[i][j] != 1)
                {
                    flag = false;
                    break;
                }
        
        if(flag) ++ans;
        return ;
    }
    
    if(c==C)
    {
        solve(r+1, 0);
        return ;
    }
    
    cho[r][c] = 0;
    solve(r, c+1);
    cho[r][c] = 1;
    solve(r, c+1);    
}

int main()
{
    freopen("Cs.in", "r", stdin);
    freopen("outc_s.txt", "w", stdout);
    scanf("%d\n", &T);
    
    for(int t = 1; T--; ++t)
    {
        ans = 0;
        scanf("%d %d\n", &R, &C);
        for(int i = 0; i < R; i++)
            scanf("%s\n", str[i]);
        
        solve(0, 0);
        
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
