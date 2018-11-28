#include <iostream>
#include <conio.h>
#include <fstream>
#include <string>

using namespace std;

char a[4][4];
bool accept_row[4];
bool accept_col[4];
bool accept_across1;
bool accept_across2;
void init(){
    char buf[255];
    for(int i = 0; i<4; i++){
        cin.getline(buf, 255);
        for(int j = 0; j < 4; j++)
            a[i][j] = buf[j];
    }
    cin.getline(buf, 255);
}

void process(int ti){
    bool draw_flag = false;
    bool X_flag = false;
    bool O_flag = false;
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++)
            if(a[i][j] == '.')
                draw_flag = true;
    }

    for(int i = 0; i < 4; i++){
        accept_row[i] = true;
        for(int j = 0; j < 4; j++)
            if(a[i][j] != 'X' && a[i][j] != 'T')
                accept_row[i] = false;
        X_flag = X_flag || accept_row[i];
    }

    for(int j = 0; j < 4; j++){
        accept_col[j] = true;
        for(int i = 0; i < 4; i++)
            if(a[i][j] != 'X' && a[i][j] != 'T')
                accept_col[j] = false;
        X_flag = X_flag || accept_col[j];
    }
    accept_across1 = true;
    for(int i = 0; i < 4; i++){
        if(a[i][i] != 'X' && a[i][i] != 'T')
            accept_across1 = false;
    }
    X_flag = X_flag || accept_across1;
    accept_across2 = true;
    for(int i = 0; i < 4; i++){
        if(a[i][3-i] != 'X' && a[i][3-i] != 'T')
            accept_across2 = false;
    }
    X_flag = X_flag || accept_across2;


    if(X_flag){
        cout << "Case #" << ti+1 << ": X won" << endl;
        return;
    }

    for(int i = 0; i < 4; i++){
        accept_row[i] = true;
        for(int j = 0; j < 4; j++)
            if(a[i][j] != 'O' && a[i][j] != 'T')
                accept_row[i] = false;
        O_flag = O_flag || accept_row[i];
    }

    for(int j = 0; j < 4; j++){
        accept_col[j] = true;
        for(int i = 0; i < 4; i++)
            if(a[i][j] != 'O' && a[i][j] != 'T')
                accept_col[j] = false;
        O_flag = O_flag || accept_col[j];
    }
    accept_across1 = true;
    for(int i = 0; i < 4; i++){
        if(a[i][i] != 'O' && a[i][i] != 'T')
            accept_across1 = false;
    }
    O_flag = O_flag || accept_across1;
    accept_across2 = true;
    for(int i = 0; i < 4; i++){
        if(a[i][3-i] != 'O' && a[i][3-i] != 'T')
            accept_across2 = false;
    }
    O_flag = O_flag || accept_across2;

    if(O_flag){
        cout << "Case #" << ti+1 << ": O won" << endl;
        return;
    }


    if(draw_flag){
        cout << "Case #" << ti+1 << ": Game has not completed" << endl;
        return;
    }

    cout << "Case #" << ti+1 << ": Draw" << endl;
}

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int TC;
    cin >> TC;
    cin.ignore(1);
    for(int ti = 0; ti < TC; ti++){
        init();
        process(ti);
    }
    return 0;
}
