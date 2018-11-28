#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main(int argc, char *argv[])
{
    FILE *inf = fopen("A-small.in","r");
    FILE *of = fopen("out.out","w");
    int T, N, K;
    long long int n;
    fscanf(inf,"%d\n",&T);
    for(int i=0;i<T;i++){
        fscanf(inf, "%d %d\n", &N, &K);
        n=1;
        for(int k = 0; k < N; k++)n*=2;
        if((K+1) % (n) == 0){
            fprintf(of,"Case #%d: ON\n", i+1);
        }else{
            fprintf(of,"Case #%d: OFF\n", i+1); 
        }
    }
    fclose(inf);fclose(of);
    return EXIT_SUCCESS;
}

