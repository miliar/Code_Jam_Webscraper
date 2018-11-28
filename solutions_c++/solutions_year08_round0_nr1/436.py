#include <stdio.h>
#include <conio.h>
#include <string.h>
#include <math.h>

int jumpAt(char eng[100][102], char que[1000][102] , int e,int q,int qs) {
  int nm, fs;
  int min, end;
  int en, qn;

     min=q; end=0;
     for (en=0; en<e; en++) {
          nm=0; fs=q;
          for (qn=qs; qn<q; qn++) {
            if (strcmp(eng[en],que[qn])==0) {
                nm++;
                if (fs==q) fs=qn;
            }
          }
          if (fs>=end) {
            min=nm;
            end=fs;
          }
      }
    return end;
}


int main()
{
   FILE *in, *out;
   int c, cn, e, en, q, qn;
   char eng[100][102],que[1000][102];
   int nxt, cyc, res;


   in = fopen("A-small.in", "rt");
   out = fopen("A-small.out", "wt");

   fscanf(in, "%d", &c);
   for (cn=1; cn<=c; cn++) {
       fscanf(in, "%d", &e);
      fscanf(in,"%[^\n]%*c",eng[0]);
      for (en=0; en<e; en++) {
          fscanf(in,"%[^\n]%*c",eng[en]);
      }
      fscanf(in, "%d", &q);
      fscanf(in,"%[^\n]%*c",que[0]);
      for (qn=0; qn<q; qn++) {
          fscanf(in,"%[^\n]%*c",que[qn]);
      }
      nxt=0; cyc=-1; res=0;
      while (res!=q) {
        res=jumpAt(eng, que, e, q, nxt);
        nxt=res;
        cyc++;
      };
      if (q==0) cyc=0;
      fprintf(out,"Case #%d: %d\n",cn,cyc);
   }


   fclose(in);
   fclose(out);
   return 0;
}


