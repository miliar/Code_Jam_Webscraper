#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <utility>

using namespace std;

int main() {
    int n;
    cin >> n;
    
    for(int z=1; z<=n; z++) {
        //Read inputs
        int N;
        cin >> N;
        
        vector<pair<int, int> > orange(0);
        vector<pair<int, int> > blue(0);
        
        for(int i=0; i<N; i++) {
            char bot;
            int value;
            cin >> bot >> value;
            if(bot == 'O') {
                orange.push_back(make_pair(i, value));
            } else { //bot == 'B'
                blue.push_back(make_pair(i, value));
            }
        }
        
        int cpt = 0;
        int curOr = 0;
        int curBl = 0;
        int posBlue = 1;
        int posOrange = 1;
        
        while(curOr < (int)orange.size() || curBl < (int)blue.size()) {
            
            if(curOr == (int)orange.size()) {
                for(int i=curBl; i<(int)blue.size(); i++) {
                    cpt += abs(blue[i].second-posBlue) + 1;
                    posBlue = blue[i].second;
                }
                break;
            } else if(curBl == (int)blue.size()) {
                for(int i=curOr; i<(int)orange.size(); i++) {
                    cpt += abs(orange[i].second-posOrange) + 1;
                    posOrange = orange[i].second;
                }
                break;
            }
            
            bool changeOr = false;
            if(posOrange != orange[curOr].second) {
                if(posOrange < orange[curOr].second) {
                    posOrange++;
                } else {
                    posOrange--;
                }
            } else {
                if(orange[curOr].first < blue[curBl].first) {
                    changeOr = true;
                }
            }
            
            if(posBlue != blue[curBl].second) {
                if(posBlue < blue[curBl].second) {
                    posBlue++;
                } else {
                    posBlue--;
                }
            } else {
                if(blue[curBl].first < orange[curOr].first) {
                    curBl++;
                }
            }
            
            if(changeOr) curOr++;
            
            cpt++;
        }
        
        //Print outputs
        printf("Case #%d: %d\n", z, cpt);
        
    }
    
    return 0;
};
