#include<iostream>
using namespace std;
#define Ls(p) (p*2)
#define Rs(p) (p*2+1)
int M[1<<15];
int P;
int A[1<<15];
int F[1<<15][20];
int V[1<<15];
void CMIN(int&a, int b)
{
     if(b < a) a = b;
}
void Build(int p, int L, int R)
{
    int i, j, k;
    if(L < R)
    {
        Build(p*2, L, (L+R)/2);
        Build(p*2+1, (L+R)/2+1, R);
        int v = V[p];
       // scanf("%d", &v);

        for(j = 0; j <= P; ++j)
           for(k = 0; k <= P; ++k)
           {
               i = max(j, k);
               CMIN(F[p][i], F[Ls(p)][j]+ F[Rs(p)][k]);
               
               i = max(j ,k) - 1;
               if(i >= 0)
                    CMIN(F[p][i], F[Ls(p)][j]+F[Rs(p)][k]+v);
           }
    }
    else
    {
        for(i = P-M[L]; i <= P; ++i)
              F[p][i] = 0;
    }
    
    //printf("P: %d\n", p);
    //1int i;
    //for(i = 0; i <= P; ++i) printf("%d ", F[p][i]); printf("\n"); 
}
int main()
{
    int t, cs = 0;
    int i, j;
    freopen("B_L.in", "r", stdin);
    freopen("B_L.out", "w", stdout);
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d", &P);
       for(i = 0; i < (1<<P); ++i)
           scanf("%d", &M[i]);
       for(i = P - 1; i >= 0; --i)
          for(j = 0; j < (1 << i); ++j)
          {
              scanf("%d", V + (1<<i)+j);
          }
       memset(F, 63, sizeof(F));
       Build(1, 0, (1<<P)-1);
       printf("Case #%d: %d\n", ++cs, F[1][0]);
    }
}
