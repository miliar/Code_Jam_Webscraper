#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <ctime>

#define ull unsigned long long
//#define DEBUG

#define VERT 1
#define HORIZ 2
#define DIAG1 3
#define DIAG2 4

using namespace std;

bool is_t [4][4];
char board [4][4];
bool checked [4][4];

void init(){
    for (int i = 0;i<4;i++){
        for(int j = 0;j<4;j++){
            is_t[i][j] = 0;
            board[i][j] = '.';
            checked[i][j] = 0;
        }
    }


}


bool filled(){
    for(int i =0;i<4;i++){
        for(int j=0;j<4;j++){
            if(board[i][j]=='.') return false;


        }
    }
    return true;
}

bool recurse(int i, int j, int depth, int prev, int flag, char c){
    if(depth==4&&flag<2){
        return 1;
    }

    if(i>3||j>3||j<0) return 0;
    int f = 0;
    if(board[i][j]=='T'||board[i][j]==c){
        if(board[i][j]=='T') f = 1;
        if(prev==VERT) return recurse (i+1,j,depth+1,prev,flag+f,c);
        else if(prev==HORIZ) return recurse (i,j+1,depth+1,prev,flag+f,c);
        else if(prev==DIAG1) return recurse (i+1,j+1,depth+1,prev,flag+f,c);
        else if(prev==DIAG2) return recurse (i+1,j-1,depth+1,prev,flag+f,c);
    }

    return 0;
}


int check(char c){
    int answer = 0;

    for(int i = 0;i<4;i++){
        answer+=recurse(0,i,0,VERT,0,c);
        answer+=recurse(i,0,0,HORIZ,0,c);
    }
    answer+=recurse(0,0,0,DIAG1,0,c);
    answer+=recurse(0,3,0,DIAG2,0,c);

    return answer;

}

int main ()
{
    #ifndef DEBUG
        freopen ("A-large.in","r",stdin);
        freopen ("A-large.out","w",stdout);
    #endif


    int t;
    cin>>t;
    string garbage;
    for (int _t=0;_t<t;_t++){
        init();

        for(int i =0;i<4;i++){
            cin>>garbage;
            for(int j=0;j<4;j++){
                board[i][j] = garbage[j];
                if(garbage[j]=='T'){
                    is_t[i][j] = 1;
                }
            }
        }


        if(check('O')){
            cout<<"Case #"<<_t+1<<": O won"<<endl;
        }
        else if(check('X')){
            cout<<"Case #"<<_t+1<<": X won"<<endl;
        }

        else if(filled()){
            cout<<"Case #"<<_t+1<<": Draw"<<endl;
        }
        else {
            cout<<"Case #"<<_t+1<<": Game has not completed"<<endl;
        }
        getline(cin,garbage);

    }

    return 0;
}

