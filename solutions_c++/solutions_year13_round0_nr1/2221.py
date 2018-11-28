/*
 * =============================================================
 *
 *       Filename:  tictac.cpp
 *    Description:  
 *         Author:  Shitikanth Kashyap (), shitikanth1@gmail.com
 *   Organization:  University of Waterloo
 *
 * ==============================================================
 */

#include <iostream>
#include <cstdio>

using namespace std;


int main() {
    char board[16];
    // X- 1, O - 0, T-2, .-(-1)
    bool over=false;

    int T;
    char c;

    scanf("%d",&T);
    int cur_t=0;
    while(cur_t<T){
        over=false;
        for(int i=0; i<16; i++){
            do scanf("%c",&c);
            while(c==' ' || c=='\n');
            board[i]=c;
        }
        printf("Case #%d: ",++cur_t);
        /*  */
        // check rows
        for(int i=0; i<4; i++){
            c='T';
            bool flag=true;
            for(int j=0; j<4; j++){
                if(board[4*i+j]=='.'){
                    flag=false;
                    break;
                }
                if(c=='T'){
                    c=board[4*i+j];
                }
                else if(board[4*i+j]!=c && board[4*i+j]!='T'){
                    flag=false;
                    break;
                }
            }
            if(flag){
                printf("%c won\n",c);
                over=true;
                break;
            }
        }
        if(over)
            continue;
        //check columns
        for(int j=0; j<4; j++){
            c='T';
            bool flag=true;
            for(int i=0; i<4; i++){
                if(board[4*i+j]=='.'){
                    flag=false;
                    break;
                }
                if(c=='T')
                    c=board[4*i+j];
                else if(board[4*i+j]!=c && board[4*i+j]!='T'){
                    flag=false;
                    break;
                }
            }
            if(flag){
                printf("%c won\n",c);
                over=true;
                break;
            }
        }
        if(over)
            continue;
        //check diagonals
        bool flag=true;
        c='T';
        for(int i=0; i<4; i++){
            int j=i;
            if(board[4*i+j]=='.'){
                flag=false;
                break;
            }
            if(c=='T')
                c=board[4*i+j];
            else if(board[4*i+j]!=c && board[4*i+j]!='T'){
                flag=false;
                break;
            }
        }
        if(flag){
            printf("%c won\n",c);
            over=true;
        }
        if(over)
            continue;
        flag=true;
        c='T';
        for(int i=0; i<4; i++){
            int j=3-i;
            if(board[4*i+j]=='.'){
                flag=false;
                break;
            }
            if(c=='T')
                c=board[4*i+j];
            else if(board[4*i+j]!=c && board[4*i+j]!='T'){
                flag=false;
                break;
            }
        }
        if(flag){
            printf("%c won\n",c);
            over=true;
        }
        if(over)
            continue;
        over=true;
        for(int i=0; i<16; i++)
            if(board[i]=='.'){
                over=false;
                break;
            }
        if(over)
            printf("Draw\n");
        else
            printf("Game has not completed\n");

    }

    return 0;
}
