#include <cstdio>
#define MAXW 1005

int leftpoint[MAXW];
int rightpoint[MAXW];
int N;
int T;
int intersect;

FILE *inputfile = fopen("A-small.in", "r");
FILE *outputfile = fopen("A-small.out", "w");

int main(){
    fscanf(inputfile, "%d", &T);
    for (int foo = 1; foo <= T; foo++){
        fscanf(inputfile, "%d", &N);
        intersect = 0;
        for (int bar = 0; bar < N; bar++){
            fscanf(inputfile, "%d %d", &leftpoint[bar], &rightpoint[bar]);
            for (int baz = 0; baz < bar; baz++){
                if ((leftpoint[bar] < leftpoint[baz] && rightpoint[bar] > rightpoint[baz])
                    || (leftpoint[bar] > leftpoint[baz] && rightpoint[bar] < rightpoint[baz])){
                    intersect++;
                }
            }
        }
        fprintf(outputfile, "Case #%d: %d\n", foo, intersect);
    }
    return 0;
}

