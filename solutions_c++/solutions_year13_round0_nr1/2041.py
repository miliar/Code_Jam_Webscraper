#include<cstdio>
#include<string>
#include<vector>
#include<iostream>

using namespace std;

string getResult(vector<string> &board){
    int i,j,r=-1,c=-1;
    char st;
    bool found = true;
    for(i=0;i<4;i++){
        for(j=0;j<4;j++){
            if(board[i][j] == 'T'){
                r = i;
                c = j;
            }

        }

    }
    if(r!=-1){
        found = true;
        if(c == 0)
            st = board[r][1];
        else
            st = board[r][0];
        if(st != '.'){
            for(i=0;i<4;i++){
                if(i == c)
                    continue;
                if(board[r][i]!=st){
                    found = false;
                }

            }
        }
        else{
            found = false;
        }
        if(found) {
            string s = "";
            s.push_back(st);
            s+=" won";
            return s;

        }
        found = true;
        if(r == 0)
            st = board[1][c];
        else
            st = board[0][c];
        if(st != '.'){
            for(i=0;i<4;i++){
                if(i == r)
                    continue;
                if(board[i][c]!=st){
                    found = false;
                }

            }
        }
        else{
            found = false;
        }
        if(found) {
            string s = "";
            s.push_back(st);
            s+=" won";
            return s;

        }

        if(r==c){
            found = true;
            if(r==0){
                st = board[1][1];
            }
            else
                st = board[0][0];
            if(st != '.'){
                for(i=0;i<4;i++){
                    if(i==r)
                        continue;
                    else{
                        if(board[i][i]!=st)
                            found = false;

                    }
                }

            }
            else{
                found = false;
            }
            if(found) {
                string s = "";
                s.push_back(st);
                s+=" won";
                return s;

            }


        }
        if((r+c) == 3){
            found = true;
            if(r==0){
                st = board[3][0];
            }
            else
                st = board[0][3];
            if(st != '.'){
                for(i=0;i<4;i++){
                    if(i==r)
                        continue;
                    else{
                        if(board[i][3-i]!=st)
                            found = false;

                    }
                }

            }
            else{
                found = false;
            }
            if(found) {
                string s = "";
                s.push_back(st);
                s+=" won";
                return s;

            }


        }

    }

    for(i=0;i<4;i++){
        found = true;
        if(board[i][0]=='.')
            continue;
        for(j=1;j<4;j++){
            if(board[i][j]!=board[i][j-1])
                found = false;

        }
        if(found){
            string s = "";
            s.push_back(board[i][0]);
            s+=" won";
            return s;
        }


    }

    for(i=0;i<4;i++){
        found = true;
        if(board[0][i]=='.')
            continue;
        for(j=1;j<4;j++){
            if(board[j][i]!=board[j-1][i])
                found = false;

        }
        if(found){
            string s = "";
            s.push_back(board[0][i]);
            s+=" won";
            return s;
        }


    }

    if(board[0][0]!='.'){
        found = true;
        for(i=1;i<4;i++){
            if(board[0][0]!=board[i][i])
                found = false;

        }
        if(found){
            string s = "";
            s.push_back(board[0][0]);
            s+=" won";
            return s;
        }

    }

    if(board[0][3]!='.'){
        found = true;
        for(i=1;i<4;i++){
            if(board[0][3]!=board[i][3-i])
                found = false;

        }
        if(found){
            string s = "";
            s.push_back(board[0][3]);
            s+=" won";
            return s;
        }

    }



    for(i=0;i<4;i++){
        for(j=0;j<4;j++){
            if(board[i][j] == '.'){
                return "Game has not completed";
            }

        }

    }


    return "Draw";

}

int main(){

    int T,tc=1;
    vector<string> board;
    scanf("%d\n",&T);
    while(tc <= T){
        board = vector<string>();
        string s;
        for(int i=0;i<4;i++){
            getline(cin,s);
            board.push_back(s);
        }
        cout <<"Case #" << tc << ": " << getResult(board) <<endl;
        scanf("\n");
        tc++;
    }



}
