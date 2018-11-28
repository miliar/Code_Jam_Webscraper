#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <algorithm>
using namespace std;

int Normal_Scores[31];
int Suprising_Scores[31];
int T, N, S, P, G[101], R;
bool U[101];

void generate_triplets(void){
    for(int i = 0; i <= 30; i ++){
        Normal_Scores[i] = 0;
        Suprising_Scores[i] = 0;
    }

    for(int i = 0; i <= 10; i ++){
        for(int j = i; j <= 10; j ++){
            for(int l = j; l <= 10; l ++){
                if( (j - i) > 2 || (l - i) > 2 || (l - j) > 2 )
                    continue;
                if( (j - i) == 2 || (l - i) == 2 || (l - j) == 2 )
                    Suprising_Scores[(i+j+l)] = max(Suprising_Scores[(i+j+l)], max(i, max(j, l)));
                else
                    Normal_Scores[(i+j+l)] = max(Normal_Scores[(i+j+l)], max(i, max(j, l)));
            }
        }
    }

    return;
}

void dfs(int Count){
    if(Count == S){
        int Tops = 0;
        for(int i = 0; i < N; i ++){
            if(U[i]){
                if(Suprising_Scores[(G[i])] >= P){
                    Tops ++;
                }
            }
            else{
                if(Normal_Scores[(G[i])] >= P){
                    Tops ++;
                }
            }
        }
        if(Tops > R){
            R = Tops;
        }
    }
    else{
        for(int i = 0; i < N; i ++){
            if(!U[i]){
                U[i] = true;
                dfs(Count + 1);
                U[i] = false;
            }
        }
    }
    return;
}

int main(void){

    generate_triplets();

    cin >> T;
    for(int i = 1; i <= T; i ++){
        cin >> N >> S >> P;
        for(int j = 0; j < N; j ++){
            cin >> G[j];
            U[j] = false;
        }
        R = 0;
        dfs(0);
        cout << "Case #" << i << ": " << R << endl;
    }

    return 0;
}
