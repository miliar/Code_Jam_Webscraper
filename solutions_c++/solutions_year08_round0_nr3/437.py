#include <stdio.h>
#include <conio.h>
#include <string.h>
#include <math.h>

double f, R, t, r, g;


bool isDotIn(double x, double y) {
  double eq=(R-t-f-x)*(R-t-f+x);
  if (eq<0) return false;
  double res=sqrt(eq);
  if (y<res) return true;
  else return false;
}


double calcS(double x1, double x2, double dy) {
  double res=0;
  double x, dx=(x2-x1)/200000;
  for (x=x1; x<=x2; x+=dx) {
    if (isDotIn(x, dy))
        res+=dx*(sqrt((R-t-f-x)*(R-t-f+x))-dy);
  }
  return res;
}

double getInters(double x1, double x2, double dy) {
  double res=x1;
  double x, dx=(x2-x1)/100000;
  for (x=x1; x<=x2; x+=dx) {
    if (!isDotIn(x, dy))
        return x;
  }
  return res;
}


int main()
{
   FILE *in, *out;
   int c, cn;

   int i, j, pos;

   double x, y, Spass, Sall, prob, is;
   float f1, R1, t1, r1, g1;

   in = fopen("C-small.in", "rt");
   out = fopen("C-small.out", "wt");

   fscanf(in, "%d", &c);
   for (cn=1; cn<=c; cn++) {
      fscanf(in, "%f%f%f%f%f", &f1, &R1, &t1, &r1, &g1);
      f=f1;R=R1;t=t1;r=r1;g=g1;

      Spass=0; Sall=0;
      if (g>2*f) {
      for(x=r+f; x<R; x+=(g+2*r)) {
         for(y=r+f; y<R; y+=(g+2*r)) {
           if (isDotIn(x, y+(g-2*f)) && isDotIn(x+(g-2*f), y+(g-2*f)))
              Spass+=((g-2*f)*(g-2*f));
           else {

               is=getInters(x, x+(g-2*f), y+(g-2*f));
               Spass+=((is-x)*(g-2*f));
               Spass+=calcS(is, x+(g-2*f), y);
           }
              //Spass+=calcS(x, x+(g-2*f), y);

         }
      }
      }
      Spass*=4;
      Sall=M_PI*R*R;
      prob=1-Spass/Sall;
      if (prob<0) prob=0;
      fprintf(out,"Case #%d: %f\n",cn, prob);

   }


   fclose(in);
   fclose(out);
   return 0;
}


