#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <cmath>
#include <map>
#include <string>
#include <algorithm>

class Combination{

    public:

    int n;
    int k;
    std::vector<int> comb;

    Combination(int an, int ak) : n(an), k(ak), comb(k) {
        for(int i = 0; i < k; i++){
            comb[i] = i;
        }
    }

    bool nextComb(){
        if(comb[0] == n - k){
            return false;
        }

        int i = 0;
        for(i = k - 1; i > 0 && comb[i] == n - k + i; --i) {}

        comb[i]++;

        for(int j = i; j < k-1; j++){
            comb[j+1] = comb[j] + 1;
        }

        return true;

    }

};

int badAdd(int a, int b){

    int c = a | b;
    int d = a & b;

    return c - d;

}

int main(){

    std::freopen("small.in", "r", stdin);
    std::freopen("small.out", "w", stdout);

    int T;
    std::scanf("%d", &T);

    for(int i = 0; i < T; i++){

        int N;
        std::scanf("%d", &N);

        std::vector<unsigned int> candyValues (N,0);

        for(int j = 0; j < N; j++){
            int Ci;
            std::scanf("%d", &Ci);
            candyValues[j] = Ci;
        }

        std::sort(candyValues.begin(), candyValues.end());

        bool possible = false;
        int seanMax = 0;

        for(int j = 1; j < N; j++){

            Combination c(N,j);

            do{

                int patrickBadValue = 0;
                int seanBadValue = 0;
                int seanRealValue = 0;

                for(int k = 0; k < N; k++){
                    if(std::find(c.comb.begin(),c.comb.end(),k) != c.comb.end()){
                        patrickBadValue = badAdd(patrickBadValue,candyValues[k]);
                    }
                    else{
                        seanBadValue = badAdd(seanBadValue,candyValues[k]);
                        seanRealValue += candyValues[k];
                    }
                }

                if(seanBadValue == patrickBadValue){
                    possible = true;
                    if(seanRealValue > seanMax){
                        seanMax = seanRealValue;
                    }
                }

            } while( c.nextComb() );

        }

        std::printf("Case #%d: ", i+1);
        if(possible){
            std::printf("%d", seanMax);
        }
        else{
            std::printf("NO");
        }
        printf("\n");

    }


    return 0;
}
