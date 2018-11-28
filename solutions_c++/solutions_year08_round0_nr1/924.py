#include <stdio.h> //printf(), scanf(), getchar()
#include <stdlib.h> //malloc(), free()
#include <string.h>
//#include <vector>
//#include <math.h>

#define INPUT_LARGE

struct engine
{
   char name[101];
   unsigned int num;
};

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
      unsigned int S,Q;
      fscanf(in,"%u\n",&S);

      engine* field=(engine*)malloc(S*sizeof(engine));

      for (unsigned int s=0;s<S;s++)
      {
         fscanf(in,"%[^\n]\n",field[s].name);
         field[s].num=0;
      }

      fscanf(in,"%u\n",&Q);

      char name[101];

      unsigned int* line=(unsigned int*)malloc(Q*sizeof(unsigned int));
      memset(line,255,Q);

      bool* cans=(bool*)malloc(S*sizeof(unsigned int));
      memset(cans,1,S);

      unsigned int lMin=0;
      unsigned int lCan=S;

      for (unsigned int q=0;q<Q;q++)
      {
         fscanf(in,"%[^\n]\n",name);
         for (unsigned int s=0;s<S;s++)
         {
            if (strcmp(field[s].name,name)==0) {
               line[q]=s;
               //break;
            }
         }
         if (cans[line[q]]) {
            cans[line[q]]=false;
            lCan--;
            if (!lCan)
            {
               lMin++;
               lCan=S-1;
               memset(cans,1,S);
               cans[line[q]]=false;
            }
         }
      }

      free(field);
      free(line);
      free(cans);

      fprintf(out,"Case #%u: %u\n",n+1,lMin);

   }

   fclose(in);
   fclose(out);

   return 0;
}