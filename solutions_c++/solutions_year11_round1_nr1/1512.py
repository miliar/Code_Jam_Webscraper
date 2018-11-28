#include <cstdio>
#include <iostream>
#include <vector>

void getCommonFraction(int percentage, int* num, int* den){

    //Find highest common factor which goes into percentage & 100
    int factorsOf100[] = {1,2,4,5,10,20,25,50,100};
    int nFactorsOf100 = 9;

    int highestCommonFactor = 0;

    for(int i = nFactorsOf100-1; i > -1; i--){

        if(percentage % factorsOf100[i] == 0){
            highestCommonFactor = factorsOf100[i];
            break;
        }

    }

    *num = percentage/highestCommonFactor;
    *den = 100/highestCommonFactor;

}

int main(){

    std::freopen("small.in", "r", stdin);
    std::freopen("small.out", "w", stdout);

    int t;
    std::scanf("%d", &t);

    for(int i = 0; i < t; i++){

        int N, Pd, Pg;
        std::scanf("%d %d %d", &N, &Pd, &Pg);

        int num, den;
        getCommonFraction(Pd,&num,&den);

        bool possible = false;

        if(den <= N){
            possible = true;
            if(Pd < 100 && Pg == 100){
                possible = false;
            }
            if(Pd > 0 && Pg == 0){
                possible = false;
            }
        }

        std::printf("Case #%d: ", i+1);

        if(possible){
            std::printf("Possible");
        }
        else{
            std::printf("Broken");
        }

        std::printf("\n");

    }

    return 0;

}

