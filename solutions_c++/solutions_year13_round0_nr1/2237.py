#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <math.h>
#include <fstream>

using namespace std;

ifstream fin ("tictac-large.in");
ofstream fout ("tictac.out");

int main() {
    int n;
    fin>>n;
    for(int i=0;i<n;i++) {
        int board[4][4] = {{0,0,0,0},{0,0,0,0},{0,0,0,0},{0,0,0,0}};
        // . T X O
        int rows[4][4] = {{0,0,0,0},{0,0,0,0},{0,0,0,0},{0,0,0,0}};
        int cols[4][4] = {{0,0,0,0},{0,0,0,0},{0,0,0,0},{0,0,0,0}};
        int diags[2][4] = {{0,0,0,0},{0,0,0,0}};
        for(int r=0;r<4;r++)
            for(int c=0;c<4;c++){
                char k;
                fin>>k;
                if(k=='X'){
                    rows[r][2]++;
                    cols[c][2]++;
                    if(r==c) 
                        diags[0][2]++;
                    if(r==3-c)
                        diags[1][2]++;
                }
                else if(k=='O') {
                    rows[r][3]++;
                    cols[c][3]++;
                    if(r==c) 
                        diags[0][3]++;
                    if(r==3-c)
                        diags[1][3]++;
                }
                else if(k=='T') {
                    rows[r][1]++;
                    cols[c][1]++;
                    if(r==c) 
                        diags[0][1]++;
                    if(r==3-c)
                        diags[1][1]++;
                }
                else {
                    rows[r][0]++;
                    cols[c][0]++;
                    if(r==c) 
                        diags[0][0]++;
                    if(r==3-c)
                        diags[1][0]++;
                }
            }
        bool done = true;
        bool checker = false;
        for(int r=0;r<4;r++){
            if(checker)
                break;
            if(rows[r][0]>0 || cols[r][0]>0){
                done = false;
            }
            if(rows[r][2]==4 || cols[r][2]==4 || diags[0][2]==4 || diags[1][2]==4) {
                fout<<"Case #"<<i+1<<": X won"<<endl;
                checker=true;
            }
            else if(rows[r][3]==4 || cols[r][3]==4 || diags[0][3]==4 || diags[1][3]==4) {
                fout<<"Case #"<<i+1<<": O won"<<endl;
                checker=true;

            }
            else if((rows[r][2]==3 && rows[r][1]==1) || (cols[r][2]==3 && cols[r][1]==1) || 
                    (diags[0][2]==3 && diags[0][1]==1) || (diags[1][2]==3 && diags[1][1]==1)) {
                fout<<"Case #"<<i+1<<": X won"<<endl;
                checker=true;
            }
            else if((rows[r][3]==3 && rows[r][1]==1) || (cols[r][3]==3 && cols[r][1]==1) ||
                    (diags[0][3]==3 && diags[0][1]==1) || (diags[1][3]==3 && diags[1][1]==1)) {
                fout<<"Case #"<<i+1<<": O won"<<endl;
                checker=true;
            }
        }
        if(!checker) {
            if(done)
                fout<<"Case #"<<i+1<<": Draw"<<endl; 
            else
                fout<<"Case #"<<i+1<<": Game has not completed"<<endl;
        }
      

    }
}
