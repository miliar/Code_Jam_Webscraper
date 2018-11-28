#include <stdio.h>
#include <conio.h>
#include <conio.h>
#include <string.h>
#include <math.h>







int main()
{
   FILE *in, *out;
   int c, cn, p, pn, k, kn, l, ln;
   int x[1000];
   int max, i, j, m, tmp, res;



   in = fopen("A-small.in", "rt");
   out = fopen("A-small.out", "wt");

   fscanf(in, "%d", &c);
   for (cn=1; cn<=c; cn++) {
       fscanf(in, "%d%d%d", &p, &k, &l);

       for (ln=0;ln<l;ln++)
         fscanf(in, "%d", &x[ln]);

       for (i=0; i<l; i++) {
        max=x[i];
        m=i;
        for (j=i+1; j<l; j++) {
          if (x[j]>max) {max=x[j];m=j;}
        }
        tmp=x[m];
        x[m]=x[i];
        x[i]=tmp;
      }

      res=0;
      for (ln=0; ln<l; ln++) {
        res+=x[ln]*(ln/k+1);
      }
      fprintf(out,"Case #%d: %d\n",cn,res);

   }


   fclose(in);
   fclose(out);
   return 0;
}

