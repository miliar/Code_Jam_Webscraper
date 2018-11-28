//In the name of Allah
#include <iostream>
using namespace std;

char a[10][10];

bool check(char c){
    int me = 0, t = 0;
    for(int i = 0; i < 4; i++){
        me = t = 0;
        for(int j = 0; j < 4; j++)
            if (a[i][j] == c)   me++;
            else if (a[i][j] == 'T')    t++;
        if (me == 4 || (me == 3 && t == 1)) return true;
    }

    for(int j = 0; j < 4; j++){
        me = t = 0;
        for(int i = 0; i < 4; i++)
            if (a[i][j] == c)   me++;
            else if (a[i][j] == 'T')    t++;
        if (me == 4 || (me == 3 && t == 1)) return true;
    }

    me = t = 0;
    for(int i = 0; i < 4; i++){
        if (a[i][i] == c)   me++;
        else if (a[i][i] == 'T')    t++;
        if (me == 4 || (me == 3 && t == 1)) return true;
    }


    me = t = 0;
    for(int i = 0; i < 4; i++){
        if (a[i][3-i] == c)   me++;
        else if (a[i][3-i] == 'T')    t++;
        if (me == 4 || (me == 3 && t == 1)) return true;
    }

    return false;
}

string solve(){
    if (check('X'))
        return "X won";
    if (check('O'))
        return "O won";
    for(int i = 0; i < 4; i++)for(int j = 0; j < 4; j++)
        if (a[i][j] == '.') return "Game has not completed";
    return "Draw";
}

int main(){
    int tests;
    cin >> tests;
    for (int tt = 1; tt <= tests; tt++){
        for(int i = 0; i < 4; i++)for(int j = 0; j < 4; j++) cin >> a[i][j];
        cout << "Case #" << tt << ": " << solve() << endl;
    }
    return 0;
}
