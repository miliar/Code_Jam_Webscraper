#include <cstdio>
#include <cstdlib>

FILE * fin = fopen ("A-large.in", "r"), * fout = fopen ("A-large.out", "w");

void work (){
     int n;
     fscanf (fin, "%d", &n);
     int x[1000], y[1000];
     for (int i = 0; i < n; i ++){
         fscanf (fin, "%d%d", &x[i], &y[i]);
     }
     int inter = 0;
     for (int i = 0; i < n; i ++){
         for (int j = i + 1; j < n; j ++){
             if ((x[i] - x[j]) * (y[i] - y[j]) < 0){
                       inter ++;
             }
         }
     }
     fprintf (fout, "%d\n", inter);
     return;
}

int main (){
    int n;
    fscanf (fin, "%d", &n);
    for (int i = 0; i < n; i ++){
        fprintf (fout, "Case #%d: ", i + 1);
        work ();
    }
    return 0;
}
