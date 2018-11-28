#include <stdio.h>

char a[512], b[16];
int nr[512][36], n,m, test_case;
int pot[512][36];

void solve()
{
     ++test_case;

     for (int i=0;i<512;++i)
          a[i] = 0;

     fgets(a+1,511,stdin);

     n=1;
     
     while (a[n+1] != 0)
          ++n;

     for (int i=1;i<=n;++i)
     for (int j=1;j<=m;++j)
          nr[i][j] = 0,
          pot[i][j] = 0;

     for (int i=0;i<=n;++i)
          nr[i][0] = 1,
          pot[i][0] = 1;


     for (int i=1;i<=n;++i)
     {
//          printf("%c ", a[i]);

     for (int j=1;j<=m;++j)
     {
          nr[i][j] = nr[i-1][j];
          pot[i][j] |= pot[i-1][j];
          
          if (a[i] == b[j] && pot[i-1][j-1] == 1)
               nr[i][j] += nr[i-1][j-1],
               pot[i][j] = 1;
               
          nr[i][j] %= 10000;
          
          //printf("%d ", nr[i][j]);
     }
//          printf("\n");
     }
     
     char ret[6];
     
     ret[0] = ret[1] = ret[2] = ret[3] = '0';
     ret[4] = '\n';
     ret[5] = 0;
     
     int ind = 3;
     
     while(nr[n][m] > 0 && ind >= 0)
     {
          ret[ind] = '0' + nr[n][m] % 10;
          nr[n][m] /= 10;
          --ind;
     }

     ret[3] =
     printf("Case #%d: %s", test_case, ret);
}

int main()
{
     freopen("C.in","r",stdin);
     freopen("C.out","w",stdout);

     sprintf(b+1,"welcome to code jam");

     m = 1;
     while (b[m+1] != 0)
          ++m;


     int t;
     
     scanf("%d\n", &t);
     
     while (t--)
          solve();

     return 0;
}
