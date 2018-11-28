#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

int main(int argc, char** argv){
    ifstream inFile(argv[1]);
    ofstream outFile(argv[2]);
    
    int line;
    inFile >> line;
    
    for(int i = 0 ; i < line ; i++){
        int num, sup, p;
        inFile >> num >> sup >> p;
        int* g = new int[num];
        for(int j = 0 ; j < num ; j++)
            g[j] = 0;
            
        int ans = num;
        for(int j = 0 ; j < num ; j++){
            inFile >> g[j];
        }

        int minS = 0, maxS = num;        
        for(int j = 0 ; j < num ; j++){
            int a = g[j] - 3*p;
            if(g[j] == 0){
                if(p >= 1)
                    ans--;
                maxS--;
            }else if(g[j] == 1){
                if(p > 1)
                    ans--;
                maxS--;
            }else if(g[j] == 2){
                if(p == 2){
                    minS++;
                }else if(p > 2){
                    ans--;
                }
            }else if(g[j] == 3){
                if(p == 2){
                    minS++;
                }else if(p > 2){
                    ans--;
                }
            }else{
                if(a == -4 || a == -3){
                    minS++;
                }else if(a < -4){
                    ans--;
                }
            }
        }
        
        if(minS > sup)
            ans -= (minS - sup);
        if(maxS < sup)
            ans -= (sup - maxS);
        
        outFile << "Case #" << i+1 << ": "<< ans << endl;
        cout << ans << endl;
    }
}
