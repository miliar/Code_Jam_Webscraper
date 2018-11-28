#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main()
{
    ifstream fin("A-small-attempt2.in");
    ofstream fout("A-small-attempt2.out");
    int T;
    fin>>T;
    string B[5];
    for(int t=1;t<=T;t++){
        int end=0,I=4,J=4;
        bool f=1;
        for(int i=0;i<4;i++){
            fin>>B[i];
            for(int j=0;j<4;j++){
                if(B[i][j]=='T'){
                    I=i;
                    J=j;
                }
                if(B[i][j]=='.'){
                    f=0;
                }
            }
        }
        B[I][J]='O';
        for(int i=0;i<4;i++){
            if(B[i][0]==B[i][1]&&B[i][1]==B[i][2]&&B[i][2]==B[i][3]){
                if(B[i][0]=='O')end=1;
                else if(B[i][0]=='X') end=-1;
            }
            if(B[0][i]==B[1][i]&&B[0][i]==B[2][i]&&B[0][i]==B[3][i]){
                if(B[0][i]=='O')end=1;
                else if(B[0][i]=='X') end=-1;
            }
        }
        if(B[0][0]==B[1][1]&&B[0][0]==B[2][2]&&B[0][0]==B[3][3]){
            if(B[0][0]=='O')end=1;
            else if(B[0][0]=='X') end=-1;
        }
        if(B[0][3]==B[1][2]&&B[0][3]==B[2][1]&&B[0][3]==B[3][0]){
            if(B[0][3]=='O')end=1;
            else if(B[0][3]=='X') end=-1;
        }
        B[I][J]='X';
        for(int i=0;i<4;i++){
            if(B[i][0]==B[i][1]&&B[i][1]==B[i][2]&&B[i][2]==B[i][3]){
                if(B[i][0]=='O')end=1;
                else if(B[i][0]=='X') end=-1;
            }
            if(B[0][i]==B[1][i]&&B[0][i]==B[2][i]&&B[0][i]==B[3][i]){
                if(B[0][i]=='O')end=1;
                else if(B[0][i]=='X') end=-1;
            }
        }
        if(B[0][0]==B[1][1]&&B[0][0]==B[2][2]&&B[0][0]==B[3][3]){
            if(B[0][0]=='O')end=1;
            else if(B[0][0]=='X') end=-1;
        }
        if(B[0][3]==B[1][2]&&B[0][3]==B[2][1]&&B[0][3]==B[3][0]){
            if(B[0][3]=='O')end=1;
        }
        if(end==1){
            fout<<"Case #"<<t<<": O won\n";
        }
        else if(end==-1){
            fout<<"Case #"<<t<<": X won\n";
        }
        else if(f==0){
            fout<<"Case #"<<t<<": Game has not completed\n";
        }
        else{
            fout<<"Case #"<<t<<": Draw\n";
        }
    }
    fout.close();
    fin.close();
    return 0;
}
