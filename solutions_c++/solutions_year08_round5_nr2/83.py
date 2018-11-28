#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#define MAX_N 32
#define INF 0x3f3f3f3f

char P[MAX_N][MAX_N];
int D[MAX_N][MAX_N], U[MAX_N][MAX_N];

const int dx[] = { -1, 0, 1, 0},
          dy[] = {  0,-1, 0, 1};

int main(void)
{
    int test, tests;
    
    freopen("b-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    scanf("%d", &tests);
    for (test = 1; test <= tests; test++)
    {
        int i, j, R, C, si, sj, ei, ej, move, moves;

        scanf("%d%d\n", &R, &C);
        for (i = 0; i < R; i++)
        {
            scanf("%s", P[i]);
            for (j = 0; j < C; j++)
                if (P[i][j] == 'O')
                   P[i][j] = '.', si = i, sj = j;
                else
                if (P[i][j] == 'X')
                   P[i][j] = '.', ei = i, ej = j;
        }
            
        memset(D, 0x3f, sizeof(D));
        memset(U, 0, sizeof(U));
        
        D[si][sj] = 0;
        moves = R * C;
        for (move = 0; move < moves; move++)
        {
            int m = INF, pi, pj;
            
            for (i = 0; i < R; i++)
                for (j = 0; j < C; j++)
                    if (D[i][j] < m && (!U[i][j]))
                       m = D[i][j], pi = i, pj = j;
            
            U[pi][pj] = 1;
            
            for (i = 0; i < 4; i++)
            {
                int ni = pi + dx[i], nj = pj + dy[i];
                
                if (ni >= 0 && ni < R && nj >= 0 && nj < C && P[ni][nj] == '.' && D[ni][nj] > (D[pi][pj] + 1))
                   D[ni][nj] = D[pi][pj] + 1;      
            }
            
            for (i = 0; i < 4; i++)
            {
                int fi = pi, fj = pj, add;
                
                for (; fi >= 0 && fi < R && fj >= 0 && fj < C && P[fi][fj] == '.'; fi += dx[i], fj += dy[i]) ;
                add = abs(fi - pi) + abs(fj - pj);
                
                for (j = 0; j < 4; j++)
                    if (i != j)
                    {
                       int ni = pi, nj = pj;
                       
                       for (; ni >= 0 && ni < R && nj >= 0 && nj < C && P[ni][nj] == '.'; ni += dx[j], nj += dy[j]) ;
                       ni -= dx[j], nj -= dy[j];
                       
                       if (D[ni][nj] > (D[pi][pj] + add))
                          D[ni][nj] = D[pi][pj] + add;
                    }
            }
        }
        
        if (D[ei][ej] != INF)
           printf("Case #%d: %d\n", test, D[ei][ej]);
        else printf("Case #%d: THE CAKE IS A LIE\n", test);
    }
    
    return 0;
}
