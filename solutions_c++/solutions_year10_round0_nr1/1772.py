/* 
 * File:   main.cpp
 * Author: nico
 *
 * Created on 8. Mai 2010, 10:34
 */

#include <stdlib.h>
#include <stdio.h>
#include <math.h>
using namespace std;
/*
 * 
 */
int main(int argc, char** argv) {
    unsigned long N, K;
    K = N = 0;
    int Cases;
    FILE* in = fopen("A-large.in", "r");
    FILE* out = fopen("A-large.out", "w");
    fscanf(in, "%d", &Cases);
    for(int i=0; i<Cases;++i){
        fscanf(in, "%d %d", &N, &K);
        N = pow(2, N);
        if((K%N) == N-1) fprintf(out, "Case #%i: ON\n",i+1);
        else fprintf(out, "Case #%i: OFF\n",i+1);
    }
    return (EXIT_SUCCESS);
}

