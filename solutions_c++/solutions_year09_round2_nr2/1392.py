#include <cstdio>
#include <cstring>

int main()
{
   int i, j, k, lz, l;
   int tab[11], wz[11];
   int T, N;
   bool is = true;

   scanf("%d", &T);

   for(i = 1 ; i <= T ; i++)
   {
      scanf("%d", &N);

      memset(wz, 0, sizeof(wz));

      k = N;
      while(k)
      {
         wz[(k % 10)]++;
         k /= 10;
      }

      lz = 0;
      j = N;
      while(1)
      {
         memset(tab, 0, sizeof(tab));

         k = (++j);
         while(k)
         {
            tab[(k % 10)]++;
            k /= 10;
         }

         if (j == 10 || j == 100 | j == 1000 || j == 10000 || j == 100000 || j == 1000000 || j == 10000000)
         {
            lz++;
         }

         is = true;
         for(l = 1 ; l <= 10 ; l++)
         {
            if (tab[l] != wz[l]) is = false;
         }

         if(is && (tab[0] - lz) == wz[0])
         {
            printf("Case #%d: %d\n", i, j);
            break;
         }
      }
   }

   return 0;
}
