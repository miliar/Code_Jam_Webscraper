#include<cstdio>
#include<cstring>

int main()
{
   int i, j, k, result;
   int L, D, N;
   char d[5001][20];
   char n[501][500];
   int t[501][15];

   scanf("%d", &L);
   scanf("%d", &D);
   scanf("%d", &N);

   for(i = 0 ; i < D ; i++)
   {
      scanf("%s", d[i]);
   }

   for(i = 0 ; i < N ; i++)
   {
      scanf("%s", n[i]);

      k = 0;
      for(j = 0 ; j < L ; j++)
      {
         t[i][j] = 0;
         if(n[i][k] == '(')
         {
            k++;
            while(n[i][k] >= 'a' && n[i][k] <= 'z')
            {
               t[i][j] |= (1 << (n[i][k] - 'a'));
               k++;
            }
         }
         else
         {
            t[i][j] |= (1 << (n[i][k] - 'a'));
         }
         k++;

         //printf("%d ", t[i][j]);
      }
      //printf("\n");

      result = 0;
      for(j = 0 ; j < D ; j++)
      {
         k = 0;
         while(k < L && ((1 << (d[j][k] - 'a')) & t[i][k]))
         {
            k++;
         }

         if(k == L)
         {
            result++;
         }
      }

      printf("Case #%d: %d\n", i + 1, result);
   }

   return 0;
}

