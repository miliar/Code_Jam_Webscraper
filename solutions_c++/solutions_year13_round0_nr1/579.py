/*
Bismillahir Rahmanir Rahim
Coder: Ahmad Faiyaz
Problem: CodeJam Qualification 2013
*/

#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <fstream>

#define READ(f) {ifstream infile(f) ;if(infile.good()) freopen(f, "r", stdin);}
#define WRITE(f) freopen(f, "w", stdout)
#define DBG(vari) cerr<<#vari<<" = "<<(vari)<<endl;

using namespace std;

char grid [15][15];

int run (char p) {

    int j=0;
    int ok=1;
    for(int i=0;i<4;i++){
        if(grid[i][j]!='T' && grid[i][j]!=p) {
                ok=0;
        }
        j++;
    }
    if(ok) return 1;
    ok=1;
    j=3;
    for(int i=0;i<4;i++){
        if(grid[i][j]!='T' && grid[i][j]!=p) {
                ok=0;
        }
        j--;
    }
    if(ok) return 1;

    for(int i=0; i<4; i++) {
        int ok = 1;
        for(int j=0; j<4; j++) {
            if(grid[i][j]!='T' && grid[i][j]!=p) {
                ok=0;
            }
        }
        if(ok) return 1;
    }

    for(int j=0; j<4; j++) {
        int ok = 1;
        for(int i=0; i<4; i++) {
            if(grid[i][j]!='T' && grid[i][j]!=p) {
                ok=0;
            }
        }
        if(ok) return 1;
    }
    return 0;
}

int main() {
#if defined( faiyaz_pc )
    READ("A-large.in");
    WRITE("A_lar.txt");
#endif
    int t,chk=1;
    cin>>t;
    while(t--) {
        printf("Case #%d: ",chk++);
        int allfilled=1;
        for(int i=0; i<4; i++) {
            for(int j=0; j<4; j++) {
                cin>>grid[i][j];
                if(grid[i][j]=='.') {
                    allfilled=0;
                }
            }
        }


        int X = run ('X');
        int O = run ('O');


        if(X){
            printf("X won\n");
            continue;
        }
        if(O){
            printf("O won\n");
            continue;
        }
        if(allfilled){
            printf("Draw\n");
            continue;
        }

        printf("Game has not completed\n");


    }
    return 0;
}
