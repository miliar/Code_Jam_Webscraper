#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<set>
#include<string>
#include<iostream>
using namespace std;

//#define _DEBUG 0


#define OandX ('O' & 'X')
#define  OandT ('O' & 'T')
#define XandT ('X' & 'T')
#define OandXandT ('O' & 'X' & 'T')

char board[4][4];
char resRow[4];
char resLine[4];
int resDiag[2];

int iCaseCount;

int output(char *str){
    cout << "Case #" << iCaseCount + 1 << ": ";
    cout << str << endl;
   return 0;
}

int init(){
    for(int i = 0; i < 4; ++i)
        for(int j = 0; j < 4; ++j)
            cin >> board[i][j];
    for(int i = 0; i < 4; ++i) resRow[i] = resLine[i] = -1;

#ifdef
    for(int i = 0; i < 4; ++i){
        for(int j = 0; j < 4; ++j){
            cout << board[i][j];
        }
        cout << endl;
    }
    system("pause");
#endif

    return 0;
}

int solve(){
    bool globalEmpty = 0;
    for(int i = 0; i < 4; ++i){
        int bitState = 0x000000ff;
        bool breakFlag = 0;
        for(int j = 0; j < 4; ++j){
            if('.' == board[i][j]){
                breakFlag = 1;
                globalEmpty = 1;
                break;
            }
            //cout << bitState << "-" << (char)board[i][j] << endl;
            bitState &= board[i][j];
        }
        //cout << XandT << " " << bitState << endl;
        if(!breakFlag && ((bitState == OandT) || bitState == (int)'O')){
            output("O won");
            return 0;
        }
        if(!breakFlag && ((bitState == XandT) || bitState == (int)'X')){
            output("X won");
            return 0;
        }
    }
    
    for(int i = 0; i < 4; ++i){
        char bitState = 255;
        bool breakFlag = 0;
        for(int j = 0; j < 4; ++j){
            if('.' == board[j][i]){
                breakFlag = 1;
                globalEmpty = 1;
                break;
            }
            bitState &= board[j][i];
        }
        if(!breakFlag && ((bitState == OandT) || bitState == (int)'O')){
            output("O won");
            return 0;
        }
        if(!breakFlag && ((bitState == XandT) || bitState == (int)'X')){
            output("X won");
            return 0;
        }
    }
    
    for(int i = 0; i < 1; ++i){
        char bitState = 255;
        bool breakFlag = 0;
        for(int j = 0; j < 4; ++j){
            if('.' == board[j][j]){
                breakFlag = 1;
                globalEmpty = 1;
                break;
            }
            bitState &= board[j][j];
        }
        if(!breakFlag && ((bitState == OandT) || bitState == (int)'O')){
            output("O won");
            return 0;
        }
        if(!breakFlag && ((bitState == XandT) || bitState == (int)'X')){
            output("X won");
            return 0;
        }
    }

    for(int i = 0; i < 1; ++i){
        char bitState = 255;
        bool breakFlag = 0;
        for(int j = 0; j < 4; ++j){
            if('.' == board[4 - j - 1][j]){
                breakFlag = 1;
                globalEmpty = 1;
                break;
            }
            bitState &= board[4 - j - 1][j];
        }
        if(!breakFlag && ((bitState == OandT) || bitState == (int)'O')){
            output("O won");
            return 0;
        }
        if(!breakFlag && ((bitState == XandT) || bitState == (int)'X')){
            output("X won");
            return 0;
        }
    }
    
    if(globalEmpty){
        output("Game has not completed");
        return 0;
    }else{
        output("Draw");
        return 0;
    }
    return 0;
}

int main(){
#ifdef _DEBUG
    cout << (0xffffffff & OandXandT) << endl;
    cout << (0xffffffff & OandX) << endl;
    cout << (0xffffffff & XandT) << endl;
    cout << (0xffffffff & OandT) << endl;
#endif
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int iCaseMaxCount = 0;
    while(cin >> iCaseMaxCount){
        iCaseCount = 0;
        for(; iCaseCount < iCaseMaxCount; ++iCaseCount){
            init();
            solve();
        }
    }
    return 0;
}
/*
6
XXXT
....
OO..
....

XOXT
XXOO
OXOX
XXOO

XOX.
OX..
....
....

OOXX
OXXX
OX.T
O..O

XXXO
..O.
.O..
T...

OXXX
XO..
..O.
...O
*/

