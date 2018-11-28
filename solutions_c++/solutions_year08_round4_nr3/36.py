#include <iostream>
#include <algorithm>

using namespace std;

#define MAX 1001

int N;
int X[MAX];
int Y[MAX];
int Z[MAX];
int P[MAX];

bool test(double power) {
    double dims[8];

    for(int i=0;i<8;++i) {
        dims[i] = 1e100;
    };

    for(int i=0;i<N;++i) {
        double d = power * P[i];
        for(int x=-1;x<=1;x+=2) {
            for(int y=-1;y<=1;y+=2) {
                for(int z=-1;z<=1;z+=2) {
                    dims[(x+1)/2 + (y+1)/2*2 + (z+1)/2*4] =
                        min(dims[(x+1)/2 + (y+1)/2*2 + (z+1)/2*4], 
                                X[i]*x + Y[i]*y + Z[i]*z + d);
                    if(-dims[(-x+1)/2 + (-y+1)/2*2 + (-z+1)/2*4] >= dims[(x+1)/2 + (y+1)/2*2 + (z+1)/2*4]) {
                        return false;
                    }
                }
            }
        }
    }
    return true;
}

int main(void) {
    int T;
    scanf("%d", &T);
    for(int t=1;t<=T;++t) {


        scanf("%d", &N);

        for(int i=0;i<N;++i) {
            scanf("%d%d%d%d", X+i, Y+i, Z+i, P+i);
        }

        double fim = 1.0;

        while(not test(fim)) {
            fim = fim * 2.0;
        }

        double inicio = 0;
        for(int i=0;i<200;++i) {
            double meio = (inicio + fim) / 2;
            if(not test(meio)) {
                inicio = meio;
            } else {
                fim = meio;
            }
        }

        printf("Case #%d: ", t);
        printf("%.7lf", fim);
        printf("\n");
    }
    return 0;
}
