#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>
using namespace std;
const string X_WON = "X won\n";
const string O_WON = "O won\n";
const string GAME_DRAW = "Draw\n";
const string GAME_NOT_COMPLETED = "Game has not completed\n";
string arr[4];
bool evaluated;
void print(int x,int y) {
    if( arr[x][y] == 'X' )
        cout<<X_WON;
    if( arr[x][y] == 'O' )
        cout<<O_WON;
    evaluated = true;
}

bool checkLeftDiagnol() {
    int countX = 0, countO = 0, countT = 0;
    for(int i = 0 ; i < 4 ; i++) {
        switch( arr[i][i] ) {
            case 'X' : ++ countX; break;
            case 'O' : ++ countO; break;
            case 'T' : ++ countT; break;
        }
    }
    if( countX + countT == 4) {
        for( int i = 0 ; i < 4 ; i++) {
            arr[i][i] = 'X';
        }
        return true;
    } else if( countO + countT == 4) {
        for( int i = 0 ; i < 4 ; i++) {
            arr[i][i] = 'O';
        }
        return true;
    } else {
        return false;
    }
}
bool checkRightDiagnol() {
    int countX = 0, countO = 0, countT = 0;
    for(int i = 0 ; i < 4 ; i++) {
        switch( arr[3-i][i] ) {
            case 'X' : ++ countX; break;
            case 'O' : ++ countO; break;
            case 'T' : ++ countT; break;
        }
    }
    if( countX + countT == 4) {
        for( int i = 0 ; i < 4 ; i++) {
            arr[3-i][i] = 'X';
        }
        return true;
    } else if( countO + countT == 4) {
        for( int i = 0 ; i < 4 ; i++) {
            arr[3-i][i] = 'O';
        }
        return true;
    } else {
        return false;
    }
}
bool checkRow(int x) {
    int countX = 0, countO = 0, countT = 0;
    for(int i = 0 ; i < 4 ; i++) {
        switch( arr[x][i] ) {
            case 'X' : ++ countX; break;
            case 'O' : ++ countO; break;
            case 'T' : ++ countT; break;
        }
    }
    if( countX + countT == 4) {
        for( int i = 0 ; i < 4 ; i++) {
            arr[x][i] = 'X';
        }
        return true;
    } else if( countO + countT == 4) {
        for( int i = 0 ; i < 4 ; i++) {
            arr[x][i] = 'O';
        }
        return true;
    } else {
        return false;
    }
}
bool checkColumn(int x) {
    int countX = 0, countO = 0, countT = 0;
    for(int i = 0 ; i < 4 ; i++) {
        switch( arr[i][x] ) {
            case 'X' : ++ countX; break;
            case 'O' : ++ countO; break;
            case 'T' : ++ countT; break;
        }
    }
    if( countX + countT == 4) {
        for( int i = 0 ; i < 4 ; i++) {
            arr[i][x] = 'X';
        }
        return true;
    } else if( countO + countT == 4) {
        for( int i = 0 ; i < 4 ; i++) {
            arr[i][x] = 'O';
        }
        return true;
    } else {
        return false;
    }
}
bool gridComplete() {
    for(int i = 0 ; i < 4 ; i++) {
        for(int j = 0 ; j < 4 ; j++) {
            if(arr[i][j] == '.') {
                return false;
            }
        }
    }
    return true;
}
int main() {
    int t, Kases = 0;
    scanf("%d",&t);
    while(Kases < t) {
        scanf("\n");
        cout<<"Case #" << ++Kases << ": ";
                for(int i = 0 ; i < 4 ; i++) {
            for(int j = 0 ; j < 4 ; j++) {
                arr[i][j] = '.';
            }
        }
        for(int i = 0 ; i < 4 ; i++) {
            getline(cin, arr[i]);
        }
        evaluated = false;
        if( !evaluated && checkLeftDiagnol() ) {
            print(0, 0);
        }
        for(int i = 0 ; !evaluated && i < 4 ; i++) {
            if( checkRow(i) ) {
                print(i, 0);
            }
        }
        for(int i = 0 ; !evaluated && i < 4 ; i++) {
            if (checkColumn(i) ) {
                print(0, i);
            }
        }
        if( !evaluated && checkRightDiagnol() ) {
            print(0, 3);
        }
        
        if( !evaluated ) {
            if( gridComplete() )
                cout<<GAME_DRAW;
            else
                cout<<GAME_NOT_COMPLETED;
        }
    }
    return 0;
}
