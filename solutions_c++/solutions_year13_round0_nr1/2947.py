#include <iostream>
#include <string>

using namespace std;

#define XWON    "X won"
#define OWON    "O won"
#define DRAW    "Draw"
#define INC     "Game has not completed"
#define XW  0
#define OW  1
#define DW  2
#define IN  3

int checkGame(string s){
    
    int ret;
    unsigned int tpos = s.find("T");
    if (tpos != string::npos)
    {
        int rowNum = tpos/4;
        int colNum = tpos%4;
        int diag = 0;
        if (tpos%5 == 0)
            diag = 1;   // left diag
        else if (tpos%3 == 0)
            diag = 2;
        //check row
        char c = '0';
        int flag = 1;
        for (int i = rowNum*4; i < rowNum*4+4; i ++){
            if (s[i] == 'T')
                continue;
            if (c == '0'){
                c = s[i];
                continue;
            }
            if (c != s[i]){
                flag = 0;
                break;
            }
        }
        if (flag && c == 'X')
            return XW;
        else if (flag && c == 'O')
            return OW;
        // check column
        c = '0';
        flag = 1;
        for (int i = colNum; i < 16; i += 4){
            if (s[i] == 'T')
                continue;
            if (c == '0'){
                c = s[i];
                continue;
            }
            if (c != s[i]){
                flag = 0;
                break;
            }
        }
        if (flag && c == 'X')
            return XW;
        else if (flag && c == 'O')
            return OW;
        // check diagonal
        c = '0';
        flag = 1;
        if (diag == 1){
            for (int i = 0; i < 16; i += 5){
                if (s[i] == 'T')
                    continue;
                if (c == '0'){
                    c = s[i];
                    continue;
                }
                if (c != s[i]){
                    flag = 0;
                    break;
                }
            }
        }
        else if (diag == 2){
            for (int i = 3; i < 13; i += 3){
                if (s[i] == 'T')
                    continue;
                if (c == '0'){
                    c = s[i];
                    continue;
                }
                if (c != s[i]){
                    flag = 0;
                    break;
                }
            }
        }
        if (flag && c == 'X')
            return XW;
        else if (flag && c == 'O')
            return OW;
    }

    // check rows
    for (int i = 0; i < 16; i += 4){
        char c = '0';
        int flag = 1;
        for (int j = i; j < i+4; j++){
            if (c == '0'){
                c = s[j];
                continue;
            }
            if (c != s[j]){
                flag = 0;
                break;
            }
        }
        if (flag && c == 'X')
            return XW;
        else if (flag && c == 'O')
            return OW;
    }

    // check column
    for (int i = 0; i < 4; i ++){
        char c = '0';
        int flag = 1;
        for (int j = i; j < 16; j += 4){
            if (c == '0'){
                c = s[j];
                continue;
            }
            if (c != s[j]){
                flag = 0;
                break;
            }
        }
        if (flag && c == 'X')
            return XW;
        else if (flag && c == 'O')
            return OW;
    }

    // check diagonal
    // left diag
    char c = '0';
    int flag = 1;
    for (int i = 0; i < 16; i += 5){
        if (c == '0'){
            c = s[i];
            continue;
        }
        if (c != s[i]){
            flag = 0;
            break;
        }
    }
    if (flag && c == 'X')
        return XW;
    else if (flag && c == 'O')
        return OW;
    // right diag
    c = '0';
    flag = 1;
    for (int i = 3; i < 13; i += 3){
        if (c == '0'){
            c = s[i];
            continue;
        }
        if (c != s[i]){
            flag = 0;
            break;
        }
    }
    if (flag && c == 'X')
        return XW;
    else if (flag && c == 'O')
        return OW;

    // no empty squares - draw
    if (s.find(".") == string::npos)
        return DW;
    // empty squres - INC
    else
        return IN;
}





int main (void) {

    int n;
    int i = 0;
    cin >> n;

    string cases[n];
    string line;

    while (i < n)
    {
        cases[i] = "";
        cin >> line;
        cases[i] += line;
        cin >> line;
        cases[i] += line;
        cin >> line;
        cases[i] += line;
        cin >> line;
        cases[i] += line;
        i ++;
    }

    for (i = 1; i < n+1; i++){
        int ret = checkGame(cases[i-1]);
        if (ret == XW)
            cout << "Case #" << i << ": " << XWON << endl;
        else if (ret == OW)
            cout << "Case #" << i << ": " << OWON << endl;
        else if (ret == DW)
            cout << "Case #" << i << ": " << DRAW << endl;
        else
            cout << "Case #" << i << ": " << INC << endl;
    }

}
