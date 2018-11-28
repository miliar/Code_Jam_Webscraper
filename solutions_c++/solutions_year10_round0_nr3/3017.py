// Fair Warning

#include <cstdio>
using namespace std;

int main(){
    int T, R, k, N;
    int g[1024], load[1024], next[1024], visited[1024], seq[1024];
    int i, j, h, income, n_seq, weight, cycle;

    FILE *fin, *fout;

    fin = fopen("C-small-attempt2.in", "r");
    fout = fopen("C-small-attempt2.out", "w");

    if(fin==NULL || fout==NULL){
        printf(" input errors\n");
        return 1;
    }

    fscanf(fin, "%d", &T);
    printf(" read T\n");
    for(i=0; i<T; i++){
//        printf(" read data\n");
        fscanf(fin, "%d %d %d", &R, &k, &N);
        for(j=0; j<N; j++)
            fscanf(fin, "%d", &g[j]);
//        printf(" gen graph\n");
        for(j=0; j<N; j++){
            load[j] = 0;
            for(h=j; load[j]+g[h%N] <= k && h-j<N; h++)
                load[j] += g[h%N];
            if(h == j)
                next[j] = -1;
            else
                next[j] = h%N;
        }
/*         income = 0;
 *         h = 0;
 *         for(j=0; j<R; j++){
 *             income += load[h];
 *             h = next[h];
 *             if(h == -1)
 *                 break;
 *         }
 *         fprintf(fout, ".Case #%d: %d\n", i+1, income);
 */
        
        for(j=0; j<N; j++){
            visited[j] = -1;
            seq[j] = -1;
        }
        n_seq = 0;
        h = 0;
        do{
            visited[h] = n_seq;
            seq[n_seq++] = h;
            h = next[h];
        }while(h != -1 && visited[h]==-1);
        if(h == -1){
            cycle = 0;
            income = 0;
            for(j=0; j<(R>n_seq? n_seq: R); j++){
                income += load[seq[j]];
            }
            fprintf(fout, "Case #%d: %d\n", i+1, income);
            continue;
        }
        else{
            cycle = n_seq - visited[h];
            weight = 0;
            income = 0;
            for(j=visited[h]; j<n_seq; j++)
                weight += load[seq[j]];
//            printf(" weight %d\n", weight);
            for(j=0; j<visited[h] && R>0; j++, R--)
                income += load[seq[j]];
            income += R/cycle*weight;
            R %= cycle;
            for(j=visited[h]; j<visited[h]+R; j++)
                income += load[seq[j]];
            fprintf(fout, "Case #%d: %d\n", i+1, income);
        }
    }

    fclose(fin);
    fclose(fout);

    return 0;
}
