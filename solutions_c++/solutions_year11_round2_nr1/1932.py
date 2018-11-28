#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>

struct Team{
    double WP;
    double OWP;
    double OOWP;
};

int main(){

    std::freopen("large.in", "r", stdin);
    std::freopen("large.out", "w", stdout);

    int t;
    std::scanf("%d", &t);

    for(int i = 0; i < t; i++){

        int N;
        std::scanf("%d\n", &N);

        std::map<int,Team> teams;
        char s[N][N];

        for(int j = 0; j < N; j++){
            Team t;
            int wins = 0;
            int played = 0;
            for(int k = 0; k < N; k++){
                char c;
                if(k == N-1){
                    std::scanf("%c\n",&c);
                }
                else{
                    std::scanf("%c",&c);
                }
                s[j][k] = c;
                if(c == '1'){
                    wins++;
                }
                if(c != '.'){
                    played++;
                }

            }
            t.WP = static_cast<double>(wins)/static_cast<double>(played);
            teams[j] = t;
        }

        for(int j = 0; j < N; j++){
            int opps = 0;
            double opWps = 0;
            for(int k = 0; k < N; k++){
                if(k != j){
                    if(s[j][k] != '.'){

                        int wins = 0;
                        int played = 0;
                        for(int l = 0; l < N; l++){
                            if(l != j){
                                if(s[k][l] == '1'){
                                    wins++;
                                }
                                if(s[k][l] != '.'){
                                    played++;
                                }
                            }
                        }
                        opps++;
                        opWps += static_cast<double>(wins)/static_cast<double>(played);

                    }
                }
            }
            teams[j].OWP = opWps/static_cast<double>(opps);
        }

        for(int j = 0; j < N; j++){
            double opsOWP = 0;
            int numOps = 0;
            for(int k = 0; k < N; k++){
                if(j != k){
                    if(s[j][k]!='.'){
                        opsOWP += teams[k].OWP;
                        numOps++;
                    }
                }
            }
            teams[j].OOWP = opsOWP/static_cast<double>(numOps);
        }

        std::printf("Case #%d:\n", i+1);

        for(int j = 0; j < N; j++){
            double RPI = 0.25*teams[j].WP + 0.50*teams[j].OWP + 0.25*teams[j].OOWP;
            std::printf("%.9f\n", RPI);
        }


    }

    return 0;

}

