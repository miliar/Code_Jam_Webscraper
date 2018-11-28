#include <stdio.h>
#include <string.h>
#define NMAX 200


char a[NMAX][NMAX],b[NMAX][NMAX];
int nr_teste,nr_motoare,contor,i,nr_cautari,v[NMAX],j,schimbari,suma;


int main()
  {FILE *f,*g;

   f=fopen("univers.in","r");
   g=fopen("univers.out","w");

   fscanf(f,"%d",&nr_teste);
   for (contor=1;contor<=nr_teste;contor++)
       {fscanf(f,"%d\n",&nr_motoare);
        for (i=0;i<nr_motoare;i++)
           fgets(a[i],NMAX,f);
        fscanf(f,"%d\n",&nr_cautari);
        for (i=0;i<nr_cautari;i++)
           fgets(b[i],NMAX,f);

        for (i=0;i<nr_motoare;i++)
              v[i]=0;

        schimbari=0;
        for (i=0;i<nr_cautari;i++)
           {suma=0;
            for (j=0;j<nr_motoare;j++)
                suma+=v[j];
            if (suma==nr_motoare-1) {for (j=0;j<nr_motoare;j++) v[j]=0;
                                     schimbari++;
                                     }
            for (j=0;j<nr_motoare;j++)
               if (strcmp(b[i],a[j])==0) {v[j]=1;j=nr_motoare;}
            }

        fprintf(g,"Case #%d: %d",contor,schimbari);

        }

   return 0;
   }
