/* 
 * File:   main.cpp
 * Author: nico
 *
 * Created on 22. Mai 2010, 18:52
 */

#include <stdlib.h>
#include <stdio.h>
/*
 * 
 */
int main(int argc, char** argv) {
    FILE* in = fopen("B-large.in", "r");
    FILE* out = fopen("B-large.out", "w");
    int Cases = 0;
    long B;
    int count = -1;
    int N, K, T;
    int ei = 0;
    fscanf(in, "%d", &Cases);
    for(int i=0; i<Cases;++i){
        count = 0;
        fscanf(in, "%d %d %Ld %d", &N, &K, &B, &T);
        int X[N];
        for(int j=0; j<N; ++j){
            fscanf(in, "%d", &X[j]);
        }
        long V[N];
        for(int j=0; j<N; j++){
            fscanf(in, "%Ld", &V[j]);
            X[j] += V[j] * T;
        }
        ei = N-1;
        int tmpcount = 0;
        while(K > 0){
            if(X[ei--] >= B){
                --K;
                count += tmpcount;
            }
            else{
                int tmp = ei;
                while(tmp > -1){
                    if(X[tmp] >= B) break;
                    --tmp;
                }
                tmpcount += 1+ei - tmp;
                if(tmp < 0){
                    count = -1;
                    break;
                }
                else ei = tmp;
            }
        }
        if(count == -1) fprintf(out, "Case #%d: %s\n", i+1, "IMPOSSIBLE");
        else fprintf(out, "Case #%d: %d\n", i+1, count);
    }
    fclose(out);
    fclose(in);
    return (EXIT_SUCCESS);
}

