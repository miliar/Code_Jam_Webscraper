/* 
 * File:   main.cpp
 * Author: nico
 *
 * Created on 8. Mai 2010, 11:20
 */

#include <stdlib.h>
#include <deque>
#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
/*
 * 
 */

int main(int argc, char** argv) {
    unsigned long R, k, M;
    M = 0;
    int Cases, N;
    FILE* in = fopen("C-large.in", "r");
    FILE* out = fopen("C-large.out", "w");
    fscanf(in, "%d", &Cases);
    for(int i=0; i<Cases;++i){
        fscanf(in, "%lu %lu %d", &R, &k, &N);
        int g[N];
        for(int j=0; j<N; ++j){
            fscanf(in, "%u", &g[j]);
        }
        unsigned long kl = k;
        unsigned int l=0;
        unsigned long table[N];
        int gc[N];
        memset(table, 0, N*sizeof(long));
        M = 0;
        for(int j=0; j<R; ++j){
            int c = 0;
            if(table[l] > 0){
                M += table[l];
                l += gc[l];
                l %= N;
                continue;
            }
            int s = l;
            while(kl >= g[l%N] && c < N){
                l %= N;
                kl -= g[l];
                ++l;
                ++c;
            }
            l %= N;
            gc[s] = c;
            table[s] = k-kl;
            M += k-kl;
            kl = k;
        }
        fprintf(out, "Case #%i: %lu\n",i+1,M);
        M = 0;
    }
    return (EXIT_SUCCESS);
}

