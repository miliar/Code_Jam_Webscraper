#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cmath>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<string>
#include<climits>
#include<cfloat>
using namespace std;

const double PI = std::atan(1.0)*4;

char checkHorizontal(char **play ){
    bool wins = true;
    char pl = 'x';
    for(int i=0;i<4;++i){
        wins = true;
        pl = 'x';
        for(int j=1;j<4;++j){
            if(play[i][j] == '.'){
                wins = false;
                break;
            }
            if(play[i][j] != play[i][j-1]){
                wins = false;
                break;
            }else{
                pl = play[i][j];
            }
        }
        if(wins) 
            return pl;
    }

    return 'x';
}
char checkVertical(char **play ){
    bool wins = true;
    char pl = 'x';
    for(int j=0;j<4;++j){
        wins = true;
        pl = 'x';
        for(int i=1;i<4;++i){
            if(play[i][j] == '.'){
                wins = false;
                break;
            }
            if(play[i][j] != play[i-1][j]){
                wins = false;
                break;
            }else{
                pl = play[i][j];
            }
        }
        if(wins) 
            return pl;
    }

    return 'x';
}
char checkDiagonal(char ** play , bool izq){
    char pl = 'x';
    bool wins = true;
    if(izq){
        for(int i=1;i<4;++i){
            if(play[i][i] == '.'){
                wins = false;
                break;
            }
            if(play[i][i] != play[i-1][i-1]){
                wins = false;
                break;
            }else{
                pl = play[i][i];
            }
        }
    }else{
        int cont = 1;
        for(int i=2;i>=0 ;--i){
            if(play[cont][i] == '.'){
                wins = false;
                break;
            }
            if(play[cont][i] != play[cont-1][i+1]){
                wins = false;
                break;
            }else{
                pl = play[cont][i];
            }
            ++cont;
        }
    }
    if(wins)
        return pl;
    else
        return 'x';
}

int main(int argc, char *argv[]){
    int n;
    cin >>n;

    char ** playO = (char **)malloc(sizeof(char* )*4);
    char ** playX = (char **)malloc(sizeof(char* )*4);
    for(int i=0;i<4;++i){
        playO[i] = (char *)malloc(sizeof(char)*4);
        playX[i] = (char *)malloc(sizeof(char)*4);
    }

    bool empties = false, wins = false;
    char ant = 'x', p ='x';

    for(int t=1;t<=n;++t){
        /* Read */
        cout << "Case #" << t << ": ";
        empties = false;
        wins = true;

        int numX = 0;
        int numO = 0;

        for(int i=0;i<4;++i){
            scanf("%s",playO[i]);
            sprintf(playX[i],"%s",playO[i]);

            for(int j=0;j<4;++j){
                if(playO[i][j] == 'O')
                    numO++;
                else if(playO[i][j] == 'X')
                    numX++;
                if(playO[i][j] == 'T'){
                    playO[i][j] = 'O';
                    playX[i][j] = 'X';
                }
                if(playO[i][j] == '.'){
                    empties = true;
                }
            }
        }
        
        //scanf("%*s");

        // FIRST OPTION 
        /* Check horizontals */
        p = checkHorizontal(playX);
        if(p != 'x'){
            cout << p<< " won" << endl;
            continue;
        }
        p = checkVertical(playX);
        if(p != 'x'){
            cout << p<< " won" << endl;
            continue;
        }
        p = checkDiagonal(playX, true);
        if(p != 'x'){
            cout << p << " won" << endl;
            continue;
        }
        p = checkDiagonal(playX,false);
        if(p != 'x'){
            cout << p << " won" << endl;
            continue;
        }


        // SECOND OPTION 
        /* Check horizontals */
        p = checkHorizontal(playO);
        if(p != 'x'){
            cout << p << " won" << endl;
            continue;
        }
        /* check verticals */
        p = checkVertical(playO);
        if(p != 'x'){
            cout << p << " won" << endl;
            continue;
        }
        /* check diagonals */
        p = checkDiagonal(playO, true);
        if(p != 'x'){
            cout << p << " won" << endl;
            continue;
        }
        p = checkDiagonal(playO,false);
        if(p != 'x'){
            cout << p << " won" << endl;
            continue;
        }

        if(empties){
            cout << "Game has not completed" << endl;
        }else{
            cout << "Draw" << endl;
        }
    }
    for(int i=0;i<4;++i){
        free(playO[i]);
        free(playX[i]);
    }
    free(playO);
    free(playX);


    return EXIT_SUCCESS;    
}



