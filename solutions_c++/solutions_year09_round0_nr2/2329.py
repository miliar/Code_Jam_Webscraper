/*
  ID: nigo1
  LANG: C++
  TASK:
*/
#include <iostream>
#include <stdio.h>

#define pf printf
#define sf scanf
#define TIME ((double)clock()/CLOCKS_PER_SEC)

using namespace std;

int T, H, W, a[100][100], b[100][100], l = 0;
int moves[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int dfs(int i, int j) {
    if (b[i][j] != -1) return b[i][j];
    
    int minn = a[i][j], minm = -1;
    
    for (int k = 0; k < 4; k++)
        if (i + moves[k][0] >= 0 && i + moves[k][0] < H && j + moves[k][1] >= 0 && j + moves[k][1] < W)
           if (a[i + moves[k][0]][j + moves[k][1]] < minn)
              minn = a[i + moves[k][0]][j + moves[k][1]], minm = k;
    
    return b[i][j] = (minm == -1) ? l++ : dfs(i + moves[minm][0], j + moves[minm][1]);
}
    
int main()
{
    //freopen ("B-large.in", "r", stdin);
   // freopen ("B-large.out", "w", stdout);
    
    sf("%i", &T);
    for (int i = 0; i < T; i++) {
        memset(b, -1, sizeof(b));
        l = 0;
        
        sf("%i%i", &H, &W);
        for (int j = 0; j < H; j++)
            for (int k = 0; k < W; k++)
                sf("%i", &a[j][k]);
                
        for (int j = 0; j < H; j++)
            for (int k = 0; k < W; k++)
                if (b[j][k] == -1)
                   dfs(j, k);
                   
        pf("Case #%i:\n", i + 1);
        for (int j = 0; j < H; j++, pf("\n"))
            for (int k = 0; k < W; k++)
                pf(k == W - 1 ? "%c" : "%c ", (char)(b[j][k] + 'a'));
    }      

    //sf("%i", &T);
}
