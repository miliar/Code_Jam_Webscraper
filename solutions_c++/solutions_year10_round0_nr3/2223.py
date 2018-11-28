#include <cstdio>
#include <cstdlib>

FILE *fin = fopen ("C-small-attempt0.in", "r"), *fout = fopen ("C-small.out", "w");

void work (){
    int R, k, N;
    int g[1000];
    fscanf (fin, "%d%d%d", &R, &k, &N);
    for (int i = 0; i < N; i ++){
        fscanf (fin, "%d", &g[i]);
    }
    int head = 0;
    int account = 0;
    for (int i = 0; i < R; i ++){
        int sum = 0;
        for (int j = 0; j < N; j ++){
            if (sum + g[(head + j) % N] > k){
                head = (head + j) % N;
                break;
            }
            sum = sum + g[(head + j) % N];
        }
        account += sum;
    }
    fprintf (fout, "%d\n", account);
    return;
}

int main (){
    int T;
    fscanf (fin, "%d", &T);
    for (int i = 0; i < T; i ++){
        fprintf (fout, "Case #%d: ", i + 1);
        work ();
    }
    return 0;
}
