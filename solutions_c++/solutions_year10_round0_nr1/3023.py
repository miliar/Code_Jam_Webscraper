#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(int argc, char *argv[])
{
   int
      T,
      N,
      K,
      mask;

   FILE
      *fpi = fopen("A-large.in", "r"),
      *fpo = fopen("A-large.out", "w");

   fscanf(fpi, "%d", &T);
   for (int i = 0; i < T; i++)
   {
      fscanf(fpi, "%d", &N);
      fscanf(fpi, "%d", &K);
      mask = (1 << N) - 1;
      fprintf(fpo, "Case #%d: %s\n", i + 1, ((K & mask) == mask) ? "ON" : "OFF");
   }

   fclose(fpi);
   fclose(fpo);
   return 0;
}
