#include<iostream>
using namespace std;
bool mat[128][128];
int R, i1, i2, j1, j2;
int Solve()
{
    int i, j;
    int res = 0;
    bool end = false;
    bool m2[128][128];
    
    while(!end)
    {
       end=  true;
       ++res;
       memset(m2, 0, sizeof(m2));
       for(i = 1; i <= 100; ++i)
       {
           for(j = 1; j <= 100; ++j)
           {
               if(mat[i-1][j] && mat[i][j-1]) m2[i][j] = 1;
               if(mat[i][j]) m2[i][j] = 1;
               if(!mat[i-1][j] && !mat[i][j-1]) m2[i][j] = 0;
               if(m2[i][j] == 1) end = false;
           }
       }
       memcpy(mat, m2, sizeof(m2));
    }
    return res;
}
int main()
{
    int t, cs = 0;
    int i, j, k;
    freopen("C_S.in", "r", stdin);
    freopen("C_S.out", "w", stdout);
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d", &R);
        //printf("%d\n", R);
        memset(mat, 0, sizeof(mat));
        for(k = 0; k < R; ++k)
        {//printf("i:%d\n", i);
              scanf("%d%d%d%d", &i1, &j1, &i2, &j2);
              for(i = i1; i <= i2; ++i)
                 for(j = j1; j <= j2; ++j)
                     mat[i][j] = 1;
        }
        printf("Case #%d: %d\n", ++cs, Solve());
    }
}
