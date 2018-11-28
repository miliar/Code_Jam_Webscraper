/* BEGIN_OF_SOURCE_CODE */
#include <iostream>
#include <fstream>
#include <sstream>  

#include <cstring> //for memset
#include <cstdio>
#include <cmath>

#include <algorithm>
#include <numeric>
#include <iterator>

#include <vector>
#include <list>
#include <string>

#include <queue>
#include <stack>

#include <utility>
#include <map>
#include <set>
#include <iomanip> //??

#define REP(i,n) for(int i=0;i<(n);++i) 

using namespace std; //change 

const int dimesion = 4;
int T;
char maps[6][6];


bool Xwon(char *str) {

    if(!strcmp(str, "XXXX") || 
            !strcmp(str, "XXXT") || 
            !strcmp(str, "XXTX") || 
            !strcmp(str, "XTXX") || 
            !strcmp(str, "TXXX") 
      ) 
    return true;

    return false;
}



bool Owon(char *str) {

    if(!strcmp(str, "OOOO") || 
            !strcmp(str, "OOOT") || 
            !strcmp(str, "OOTO") || 
            !strcmp(str, "OTOO") || 
            !strcmp(str, "TOOO") 
      ) 
        return true;

    return false;
}



void gao() {
    bool filled = true;
    for(int i = 0; filled && i < dimesion; ++i)
        for(int j = 0; filled && j < dimesion; ++j)
            if('.' == maps[i][j]) filled = false;

    char cand[5];
    //if X won
    cand[4] = '\0';
    for(int i = 0; i < dimesion; ++i) {
        for(int j = 0; j < dimesion; ++j) cand[j] = maps[i][j];
        
        if( Xwon(cand) ) {
            cout<<"X won"<<endl;
            return ;
        }
 
        if( Owon(cand) ) {
            cout<<"O won"<<endl;
            return ;
        }
    }

    for(int i = 0; i < dimesion; ++i) {
        for(int j = 0; j < dimesion; ++j) cand[j] = maps[j][i];

        if( Xwon(cand) ) {
            cout<<"X won"<<endl;
            return ;
        }

        if( Owon(cand) ) {
            cout<<"O won"<<endl;
            return ;
        }
    }

    for(int i = 0; i < dimesion; ++i)  cand[i] = maps[i][i];
    if( Xwon(cand) ) {
        cout<<"X won"<<endl;
        return ;
    }

    if( Owon(cand) ) {
        cout<<"O won"<<endl;
        return ;
    }

    for(int i = 0; i < dimesion; ++i)  cand[i] = maps[i][3-i];
    if( Xwon(cand) ) {
        cout<<"X won"<<endl;
        return ;
    }

    if( Owon(cand) ) {
        cout<<"O won"<<endl;
        return ;
    }


    //draw or not over yet
    if(filled) cout<<"Draw"<<endl;
    else cout<<"Game has not completed"<<endl;
    return ;
}

int main(void) {
    cin>>T;
    for(int i = 1; i <= T; ++i)  {
        cout<<"Case #"<<i<<": ";

        for(int j = 0; j < dimesion; ++j)
            for(int k = 0; k < dimesion; ++k)
                cin>>maps[j][k];

        gao();
    }
    return 0;
}
