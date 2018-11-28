#include <cstdio>
#include <cstdlib>

FILE * fin = fopen ("C-small-attempt0.in", "r"), * fout = fopen ("C-small.out", "w");

int c (int m, int n){
    int re = 1;
    for (int i = 0; i < n; i ++){
        re = re * (m - i) / (i + 1);
    }
    re = re % 100003;
    return re;
}

void work (){
     int n;
     fscanf (fin, "%d", &n);
     int f[500][500];
     for (int i = 2; i <= n; i ++){
         f[i][1] = 1;
         for (int j = 2; j < i; j ++){
             f[i][j] = 0;
             for (int k = 1; k < j; k ++){
                 f[i][j] = f[i][j] + c(i - j - 1, j - k - 1) * f[j][k];
                 f[i][j] = f[i][j] % 100003;
             }
             //printf ("%d %d: %d\n", i, j, f[i][j]);
         }
     }
     int re = 0;
     for (int i = 1; i < n; i ++){
         re += f[n][i];
         re = re % 100003;
     }
     fprintf (fout, "%d\n", re);
     return;
}

int main (){
    int n;
    fscanf (fin, "%d", &n);
    for (int i = 0; i < n; i ++){
        fprintf (fout, "Case #%d: ", i + 1);
        work ();
    }
    //system ("pause");
    return 0;
}
