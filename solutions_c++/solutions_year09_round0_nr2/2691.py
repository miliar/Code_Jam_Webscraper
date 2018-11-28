using namespace std;
#import <iostream>
#import <map>

#define H_MAX 100
#define W_MAX 100
#define EVEREST 10000

int spot[H_MAX][W_MAX];
int parent[H_MAX * W_MAX];

inline int label(int i, int j, int w)
{
   return i * w + j;
}

int flow_direction(int i, int j, int h, int w)
{
   int center, north, west, east, south;
   center = spot[i][j];
   north = i > 0 ? spot[i - 1][j] : EVEREST;
   west = j > 0 ? spot[i][j - 1] : EVEREST;
   east = j < w - 1 ? spot[i][j + 1] : EVEREST;
   south = i < h - 1 ? spot[i + 1][j] : EVEREST;
   
   if ((center <= north || north == EVEREST)
      && (center <= west || west == EVEREST)
      && (center <= east || east == EVEREST)
      && (center <= south || south == EVEREST))
   {
      return label(i, j, w);
   }
   if (north <= west && north <= east && north <= south)
      return label(i - 1, j, w);
   if (west <= east && west <= south)
      return label(i, j - 1, w);
   if (east <= south)
      return label(i, j + 1, w);
   return label(i + 1, j, w);
}

int main()
{
   int n;
   scanf("%d", &n);
   int n_case = 0;
   while (n_case++ < n)
   {
      int h, w;
      scanf("%d %d", &h, &w);
      
      for (int i = 0; i < h; ++i)
         for (int j = 0; j < w; ++j)
            scanf("%d", &spot[i][j]);
      
      for (int i = 0; i < h; ++i)
         for (int j = 0; j < w; ++j)
            parent[label(i, j, w)] = flow_direction(i, j, h, w);
      
      printf("Case #%d:", n_case);
      
      map<int, char> basin;
      int lim = h * w;
      char cur_basin = 'a';
      for (int i = 0; i < lim; ++i)
      {
         if (i % w == 0) printf("\n");
         else printf(" ");
         
         int current = i;
         while (parent[current] != current)
            current = parent[current];
         
         if (basin[current])
         {
            printf("%c", basin[current]);
         }
         else
         {
            printf("%c", cur_basin);
            basin[current] = cur_basin;
            ++cur_basin;
         }
      }
      
      if (n_case < n) printf("\n");
   }
   return 0;
}
