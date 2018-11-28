/* 
 * File:   main.cpp
 * Author: nico
 *
 * Created on 23. Mai 2010, 10:55
 */

#include <stdlib.h>
#include <stdio.h>

/*
 * 
 */
bool solve(int x1, int y1, int x2, int y2){
    y1 -= x1;
    y2 -= x2;
    float tmp = y1 - y2;
    if (tmp == 0.0f) return false;
    float tmp2 = x2 - x1;
    tmp2 /= tmp;
    return (tmp2 > 0.0f && tmp2 < 1.0f);
}

int main(int argc, char** argv) {
    FILE* in = fopen("A-large.in", "r");
    FILE* out = fopen("A-large.out", "w");
    int Cases = 0;
    int count = 0;
    fscanf(in, "%d", &Cases);
    int N;
    for(int i=0; i<Cases;++i){
            fscanf(in, "%d", &N);
            int A[N];
            int B[N];
            for(int j=0; j<N; ++j) fscanf(in, "%d %d", &A[j], &B[j]);

            for(int j=0; j<N; ++j){
                for(int k=j; k<N; ++k){
                    if(j == k) continue;
                    if(solve(A[j], B[j], A[k], B[k])) ++count;
                }
            }
            fprintf(out, "Case #%d: %d\n", i+1, count);
            count = 0;
    }
    fclose(out);
    fclose(in);
    return (EXIT_SUCCESS);
}

