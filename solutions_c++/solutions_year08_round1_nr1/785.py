#include <stdio.h> //printf(), scanf(), getchar()
#include <stdlib.h> //malloc(), free()
//#include <string.h>
//#include <vector>
//#include <math.h>

//#define INPUT_LARGE

int one[1000];
int two[1000];

int compareasc(const void * a, const void * b)
{
  return ( *((int*)a) - *((int*)b) );
}

int comparedesc(const void * a, const void * b)
{
  return ( *((int*)b) - *((int*)a) );
}

int main(int argc, char **argv)
{

#ifdef INPUT_LARGE
   FILE* in=fopen("A-large.in","r");
   FILE* out=fopen("A-large.out","w");
#else
   FILE* in=fopen("A-small.in","r");
   FILE* out=fopen("A-small.out","w");
#endif

   unsigned int N;

   fscanf(in,"%u\n",&N);

   for (unsigned int n=0;n<N;n++)
   {

      unsigned int T;

      fscanf(in,"%u\n",&T);

      for (unsigned int i=0;i<T;i++)
         fscanf(in,"%u ",&one[i]);

      for (unsigned int i=0;i<T;i++)
         fscanf(in,"%u ",&two[i]);


      qsort(one,T,sizeof(int),&compareasc);
      qsort(two,T,sizeof(int),&comparedesc);


      int r=0;

      for (unsigned int i=0;i<T;i++)
         r+=one[i]*two[i];


      fprintf(out,"Case #%u: %d\n",n+1,r);
   }

   fclose(in);
   fclose(out);

   return 0;
}