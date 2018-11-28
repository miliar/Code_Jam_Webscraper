#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <math.h>
#include <vector>
#include <fstream>
#include <iomanip>

using namespace std; 

ifstream fin("A-large.in");
ofstream fout("A-large.out");

#define pre setprecision(9)

int N;
string matches[105];
int wins[105], games[105];
double ow[105], oow[105];
int main() {
    int T;
    fin>>T;
    
    for(int k = 1;k<=T;++k) {
        fin>>N;
        for(int i = 0;i<N;++i) {
            fin>>matches[i];
            wins[i] = games[i] = 0;
            for(int j = 0;j<matches[i].size();++j) {
                if(matches[i][j] == '1') {
                    ++wins[i];
                    ++games[i];
                }    
                else if(matches[i][j] == '0')
                    ++games[i];
            }
        }
        for(int i = 0;i<N;++i) {
            int cnt = 0;
            double amt = 0;
            for(int j = 0;j<N;++j) {
                if(matches[i][j] == '1' || matches[i][j] == '0') {
                    int opWins = wins[j], opGames = games[j];
                    if(matches[i][j] == '0') --opWins;
                    --opGames;
                    ++cnt; 
                    if(opGames == 0) continue;
                    amt += ((double)(opWins))/opGames;
                }
            }
            amt/=cnt;
            ow[i] = amt;
        }
        fout<<"Case #"<<k<<":"<<endl;
        for(int i = 0;i<N;++i) {
            double amt = (games[i] == 0?0:(0.25*((double)wins[i])/games[i]))+0.5*ow[i];
            double sum = 0;
            int cnt = 0;
            for(int j = 0;j<N;++j) {
                if(matches[i][j] == '1' || matches[i][j] == '0') {
                    sum += ow[j];
                    ++cnt;
                }
            }
            sum/=cnt;
            amt += 0.25*sum;
            fout<<pre<<amt<<endl;
        }
    }  
    system("pause");
    return 0;
}
