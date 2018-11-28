#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <iomanip>
#include <sstream>
#include <cstring>
#include <cmath>

using namespace std;

typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<string> vs;
typedef vector<bool> vb;

enum ST {WinX=0,WinO,OTH, Draw, CONT};

ST check(string& str){
    int numX = 0, numO = 0;
    //assert(str.size() == 4);
    if(str.size() != 4){
        std::cerr<<str<<endl;
        std::cerr<<"Error of size"<<std::endl;
        exit(-1);
    }

    for(int i=0; i< 4; i++){

        if(str[i]=='X'){
            numX++;
        }
        else if(str[i] == 'O'){
            numO++;
        }
        else if(str[i] == 'T'){
            numX++;
            numO++;
        }
    }

    if(numX==4){
        return WinX;
    }
    else if(numO==4){
        return WinO;
    }

    return OTH;

}

void output(ST str, int c){

    cout<<"Case #"<<c<<": ";
    if(str == WinX){
        cout<<"X won";
    }

    else if(str == WinO){
        cout<<"O won";
    }

    else if(str == Draw){

        cout<<"Draw";
    }

    else if(str==CONT) {

        cout<<"Game has not completed";

    }

    else{
        cerr<<"Error of game output"<<endl;
        exit(-1);
    }

    cout<<endl;
}

int main()
{
    int T;
    cin>>T;
    int n = 4;
    int count = 0;

    for(int c=1; c<=T; c++){
        vs board(n), board_inv(n,string(n,'.'));
        ST tmp;

        bool isFull = true;

        for(int i=0; i<n;i++){

            cin>>board[i];
            //cerr<<board[i]<<endl;
            count++;
            //cerr<<count<<endl;
        }

        for(int i=0; i<n;i++){

            for(int j=0; j<n; j++){

                board_inv[j][i] = board[i][j];

                if(board[i][j]=='.'){
                    isFull = false;
                }
            }
        }

//        cerr<<"Inv "<<endl;
//        for(int i=0; i<n;i++){
//            cerr<<board_inv[i]<<endl;
//        }
        string diag="", diag_inv="";

        for(int i=0; i<n;i++){
            //string row="",col="";

            // Checking all rows
            tmp = check(board[i]);
            if( tmp != OTH){
                output(tmp,c);
                break;
            }


            // Checking all columns
            tmp = check(board_inv[i]);
            if( tmp != OTH){
                output(tmp,c);
                break;
            }

            // Constructing diagonals
            for(int j=0; j<n;j++){

                if(i==j){

                    //cerr<<"now "<<board[i][j]<<endl;
                    diag+= string(1,board[i][j]);
                }

                if(i==n-j-1){
                    diag_inv+= string(1,board[i][j]);
                }
            }


        }

//        cerr<<"diag = "<<diag<<endl;
//        cerr<<"diag env = "<<diag_inv<<endl;

        if(tmp == OTH){

            tmp = check(diag);
            if( tmp != OTH){
                output(tmp,c);
                continue;
            }

            tmp = check(diag_inv);

            if( tmp != OTH){
                output(tmp,c);
                continue;
            }


            if(isFull){

                output(Draw,c);


            }

            else{

                output(CONT,c);

            }

        }



    }

}

