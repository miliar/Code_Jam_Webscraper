//
//  main.cpp
//  CodeJam1
//
//  Created by Zulkarnine Mahmud on 4/13/13.
//  Copyright (c) 2013 Zulkarnine Mahmud. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include <fstream>
#include <iomanip>
#include "math.h"
#include <algorithm>
#include <vector>
#include <string>
#include <array>

using namespace std;
char board[4][4];
char personX='X';
char personO='O';
char valueT='T';

string TrueFalse(bool b){
    return (b? "true":"false");

}

bool calculateHorizontal(char A,char T){
    int total=0;
    for (int i=0; i<4; i++) {
        int instances=0;
        for (int j=0; j<4; j++) {
            instances=((board[i][j]==A||board[i][j]==T)? ++instances:instances);
        }
            
        
        total=instances;
        //cout<<total<<endl;

        if (total==4) {
            return true;
    
        }
    }
    return false;
}

bool calculateVertical(char A,char T){
    int total=0;
    for (int i=0; i<4; i++) {
        int instances=0;
        for (int j=0; j<4; j++) {
            instances=((board[j][i]==A||board[j][i]==T)? ++instances:instances);
        }
        total=instances;
        if (total==4) {
            //cout<<total<<endl;
            return true;
            
        }
    }
    return false;
}

bool calculateDiagonal(char A,char T){
    int total=0;
    for (int i=0; i<4; i++) {
        total=((board[i][i]==A||board[i][i]==T)? ++total:total);
        //cout<<total<<endl;

        
    }
    if (total==4) {
        
        return true;
        
    }else{
        total=0;
        for (int i=0; i<4; i++) {
            //cout<<total<<endl;

            total=((board[0+i][3-i]==A||board[0+i][3-i]==T)? ++total:total);
            
        }
        if (total==4) {
            return true;
        }
    
    }
    return false;
}

bool calculateAlPossible(char A,char T){
    bool value;
    value=((calculateHorizontal(A, T)==true||calculateVertical(A, T)==true||calculateDiagonal(A, T)==true)? true:false);
    return value;
}
bool checkDraw(){

    for (int i=0; i<4; i++) {
        for (int j=0; j<4; j++) {
            if (board[i][j]=='.') {
                return false;
            }
        }
    }
    return true;

}

int solveCase(){
    if (calculateAlPossible(personX, valueT)) {
        return 1;
    }else if (calculateAlPossible(personO, valueT)) {
        return 2;
    }else if (checkDraw()){
        return 3;
    }else return 4;

}
string statement(int a){
    string s;
    switch (a) {
        case 1:
            s="X won";
            break;
        case 2:
            s="O won";
            break;
        case 3:
            s="Draw";
            break;
        case 4:
            s="Game has not completed";
            break;
            
        default:
            s="error";
            break;
    }
    return s;
}


int main(){

    freopen("A-large.in", "r", stdin);
    freopen("1_2.out", "w", stdout);
    int T;
    cin>>T;
    for (int cas=1; cas<=T; cas++) {
        for (int l=0; l<4; l++) {
            for (int m=0; m<4; m++) {
                cin>>board[l][m];
            }
        }
        /*for (int l=0; l<4; l++) {
            for (int m=0; m<4; m++) {
                cout<<board[l][m];
            }
            cout<<endl;
        }*/
        cout<<"Case #"<<cas<<": "<<statement(solveCase())<<endl;
         
        
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
    
}

    

