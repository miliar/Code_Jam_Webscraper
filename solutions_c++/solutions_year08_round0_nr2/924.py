#include <stdio.h> //printf(), scanf(), getchar()
#include <stdlib.h> //malloc(), free()
//#include <string.h>
#include <vector>
#include <math.h>

#define INPUT_LARGE

struct trip
{
   bool used;
   bool from;
   bool at;
   unsigned int start;
   unsigned int end;
   unsigned int index;
};

/*int compareAB(const void * a, const void * b)
{
  if (((trip*)a)->at && !((trip*)b)->at )
     return +1;
  if (!((trip*)a)->at && ((trip*)b)->at )
     return -1;
  return 0;
}

int compareABfrom(const void * a, const void * b)
{
  if (((trip*)a)->from && !((trip*)b)->from )
     return +1;
  if (!((trip*)a)->from && ((trip*)b)->from )
     return -1;
  return 0;
}*/

int comparestartasc(const void * a, const void * b)
{
  return ( ((trip*)a)->start - ((trip*)b)->start );
}

int compareenddesc(const void * a, const void * b)
{
  return ( ((trip*)b)->end - ((trip*)a)->end );
}

/*int compare2(const void * a, const void * b)
{
  return ( ((trip*)a)->end - ((trip*)b)->end );
}

int compareb2(const void * a, const void * b)
{
  return ( ((trip*)b)->start - ((trip*)a)->start );
}*/

int main(int argc, char **argv)
{

#ifdef INPUT_LARGE
   FILE* in=fopen("B-large.in","r");
   FILE* out=fopen("B-large.out","w");
#else
   FILE* in=fopen("B-small.in","r");
   FILE* out=fopen("B-small.out","w");
#endif

   unsigned int N;
   fscanf(in,"%u\n",&N);

   //trip* trips=NULL;

   for (unsigned int n=0;n<N;n++)
   {
      unsigned int T;
      fscanf(in,"%u\n",&T);

      unsigned int NA, NB;
      fscanf(in,"%u %u\n",&NA,&NB);

      //std::vector<trip> trips;

      trip* trips=(trip*)malloc((NA+NB)*sizeof(trip));
      trip* avails=(trip*)malloc((NA+NB)*sizeof(trip));
      //trips=(trip*)malloc((NA+NB)*sizeof(trip));
      //trips=(trip*)realloc(trips,(NA+NB)*sizeof(trip));

      //trip* lTrip;

      for (unsigned int na=0;na<NA;na++)
      {
         trips[na].used=true;
         trips[na].from=false;
         trips[na].at=true;

         unsigned int H, M;
         fscanf(in,"%u:%u ",&H,&M);
         trips[na].start=H*60+M;

         fscanf(in,"%u:%u\n",&H,&M);
         trips[na].end=H*60+M;
      }

      for (unsigned int nb=0;nb<NB;nb++)
      {
         trips[NA+nb].used=true;
         trips[NA+nb].from=true;
         trips[NA+nb].at=false;

         unsigned int H, M;
         fscanf(in,"%u:%u ",&H,&M);
         trips[NA+nb].start=H*60+M;

         fscanf(in,"%u:%u\n",&H,&M);
         trips[NA+nb].end=H*60+M;
      }

restart:
      unsigned int availsc=0;

      qsort(trips,NA+NB,sizeof(trip),&comparestartasc);

      for (unsigned int na=0;na<NA+NB;na++)
      {
         if (trips[na].used) {
            for (unsigned int nb=0;nb<NA+NB;nb++)
            {
               if (trips[nb].used && trips[nb].at==trips[na].from && trips[na].start>=trips[nb].end+T) {
                  avails[availsc].end=trips[nb].end;
                  avails[availsc].index=nb;
                  availsc++;
               }
            }
            if (availsc) {
               qsort(avails,availsc,sizeof(trip),&compareenddesc);

               trips[avails[0].index].end=trips[na].end;
               trips[avails[0].index].at=trips[na].at;
               trips[na].used=false;
               goto restart;
            }
         }
      }

      /*for (unsigned int i=0;i<(sqrt((float)(NA+NB))+1);i++)
      {
restarta:
         unsigned int lAt;

         qsort(trips,NA+NB,sizeof(trip),&compareAB);

         for (lAt=0;lAt<NA+NB;lAt++)
         {
            if (trips[lAt].at) break;
         }

         qsort(trips,lAt,sizeof(trip),&compare);
         qsort(&trips[lAt],NA+NB-lAt,sizeof(trip),&compareb);

         for (lAt=0;lAt<NA+NB;lAt++)
         {
            if (trips[lAt].at) break;
         }

         for (unsigned int na=0;na<NA+NB;na++)
         {
            if (trips[na].at) break;
            if (trips[na].used) {
               for (unsigned int nb=lAt;nb<NA+NB;nb++)
               {
                  if (trips[nb].used && trips[na].start>=trips[nb].end+T) {
                     trips[nb].end=trips[na].end;
                     trips[nb].at=!trips[nb].at;
                     trips[na].used=false;
                     goto restarta;
                  }
               }
            }
         }

restartb:
         qsort(trips,NA+NB,sizeof(trip),&compareAB);

         for (lAt=0;lAt<NA+NB;lAt++)
         {
            if (trips[lAt].at) break;
         }

         qsort(trips,lAt,sizeof(trip),&compareb2);
         qsort(&trips[lAt],NA+NB-lAt,sizeof(trip),&compare2);

         for (lAt=0;lAt<NA+NB;lAt++)
         {
            if (trips[lAt].at) break;
         }

         for (unsigned int nb=lAt;nb<NA+NB;nb++)
         {
            if (trips[nb].used) {
               for (unsigned int na=0;na<NA+NB;na++)
               {
                  if (trips[na].at) break;
                  if (trips[na].used && trips[nb].start>=trips[na].end+T) {
                     trips[na].end=trips[nb].end;
                     trips[na].at=!trips[na].at;
                     trips[nb].used=false;
                     goto restartb;
                  }
               }
            }
         }
      }
      qsort(trips,NA+NB,sizeof(trip),&compareAB);*/

      unsigned int lNA=0,lNB=0;

      for (unsigned int na=0;na<NA+NB;na++)
      {
         if (trips[na].used) {
            if (!trips[na].from)
               lNA++;
            else
               lNB++;
         }
      }

      free(trips);
      free(avails);

      fprintf(out,"Case #%u: %u %u\n",n+1,lNA,lNB);
   }

   fclose(in);
   fclose(out);

   return 0;
}