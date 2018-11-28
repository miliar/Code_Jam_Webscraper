#define _CRT_SECURE_NO_WARNINGS
#include <map>
#include <stdio.h>
using namespace std;

typedef struct
{
   int
      array_index,
      start_index,
      riders;

} coaster_info;

__int64 process_case(FILE *fpi)
{
   int
      R,
      k,
      N,
      g[1000],
      start_index = 0,
      array_index = 0;

   coaster_info
      aryCoasters[100];

   map<int, coaster_info *>
      mapCoasters;

   map<int, coaster_info *>::const_iterator
      iter;

   fscanf(fpi, "%d", &R);
   fscanf(fpi, "%d", &k);
   fscanf(fpi, "%d", &N);

   for (int i = 0; i < N; i++)
      fscanf(fpi, "%d", &g[i]);

   while (array_index < R)
   {
      iter = mapCoasters.find(start_index);
      if (iter != mapCoasters.end())
         break;

      int
         riders = 0,
         temp_riders = 0,
         groups = 0;

      while (groups < N)
      {
         temp_riders += g[(start_index + groups) % N];
         if (temp_riders > k)
            break;

         riders = temp_riders;
         groups++;
      }

      if (groups == N)
         return riders * R;

      aryCoasters[array_index].array_index = array_index;
      aryCoasters[array_index].start_index = start_index;
      aryCoasters[array_index].riders = riders;
      mapCoasters[start_index] = &aryCoasters[array_index];

      array_index++;
      start_index = (start_index + groups) % N;
   }

   __int64
      riders = 0;

   if (array_index == R)
   {
      for (int i = 0; i < R; i++)
         riders += aryCoasters[i].riders;

      return riders;
   }

   int
      i;

   for (i = 0; i < iter->second->array_index; i++)
      riders += aryCoasters[i].riders;

   R -= i;

   __int64
      cycle_riders = 0;

   for (; i < array_index; i++)
      cycle_riders += aryCoasters[i].riders;

   int
      cycles = R / (array_index - iter->second->array_index);

   riders += cycles * cycle_riders;
   R -= cycles * (array_index - iter->second->array_index);

   for (i = 0; i < R; i++)
      riders += aryCoasters[iter->second->array_index + i].riders;

   return riders;
}

int main(int argc, char *argv[])
{
   int
      T;

   FILE
      *fpi = fopen("C-small.in", "r"),
      *fpo = fopen("C-small.out", "w");

   fscanf(fpi, "%d", &T);
   for (int i = 0; i < T; i++)
      fprintf(fpo, "Case #%d: %I64d\n", i + 1, process_case(fpi));

   fclose(fpi);
   fclose(fpo);
   return 0;
}
