#include <cstdio>
#include <cstdlib>
#include <cmath>
using namespace std;

FILE *fout = fopen ("c.out", "w");

void work (int num){
     int n;
     int x[50], y[50], r[50];
     scanf ("%d", &n);
     for (int i = 0; i < n; i ++){
         scanf ("%d", &x[i]);
         scanf ("%d", &y[i]);
         scanf ("%d", &r[i]);
     }
     if (n == 1){
           fprintf (fout, "Case #%d: %lf\n", num, (double)r[0]);
           return;
        }
     if (n == 2){
           int re = r[0];
           if (r[1] > re){
                    re = r[1];
                    }
           fprintf (fout, "Case #%d: %lf\n", num, (double)re);
           return;
        }
     double re = 10000.0;
     double temp_re = 0.0;
     double calc;
     if (r[0] > temp_re){
              temp_re = (double) r[0];
              }
     calc = (r[1] + r[2] + sqrt ((x[1] - x[2]) * (x[1] - x[2]) + (y[1] - y[2])*(y[1] - y[2]))) / 2.0;
     if (calc > temp_re){
              temp_re = calc;
              }
     if (temp_re < re){
                 re = temp_re;
                 }
     temp_re = 0.0; 
     if (r[1] > temp_re){
              temp_re = (double) r[1];
              }
     calc = (r[0] + r[2] + sqrt ((x[0] - x[2]) * (x[0] - x[2]) + (y[0] - y[2])*(y[0] - y[2]))) / 2.0;
     if (calc > temp_re){
              temp_re = calc;
              }
     if (temp_re < re){
                 re = temp_re;
                 }
     temp_re = 0.0;                 
     if (r[2] > temp_re){
              temp_re = (double) r[2];
              }
     calc = (r[1] + r[0] + sqrt ((x[1] - x[0]) * (x[1] - x[0]) + (y[1] - y[0])*(y[1] - y[0]))) / 2.0;
     if (calc > temp_re){
              temp_re = calc;
              }
     if (temp_re < re){
                 re = temp_re;
                 }
     fprintf (fout, "Case #%d: %lf\n", num, re);
     return;
}

int main (){
    int c;
    scanf ("%d", &c);
    for (int i = 0; i < c; i ++){
        work (i + 1);
    }
    return 0;
}
