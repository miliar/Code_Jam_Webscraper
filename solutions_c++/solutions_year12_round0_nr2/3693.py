#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int T,N,S,p;
// T = antal test
// N = antal googlers
// S = antal specialfall
// p = krävda poäng

bool compare(int i,int j) { return (i>j); }

int main(){
    cin >> T;
    for(int test=1 ; test<=T ; ++test){
        //----------------------------------------------------------------------
        cin >> N >> S >> p;
        vector<int> score;
        for (int i = 0; i < N; ++i){
            int tmp;
            cin >> tmp;
            score.push_back(tmp);
        }
        sort(score.begin(), score.end(), compare);
        //----------------------------------------------------------------------
        int res = 0;
        if(p==0){
            res=N;
        }else{
            for (int i = 0; i < N; ++i){
                //--------------------------------------------------------------
                // Om delbar på 3
                if(score[i]%3 == 0 && score[i]>=3){
                    if(div(score[i],3).quot >= p){
                        res++;
                    }else if(S>0 && div(score[i],3).quot+1 >= p){
                        res++;
                        S--;
                    }
                //--------------------------------------------------------------
                // Om ej delbar på 3
                }else{
                    div_t divres = div(score[i],3);
                    if(divres.rem == 1){
                        if(divres.quot+1>=p){
                            res++;
                        }
                    }else if(divres.rem == 2){
                        if(divres.quot+1>=p){
                            res++;
                        }else if(divres.quot+2>=p && S>0){
                            res++;
                            S--;
                        }
                    }
                }
                //--------------------------------------------------------------
            }
        }
        
        //----------------------------------------------------------------------
        cout << "Case #" << test << ": ";
        cout << res;
        cout << endl;
        //----------------------------------------------------------------------
    }
}
