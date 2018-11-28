// Snapper Chain

#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

int itoa(int n, char s[]){
    int i, sign;

    i = 0;
    do {
        s[i++] = n % 2 + '0';
    } while ((n /= 2) > 0);
    s[i] = '\0';
    return i;
 }
 
int main(){
    
    int N, K, nn, ii, i, L;
    char bin[64];
    FILE *fin, *fout;
    
    fin = fopen("A-large.in", "r");
    fout = fopen("A-large.out", "w");
    fscanf(fin, "%d", &nn);
    for(ii=0; ii<nn; ii++){
        fscanf(fin, "%d %d", &N, &K);
        K = K % (1<<N);
        L = itoa(K, bin);
//        printf("N %d K %d b %s\n", 1>>N, K, bin);
        for(i=0; i<N; i++){
            if(bin[i]=='0' || bin[i] == '\0')
                break;
        }
        if(i==N)
            fprintf(fout, "Case #%d: ON\n", ii+1);
        else
            fprintf(fout, "Case #%d: OFF\n", ii+1);
    }
    
    
    return 0;
}
