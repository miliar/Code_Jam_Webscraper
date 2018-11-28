#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <cmath>

int main(){

    std::freopen("small.in", "r", stdin);
    std::freopen("small.out", "w", stdout);

    int T;
    std::scanf("%d", &T);

    for(int i = 0; i < T; i++){

        int N,L,H;
        std::scanf("%d%d%d", &N, &L, &H);

        std::vector<int> freqs (N);
        for(int j = 0; j < N; j++){
            int f;
            std::scanf("%d", &f);
            freqs[j] = f;
        }

        bool possible = false;
        int ansFreq = 0;


        for(int j = L; j <= H; j++){
            int f = j;
            bool fPos = true;
            for(int k = 0; k < N; k++){
                if((freqs[k] % f != 0) && (f % freqs[k] != 0)){
                    fPos = false;
                    break;
                }
            }
            if(fPos == true){
                possible = true;
                ansFreq = f;
                break;
            }
        }

        std::printf("Case #%d: ", i+1);
        if(possible){
            std::printf("%d",ansFreq);
        }
        else{
            std::printf("NO");
        }
        std::printf("\n");


    }

    return 0;

}

