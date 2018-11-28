#include<stdio.h>
#include<memory.h>

int F[12][1 << 10];
int num[1 << 10];
int N, M, Res;
char map[12][12];
int mapp[12];
bool A(int a, int b)
{
    int i;
    for(i = 0; i < M; ++i)
        if( (a & (1 << i))  &&
            (i && (b & (1 << (i - 1))) 
            || (i < M - 1 && (b & (1 << (i + 1))))) )
            return 0;
    return 1;
}
bool A2(int a, int b)
{
     int i;
     for(i = 0; i < M; ++i)
         if((a &( 1<< i)) &&(b & (1 << i))) return 0;
     return 1;
}
void DP()
{
    memset(F, 0, sizeof(F));
    F[0][0] = 0;
     int i, j, k;
     for(k = 1; k <= N; ++k)
     for(i = 0; i < (1 << M); ++i)
         for(j = 0; j < (1 << M); ++j)
         {
             if(A(i, i) && A2(mapp[k - 1], i) && A(i, j) && A2(mapp[k], j) && A(j, j))
             {
                 if(F[k - 1][i] != -1 && F[k - 1][i] + num[j] > F[k][j])
                     F[k][j] =  F[k - 1][i] + num[j];
             }
             if(F[k][j] > Res) Res = F[k][j];
         }
         
}

void Cal(int i)
{
     int r = 0;
     int k = i;
     while(i)
     {
         if(i & 1)
             ++r;
         i >>= 1;
     }
     num[k] = r;
}
int main()
{
    int t, ctr = 0, i, j;
    freopen("C_S.in", "r", stdin);
    freopen("C_S.out", "w", stdout);
    for(i = 1; i < 1024; ++i)
        Cal(i);
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d%d", &N, &M);
        for(i = 1; i <= N; ++i)
        {
            mapp[i] = 0;
            scanf("%s", map[i] + 1);
            for(j = 1; j <= M; ++j)
            {
                
                mapp[i] |= (map[i][j] == 'x') << (j - 1);
            }
           // printf("%d %d\n", i, mapp[i]); 
        }
        Res = 0;
        DP();
        printf("Case #%d: %d\n", ++ctr, Res);
    }
}
/*
2 3
...
...
2 2
..
..
2 2
xx
xx
2 3
x.x
xxx
2 3
x.x
x.x
10 10
....x.....
..........
..........
..x.......
..........
x...x.x...
.........x
...x......
........x.
.x...x....
3 10
xxxxxxxxxx
xxxxxxxxxx
..........
*/
