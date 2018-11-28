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


        int L,N,C;
        unsigned long int t;
        std::scanf("%d%ld%d%d", &L,&t,&N,&C);

        std::vector<int> as (C);
        for(int j = 0; j < C; j++){
            int ai;
            std::scanf("%d", &ai);
            as[j] = ai;
        }

        std::vector<int> distanceVec (N+1);
        int counter = 0;
        distanceVec[0] = 0;
        for(int j = 1; j < N+1; j++){
            distanceVec[j] = distanceVec[j-1]+as[counter];
            counter++;
            if(counter == as.size()){
                counter = 0;
            }
        }

        unsigned long int time = distanceVec[N]*2;
        int dReady = t/2;
        int boostersLeft = L;
        int startPos = 0;
        int fracD = 0;
        for(int j = 0; j < N+1; j++){
            if(distanceVec[j]>=dReady){
                startPos = j;
                fracD = distanceVec[j]-dReady;
                break;
            }
        }
        std::vector<bool> booster(N+1,false);
        as.push_back(fracD);
        std::sort(as.begin(),as.end());
        std::vector<int>::iterator it = as.end() - 1;
        while(boostersLeft > 0){
            if(*it==fracD){
                booster[startPos-1] = true;
                boostersLeft--;
                time -= fracD;
            }
            else{
                for(int j = startPos + 1; j < N+1; j++){
                    int dist = distanceVec[j]-distanceVec[j-1];
                    if(dist == *it){
                        booster[j] = true;
                        boostersLeft--;
                        time -= dist;
                        if(boostersLeft == 0){
                            break;
                        }
                    }
                }
            }

            it--;

        }
         std::printf("Case #%d: %ld\n", i+1, time);

    }

    return 0;

}

