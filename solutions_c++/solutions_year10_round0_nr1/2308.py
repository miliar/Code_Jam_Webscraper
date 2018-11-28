#include <cstdio>
#include <cstdlib>

FILE * fin = fopen ("A-large.in", "r"), * fout = fopen ("a-large.out", "w");

void work (int t){
    fprintf (fout, "Case #%d: ", t);
    int n, k;
    fscanf (fin, "%d%d", &n, &k);
    int tmp = (1 << n) - 1;
    if ((k & tmp) == tmp) fprintf (fout, "ON\n");
    else fprintf (fout, "OFF\n");
    return;
}

int main (){
    int N;
    fscanf (fin, "%d", &N);
    for (int i = 0; i < N; i ++){
        work (i + 1);
    }
    return 0;
}
