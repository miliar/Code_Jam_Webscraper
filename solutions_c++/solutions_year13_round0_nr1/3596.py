#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> R(4, vector<int>(4));

bool won(int k){
    for(int i=0; i<4; ++i){
        int s1 = 0, s2 = 0;
        for(int j=0; j<4; ++j){
            if(R[i][j] == k || R[i][j] == 3) s1++;
            if(R[j][i] == k || R[j][i] == 3) s2++;
        }
        if(s1 == 4 || s2 == 4) return true;
    }
    int s1 = 0, s2 = 0;
    for(int i=0; i<4; ++i){
        if(R[i][i] == k || R[i][i] == 3) s1++;
        if(R[i][3-i] == k || R[i][3-i] == 3) s2++;
    }
    if(s1 == 4 || s2 == 4) return true;
    return false;
}

bool draw(){
    for(int i=0; i<4; ++i){
        for(int j=0; j<4; ++j){
            if(R[i][j] == 0) return false;
        }
    }
    return true;
}

int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t){
        cout << "Case #" << t << ": ";
        char c;
        for(int i=0; i<4; ++i){
            for(int j=0; j<4; ++j){
                cin >> c;
                switch(c){
                    case '.': R[i][j] = 0; break;
                    case 'X': R[i][j] = 1; break;
                    case 'O': R[i][j] = 2; break;
                    case 'T': R[i][j] = 3; break;
                }
            }
        }
        if(won(1)){
            cout << "X won" << '\n';
        }
        else if(won(2)){
            cout << "O won" << '\n';
        }
        else if(draw()){
            cout << "Draw" << '\n';
        }
        else{
            cout << "Game has not completed" << '\n';
        }
    }
}
