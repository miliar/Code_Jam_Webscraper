#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

FILE
	*fpi = fopen("A-large.in", "r"),
	*fpo = fopen("A-large.out", "w");

int
   T;

int main(int argc, char *argv[])
{
	fscanf(fpi, "%d", &T);

	for (int i = 0; i < T; i++)
		{
      int
         N,
         W[100] = { 0 },
         L[100] = { 0 };

      char
         G[100][100];


      double
         WP[100],
         OWP[100],
         OOWP[100],
         RPI[100];

      char
         c;

		fscanf(fpi, "%d", &N);

      for (int j = 0; j < N; j++)
         {
         for (int k = 0; k < N; k++)
            {
            while (1)
               {
               fscanf(fpi, "%c", &c);
               if (c == '.' || c == '1' || c == '0')
                  break;
               }

            if (c == '0')
               L[j]++;
            else if (c == '1')
               W[j]++;

            G[j][k] = c;
            }

         WP[j] = (double)W[j] / (W[j] + L[j]);
         }

      for (int j = 0; j < N; j++)
         {
         double
            s = 0.0;

         int
            n = 0;

         for (int k = 0; k < N; k++)
            {
            if (j == k)
               continue;

            if (G[j][k] == '0')
               {
               s += ((double)W[k] - 1) / (W[k] + L[k] - 1);
               n++;
               }
            else if (G[j][k] == '1')
               {
               s += ((double)W[k]) / (W[k] + L[k] - 1);
               n++;
               }
            }

         OWP[j] = s / n;
         }

      for (int j = 0; j < N; j++)
         {
         double
            s = 0.0;

         int
            n = 0;

         for (int k = 0; k < N; k++)
            {
            if (j == k)
               continue;

            if (G[j][k] != '.')
               {
               s += OWP[k];
               n++;
               }
            }

         OOWP[j] = s / n;
         RPI[j] = 0.25 * WP[j] + 0.50 * OWP[j] + 0.25 * OOWP[j];
         }

		fprintf(fpo, "Case #%d:\n", i + 1);

      for (int j = 0; j < N; j++)
		   fprintf(fpo, "%.12lg\n", RPI[j]);
		}

	fclose(fpi);
	fclose(fpo);
	return 0;
}
