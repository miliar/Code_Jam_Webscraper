#include <cstdio>
#include <cmath>

FILE *input = fopen("A-large.in", "r");
FILE *output = fopen("large.out", "w");
int T, N, K;

int main(){
    fscanf(input, "%d", &T);
    for (int foo = 1; foo <= T; foo++){
        fscanf(input, "%d%d", &N, &K);
        if ((K+1)%(1<<N) == 0){
            fprintf(output,"Case #%d: ON\n", foo);
        } else {
            fprintf(output,"Case #%d: OFF\n", foo);
        }
    }
    return 0;
}
    
