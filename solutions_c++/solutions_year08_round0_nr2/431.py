#include <stdio.h>
#include <conio.h>
#include <string.h>
#include <math.h>

   struct sched {
      float from;
      float at;
      bool over;
   };


   int tt , hf,mf,ht,mt;
   int ab, ba , na, nb;
   sched a[100], b[100], tmp;



int main()
{
   FILE *in, *out;
   int c, cn;

   int i, j, pos;
   float min;




   in = fopen("B-small.in", "rt");
   out = fopen("B-small.out", "wt");

   fscanf(in, "%d", &c);
   for (cn=1; cn<=c; cn++) {
      fscanf(in, "%d", &tt);
      fscanf(in, "%d%d", &ab, &ba);

      for (i=0; i<ab; i++) {
          fscanf(in,"%d:%d%d:%d",&hf, &mf, &ht, &mt);
          a[i].from=(float)hf+(float)mf/60;
          a[i].at=ht+((float)mt+(float)tt)/60;
          a[i].over=false;
      }
      for (i=0; i<ba; i++) {
          fscanf(in,"%d:%d%d:%d",&hf, &mf, &ht, &mt);
          b[i].from=(float)hf+(float)mf/60;
          b[i].at=(float)ht+((float)mt+(float)tt)/60;
          b[i].over=false;;
      }

      na=ab; nb=ba;


      for (i=0; i<ab; i++) {
        min=a[i].at;
        pos=i;
        for (j=i+1; j<ab; j++) {
          if (a[j].at<min) {min=a[j].at;pos=j;}
        }
        tmp=a[pos];
        a[pos]=a[i];
        a[i]=tmp;
      }

      for (i=0; i<ba; i++) {
        min=b[i].from;
        pos=i;
        for (j=i+1; j<ba; j++) {
          if (b[j].from<min) {min=b[j].from;pos=j;}
        }
        tmp=b[pos];
        b[pos]=b[i];
        b[i]=tmp;
      }

      for (i=0; i<ab; i++) {
         for (j=0; j<ba; j++) {
           if (b[j].from>=a[i].at && b[j].over==false) {b[j].over=true; nb--; break;}
         }
      }


      for (i=0; i<ab; i++) {
        min=a[i].from;
        pos=i;
        for (j=i+1; j<ab; j++) {
          if (a[j].from<min) {min=a[j].from;pos=j;}
        }
        tmp=a[pos];
        a[pos]=a[i];
        a[i]=tmp;
      }

      for (i=0; i<ba; i++) {
        min=b[i].at;
        pos=i;
        for (j=i+1; j<ba; j++) {
          if (b[j].at<min) {min=b[j].at;pos=j;}
        }
        tmp=b[pos];
        b[pos]=b[i];
        b[i]=tmp;
      }

      for (i=0; i<ba; i++) {
         for (j=0; j<ab; j++) {
           if (a[j].from>=b[i].at && a[j].over==false) {a[j].over=true; na--; break;}
         }
      }

      fprintf(out,"Case #%d: %d %d\n",cn,na, nb);

   }


   fclose(in);
   fclose(out);
   return 0;
}


