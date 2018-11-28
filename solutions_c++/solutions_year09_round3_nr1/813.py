#include<cstdio>
#include<cstring>

unsigned long long base(unsigned long long * n, int len, unsigned long long b)
{
   int i;
   long long p = 1, res = 0;

   for(i = len - 1 ; i >= 0 ; i--)
   {
      res += (n[i] * p);
      p *= b;
   }

   return res;
}

int main()
{
   int T, i, j, len, actV = 1, k;
   unsigned long long in[70];
   char line[70];
   char lett[26];
   char digi[10];


   scanf("%d", &T);

   for(k = 1 ; k <= T ; k++)
   {
      scanf("%s", line);
      len = strlen(line);

      actV = 1;

      //memset(digi, 0, sizeof(digi));
      //memset(lett, 0, sizeof(lett));
      for(i = 0 ; i < 26  ; i++)
      {
         lett[i] = -1;
      }

      for(i = 0 ; i < 10  ; i++)
      {
         digi[i] = -1;
      }

      if(line[0] >= '0' && line[0] <= '9')
      {
         digi[(line[0] - '0')] = actV;
         line[0] = actV;
      }
      else
      {
         lett[(line[0] - 'a')] = actV;
         line[0] = actV;
      }
      actV = 0;

      for(j = 0 ; j < len ; j++)
      {
         if (line[j] < 37) continue;
         if(line[j] >= '0' && line[j] <= '9')
         {
            if (digi[(line[j] - '0')] > -1)
            {
               line[j] = digi[(line[j] - '0')];
            }
            else
            {
               digi[(line[j] - '0')] = actV;
               line[j] = actV;
               actV++;
            }
         }
         else
         {
            if (lett[(line[j] - 'a')] > -1)
            {
               line[j] = lett[(line[j] - 'a')];
            }
            else
            {
               lett[(line[j] - 'a')] = actV;
               line[j] = actV;
               actV++;
            }
         }

         if (actV == 1) actV++;
      }

      for(j = 0 ; j < len ; j++)
      {
         in[j] = line[j];
      }

      if(actV == 0) actV = 2;
      printf("Case #%d: %lld\n", k, base(in, len, actV));
   }

   return 0;
}
