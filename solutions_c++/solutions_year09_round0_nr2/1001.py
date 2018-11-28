#include <cstdio>
#include <cstring>

int H, W, l;
int map[100][100];
int C[100][100];
bool was[100][100];

int rec(int x, int y)
{
   int xx, yy, d = 0, min = 10001;

   if(C[y][x])
   {
      return C[y][x];
   }

   //north
   if (y && map[y][x] > map[y-1][x] && map[y-1][x] < min && !was[y-1][x])
   {
      min = map[y-1][x];
      d = 1;
      xx = x; yy = y - 1;
   }

   //west
   if (x && map[y][x] > map[y][x-1] && map[y][x-1] < min && !was[y][x-1])
   {
      min = map[y][x-1];
      d = 2;
      xx = x - 1; yy = y;
   }

   //east
   if (x + 1 < W && map[y][x] > map[y][x+1] && map[y][x+1] < min && !was[y][x+1])
   {
      min = map[y][x+1];
      d = 3;
      xx = x + 1; yy = y;
   }

   //south
   if (y + 1 < H && map[y][x] > map[y+1][x] && map[y+1][x] < min && !was[y+1][x])
   {
      min = map[y+1][x];
      d = 4;
      xx = x; yy = y + 1;
   }

   if (d)
   {
      was[yy][xx] = true;
      C[y][x] = rec(xx, yy);
      was[yy][xx] = false;
   }
   else
   {
      C[y][x] = l++;
   }

   return C[y][x];
}

int main()
{
   int i, j, k;
   int T;

   scanf("%d", &T);

   for(i = 1 ; i <= T ; i++)
   {
      scanf("%d", &H);
      scanf("%d", &W);

      for(j = 0 ; j < H ; j++)
      {
         for(k = 0 ; k < W ; k++)
         {
            scanf("%d", &map[j][k]);
         }
      }

      printf("Case #%d:\n", i);

      memset(C, 0, sizeof(C));
      memset(was, false, sizeof(was));
      l = 1;
      for(j = 0 ; j < H ; j++)
      {
         for(k = 0 ; k < W ; k++)
         {
            C[j][k] = rec(k, j);
            printf("%c ", (char)(C[j][k] - 1) + 'a');
         }
         printf("\n");
      }
   }

   return 0;
}

