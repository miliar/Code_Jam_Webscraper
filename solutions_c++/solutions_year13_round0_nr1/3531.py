#include <cstdio>
#include <fstream>
#include <stdint.h>
#define for0(i, n) for(int i = 0; i < n; i++)
using namespace std;
const int n = 4;
char m[n][n];
bool hasWinCombination(char notThis){
    bool win = true;
    for0(i, n){
        win = true;
        for0(j, n){
            if(m[i][j] == notThis || m[i][j] == '.'){
                win = false;
                break;
            }
        }
        if(win){
            return true;
        }
    }
    for0(i, n){
        win = true;
        for0(j, n){
            if(m[j][i] == notThis || m[j][i] == '.'){
                win = false;
                break;
            }
        }
        if(win){
            return true;
        }
    }
    win = true;
    for0(i, n){
        if(m[i][i] == notThis || m[i][i] == '.'){
            win = false;
            break;
        }
    }
    if(win){
        return true;
    }
    win = true;
    for0(i, n){
        if(m[n - 1 - i][i] == notThis || m[n - 1 - i][i] == '.'){
            win = false;
            break;
        }
    }
    if(win){
        return true;
    }
    return false;
}
int main() {
    ifstream in("common.in");
    ofstream out("common.out");
    int testCount;
    in>>testCount;

    for0(k, testCount){
        for0(i, n){
            in>>m[i];
        }
        bool notFinished = false;
        for(int i = 0; i < n && !notFinished; i++){
            for0(j, n){
                if(m[i][j] == '.'){
                    notFinished = true;
                    break;
                }
            }
        }
        out<<"Case #"<<(k + 1)<<": ";
        if(hasWinCombination('O')){
            out<<"X won\n";
        } else if(hasWinCombination('X')){
            out<<"O won\n";
        } else if(notFinished){
            out<<"Game has not completed\n";
        } else {
            out<<"Draw\n";
        }
    }
    return 0;
}
