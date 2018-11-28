#include <iostream>
#include <conio.h>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

int board[2][4][4] ;
int boardweight[4][4] ;
int winPlayer = 0 ;
int N ;

string caseout[4] ;


int main()
{
    string word ;

    caseout[0] = "Game has not completed" ;
    caseout[1] = "X won" ;
    caseout[2] = "O won" ;
    caseout[3] = "Draw" ;

    freopen("A-large.in", "r", stdin);
    freopen("result.txt", "w", stdout);

    scanf("%d" , &N);

    for(int i=0; i<N ; i++){

        for(int j =0 ; j<4 ; j++){
                cin>>word ;
                for(int k =0 ; k<4; k++){
                    if(word[k]=='X'){
                        //cout<<j<<k<<"  " ;
                        board[0][j][k] = 1 ;
                        board[1][j][k] = 0 ;
                        boardweight[j][k] = 1 ;
                    }
                    else if(word[k]=='O'){
                        board[1][j][k] = 1 ;
                        board[0][j][k] = 0 ;
                        boardweight[j][k] = 1 ;
                    }
                    else if(word[k]=='T'){
                        boardweight[j][k] = 1 ;
                        board[0][j][k] = 1 ;
                        board[1][j][k] = 1 ;
                    }
                    else{
                        boardweight[j][k] = 0 ;
                        board[0][j][k] = 0 ;
                        board[1][j][k] = 0 ;
                    }
                   // cout<<board[1][j][k] ;


                }
                //cout<<endl ;

            }
        //cin>>word ;
        winPlayer = 0;

        for(int l = 0; l<2 ; l++){
            for(int j =0 ; j<4 ;j++)
                if((board[l][j][0]==1)&&(board[l][j][1]==1)&&(board[l][j][2]==1)&&(board[l][j][3]==1)){

                    winPlayer = l+1 ;
                }
            for(int j =0 ; j<4 ;j++)
                if((board[l][0][j]==1)&&(board[l][1][j]==1)&&(board[l][2][j]==1)&&(board[l][3][j]==1)){

                    winPlayer = l+1 ;
                }
            if((board[l][0][0]==1)&&(board[l][1][1]==1)&&(board[l][2][2]==1)&&(board[l][3][3]==1))
                {

                   winPlayer = l+1 ;
                }

            if((board[l][0][3]==1)&&(board[l][3][0]==1)&&(board[l][2][1]==1)&&(board[l][1][2]==1))
                {

                    winPlayer = l+1 ;
                }
        }

        int flagfilled = 0;
        if(winPlayer==0)
        {
            //cout<<winPlayer ;
        flagfilled = 1 ;

        for(int l =0 ; l<4 ;l++){
            for(int m =0 ; m<4; m++){

                if(boardweight[l][m]!=1){
                    flagfilled = 0 ;
                    break ;
                }

            }
        }
        }

        if(flagfilled==1){
            winPlayer = 3 ;
        }

        cout<<"Case #"<<(i+1)<<": "<<caseout[winPlayer]<<"\n" ;

    }

    return 0;

}

