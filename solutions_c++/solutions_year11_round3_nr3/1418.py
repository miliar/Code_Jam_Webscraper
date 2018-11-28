#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

FILE
	*fpi = fopen("C-small.in", "r"),
	*fpo = fopen("C-small.out", "w");

int gcd(int x, int y)
{
   int
      s = min(x, y),
      l = max(x, y),
      r = l % s;

   if (!r)
      return s;

   return (gcd(s, r));
}

int gcd(vector<int> v, int n, int l)
{
   int
      s = v.size();

   if (n == s - 1)
      return (v[s - 1]);

   int
      g = gcd(v[s - 1], v[s - 2]);

   if (g < l)
      return (-1);

   for (int i = s - 3; i >= n; i--)
      {
      g = gcd(g, v[i]);
      if (g < l)
         return (-1);
      }

   return (g);
}

int lcm(int x, int y)
{
   return (x * y / gcd(x, y));
}

int lcm(vector<int> v, int n, int h)
{
   if (n == 1)
      return (v[0]);

   int
      l = lcm(v[0], v[1]);

   if (l > h)
      return (-1);

   for (int i = 2; i < n; i++)
      {
      l = lcm(l, v[i]);
      if (l > h)
         return (-1);
      }

   return (l);
}

int main(int argc, char *argv[])
{
	int
		T;

	fscanf(fpi, "%d", &T);
	for (int i = 0; i < T; i++)
		{
		int
			N,
			L,
         H,
         f,
         j;

      vector<int>
         v;

		bool
			bPoss = false;

      int
         best;

		fscanf(fpi, "%d %d %d", &N, &L, &H);
		for (j = 0; j < N; j++)
         {
         fscanf(fpi, "%d", &f);
         v.push_back(f);
         }

      if (L == 1)
         {
         bPoss = true;
         best = 1;
         }
      else
         for (best = L; best <= H; best++)
            {
            for (j = 0; j < N; j++)
               if (best >= v[j])
                  {
                  if (best % v[j] != 0)
                     break;
                  }
               else
                  {
                  if (v[j] % best != 0)
                     break;
                  }

            if (j == N)
               {
               bPoss = true;
               break;
               }
            }

      if (bPoss)
		   fprintf(fpo, "Case #%d: %d\n", i + 1, best);
      else
		   fprintf(fpo, "Case #%d: NO\n", i + 1);
      }
}

/*
int main(int argc, char *argv[])
{
	int
		T;

	fscanf(fpi, "%d", &T);
	for (int i = 0; i < T; i++)
		{
		int
			N,
			L,
         H,
         f;

      vector<int>
         v;

		bool
			bPoss = false;

      int
         best;

		fscanf(fpi, "%d %d %d", &N, &L, &H);
		for (int j = 0; j < N; j++)
         {
         fscanf(fpi, "%d", &f);
         v.push_back(f);
         }

      if (L == 1)
         {
         bPoss = true;
         best = 1;
         }
      else
         {
         sort(v.begin(), v.end());

         for (int n = 0; n < N; n++)
            {
            int
               g = gcd(v, n, L);

            if (g != -1)
               if (n == 0)
                  {
                  for (int s = (int)ceil(sqrt((double)g)); s >= 1; s--)
                     if (g % s == 0)
                        {
                        if (s <= H)
                           {
                           if (!bPoss)
                              {
                              bPoss = true;
                              best = s;
                              }
                           else
                              best = min(best, s);
                           }

                        if (g / s <= H)
                           {
                           if (!bPoss)
                              {
                              bPoss = true;
                              best = g / s;
                              }
                           else
                              best = min(best, g / s);
                           }
                        }
                  }
               else
                  {
                  for (int s = (int)ceil(sqrt((double)g)); s >= 1; s--)
                     if (g % s == 0)
                        {
                        if (s <= H)
                           {
                           int
                              n2;

                           for (n2 = 0; n2 < n; n2++)
                              if (s % v[n2] != 0)
                                 break;

                           if (n2 == n)
                              if (!bPoss)
                                 {
                                 bPoss = true;
                                 best = s;
                                 }
                              else
                                 best = min(best, s);
                           }

                        if (g / s <= H)
                           {
                           int
                              n2;

                           for (n2 = 0; n2 < n; n2++)
                              if ((g / s) % v[n2] != 0)
                                 break;

                           if (n2 == n)
                              if (!bPoss)
                                 {
                                 bPoss = true;
                                 best = g / s;
                                 }
                              else
                                 best = min(best, g / s);
                           }
                        }
                  }
            }

         for (int n = N; n > 0; n--)
            {
            int
               l = lcm(v, n, H);

            if (l != -1)
               if (n == N)
                  {
                  if (l >= L)
                     {
                     if (!bPoss)
                        {
                        bPoss = true;
                        best = l;
                        }
                     else
                        best = min(best, l);
                     }
                  else
                     {
                     double
                        d1 = (double)L / l,
                        d2 = (double)H / l,
                        c1 = ceil(d1),
                        c2 = floor(d2);

                     if (c2 >= c1)
                        if (!bPoss)
                           {
                           bPoss = true;
                           best = l * (int)c1;
                           }
                        else
                           best = min(best, l * (int)c1);
                     }
                  }
               else
                  {
                  if (l >= L)
                     {
                     int
                        n2;

                     for (n2 = n; n2 < N; n2++)
                        if (v[n2] % l != 0)
                           break;

                     if (n2 == N)
                        {
                        if (!bPoss)
                           {
                           bPoss = true;
                           best = l;
                           }
                        else
                           best = min(best, l);
                        }
                     }
                  }
            }
         }

      if (bPoss)
		   fprintf(fpo, "Case #%d: %d\n", i + 1, best);
      else
		   fprintf(fpo, "Case #%d: NO\n", i + 1);
		}

	fclose(fpi);
	fclose(fpo);
	return 0;
}
*/
