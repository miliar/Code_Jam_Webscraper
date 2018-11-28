#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <math.h>
#include <string.h>
#include <stack>

using namespace std;

string intToStr(int n) {
    if(n == 0) return "0";
    string ans = "";
    while(n > 0) {
        ans = (char) ((n % 10) + '0') + ans;
        n /= 10;
    }
    return ans;
}

int strToInt(string n) {
    int ans = 0;
    for(int i = 0; i < n.size(); i++){
        ans += (n[n.size() -i - 1] - '0') * pow(10, i);
    }
    return ans;
}

int n;
char tab[4][4];

bool win(char p){
    bool win = false;
    for(int j = 0; j < 4; j++){
        int tl = 0, tc = 0;
        for(int i = 0; i < 4; i++){
            if(tab[i][j] == p || tab[i][j] == 'T'){
                tl++;
            }
            if(tab[j][i] == p || tab[j][i] == 'T'){
                tc++;
            }
        }
        win |= tc > 3 || tl > 3;
    }
    int diagleft = 0, diagright = 0;
    for(int i = 0; i < 4; i++){
        if(tab[i][i] == p || tab[i][i] == 'T'){
            diagleft++;
        }
        if(tab[4-i-1][i] == p || tab[4-i-1][i] == 'T'){
            diagright++;
        }
    }
    win |= diagleft > 3 || diagright > 3;
    return win;
}

int main(void){
    int test = 1;
    freopen("in.in.c", "r", stdin);
    freopen("out.out", "w", stdout);
    cin >> n;
    while(n--){
    int countdot = 0;
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                cin >> tab[i][j];
                if(tab[i][j] == '.') countdot++;
            }
        }
        cout << "Case #" << test++ << ": ";
        if(win('X')){
            cout << "X won\n";
        }else if(win('O')){
            cout << "O won\n";
        }else if(countdot == 0){
            cout << "Draw\n";
        }else{
            cout << "Game has not completed\n";
        }
    }
    return 0;
}
