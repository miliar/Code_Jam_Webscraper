#include <cstdio>
#define MAXR 1005

FILE *input = fopen("C-small-attempt0.in", "r");
FILE *output = fopen("small.out", "w");

int T, R, k, N;
int groups[MAXR];

int main(){
    fscanf(input, "%d", &T);
    for (int foo = 0; foo < T; foo++){
        fscanf(input, "%d%d%d", &R, &k, &N);
        for (int bar = 0; bar < N; bar++){
            fscanf(input, "%d", &groups[bar]);
        }
        long long accum = 0, profit = 0, place = 0;
        int rides = 0, currgroups = 0;
        while (rides < R){
            if (accum + groups[place%N] > k){
                currgroups = 0;
                profit += accum;
                accum = 0;
                rides++;
            } else if (currgroups == N){
                currgroups = 0;
                profit += accum;
                rides++;
                accum = 0;
            } else {
                accum += groups[place%N];
                currgroups++;
                place++;
            }
        }
        fprintf(output, "Case #%d: %lld\n", foo+1, profit);
    }
    return 0;
}                 
         

