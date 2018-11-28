#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <cmath>
#include <map>
#include <string>
#include <algorithm>

std::string reverseString(const std::string& s){
    std::string ret;

    for(int i = s.size()-1; i >= 0; i--){
        ret.push_back(s[i]);
    }

    return ret;
}

int main(){

    std::freopen("large.in", "r", stdin);
    std::freopen("large.out", "w", stdout);

    int T;
    std::scanf("%d", &T);

    for(int i = 0; i < T; i++){

        int C;
        std::scanf("%d", &C);

        std::map<std::string,char> nonBaseElements;

        for(int j = 0; j < C; j++){
            char b1;
            char b2;
            char nb;
            std::scanf(" %c%c%c",&b1,&b2,&nb);
            std::string beComb;
            beComb.push_back(b1);
            beComb.push_back(b2);
            nonBaseElements[beComb] = nb;
            nonBaseElements[reverseString(beComb)] = nb;
        }

        int D;
        std::scanf("%d", &D);

        std::vector<std::string> opposingElements;

        for(int j = 0; j < D; j++){
            char b1;
            char b2;
            std::scanf(" %c%c", &b1, &b2);
            std::string opp;
            opp.push_back(b1);
            opp.push_back(b2);
            opposingElements.push_back(opp);
            opposingElements.push_back(reverseString(opp));
        }

        int N;
        std::scanf("%d ", &N);

        std::vector<char> seq;

        for(int j = 0; j < N; j++){
            char element;
            std::scanf("%c", &element);
            seq.push_back(element);
        }

        std::vector<char> output;
        for(int j = 0; j < seq.size(); j++){
            char element = seq[j];
            if(output.size() == 0){
                output.push_back(element);
            }
            else{
                bool didSomething = false;
                std::string last2;
                last2.push_back(output.back());
                last2.push_back(element);
                if(nonBaseElements.count(last2) > 0){
                    *(output.end()-1) = nonBaseElements[last2];
                    didSomething = true;
                }
                else{
                    for(int k = 0; k < output.size(); k++){
                        std::string comb;
                        comb.push_back(output[k]);
                        comb.push_back(element);
                        if(std::find(opposingElements.begin(),opposingElements.end(),comb) != opposingElements.end()){
                            output.clear();
                            didSomething = true;
                        }
                    }
                }
                if(!didSomething){
                    output.push_back(element);
                }
            }

        }

        std::printf("Case #%d: [", i+1);
        for(int j = 0; j < output.size(); j++){
            if(j == output.size() -1){
                std::printf("%c",output[j]);
            }
            else{
                std::printf("%c, ", output[j]);
            }
        }
        std::printf("]\n");

    }

    return 0;

}

