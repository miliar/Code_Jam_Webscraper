#include <cstdio>
#include <cstdlib>

FILE * fin = fopen ("B-large.in", "r"), *fout = fopen ("B-large.out", "w");

void work (){
     int n, k, b, t;
     fscanf (fin, "%d%d%d%d", &n, &k, &b, &t);
     int x[100];
     int v[100];
     int end[100];
     int need_swap = 0;
     bool done[100];
     for (int i = 0; i < n; i ++){
         done[i] = false;
         fscanf (fin, "%d", &x[i]);
     }
     for (int i = 0; i < n; i ++){
         fscanf (fin, "%d", &v[i]);
         end[i] = x[i] + v[i] * t;
         //fprintf (fout, "\n%d\n", end[i]);
     }
     int swap[100];
     int count = 0;
     for (int i = 0; i < n; i ++){
         swap[i] = 100;
         if (end[i] >= b){
            swap[i] = 0;
            count ++;
            for (int j = i + 1; j < n; j ++){
             if (end[j] < b)
                swap[i] ++;
            }
         }
     }
     if (count < k){
               fprintf (fout, "IMPOSSIBLE\n");
               return;
     }
     for (int i = 0; i < k; i ++){
         int min = 100;
         int argmin = 100;
         for (int j = 0; j < n; j ++){
             if (swap[j] < min && !done[j]){
                min = swap[j];
                argmin = j;
             }
         }
         done[argmin] = true;
         need_swap += swap[argmin];
     }
     fprintf (fout, "%d\n", need_swap);
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
