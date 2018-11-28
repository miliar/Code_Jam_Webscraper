#include <algorithm>
#include <iostream>
#include <vector>
#include <numeric>
#include <stdio.h>
using namespace std;

int main(){
    char data[4][4];
    int T;
    int count;
    bool xWin;
    bool oWin;
    bool isDot;
    cin >> T;
    for (int z = 0; z < T; z++){
        xWin = false;
        oWin = false;
        isDot = false;
        for(int i = 0; i < 4; i ++){
            for(int j = 0; j < 4; j++){
                cin >> data[i][j];
                if(data[i][j]== '.')
                    isDot = true;
            }
        }

        count = 0;
        for(int i = 0; i < 4; i++){
            if(data[0][i]== 'X' || data[0][i]=='T')
                count++;
        }
        if(count == 4){
            xWin = true;
        }
        count = 0;
        for(int i = 0; i < 4; i++){
            if(data[1][i]== 'X' || data[1][i]=='T')
                count++;
        }
        if(count == 4){
            xWin = true;
        }
        count = 0;
        for(int i = 0; i < 4; i++){
            if(data[2][i]== 'X' || data[2][i]=='T')
                count++;
        }
        if(count == 4){
            xWin = true;
        }
        count = 0;
        for(int i = 0; i < 4; i++){
            if(data[3][i]== 'X' || data[3][i]=='T')
                count++;
        }
        if(count == 4){
            xWin = true;
        }



        count = 0;
        for(int i = 0; i < 4; i++){
            if(data[i][0]== 'X' || data[i][0]=='T')
                count++;
        }
        if(count == 4){
            xWin = true;
        }
        count = 0;
        for(int i = 0; i < 4; i++){
            if(data[i][1]== 'X' || data[i][1]=='T')
                count++;
        }
        if(count == 4){
            xWin = true;
        }
        count = 0;
        for(int i = 0; i < 4; i++){
            if(data[i][2]== 'X' || data[i][2]=='T')
                count++;
        }
        if(count == 4){
            xWin = true;
        }


        count = 0;
        for(int i = 0; i < 4; i++){
            if(data[i][3]== 'X' || data[i][3]=='T')
                count++;
        }
        if(count == 4){
            xWin = true;
        }


        count = 0;
        for(int i = 0; i < 4; i++){
            if(data[i][i]== 'X' || data[i][i]=='T')
                count++;
        }
        if(count == 4){
            xWin = true;
        }

        count = 0;
        for(int i = 0; i < 4; i++){
            if(data[i][3-i]== 'X' || data[3][3-i]=='T')
                count++;
        }
        if(count == 4){
            xWin = true;
        }





        count = 0;
        for(int i = 0; i < 4; i++){
            if(data[0][i]== 'O' || data[0][i]=='T')
                count++;
        }
        if(count == 4){
            oWin = true;
        }
        count = 0;
        for(int i = 0; i < 4; i++){
            if(data[1][i]== 'O' || data[1][i]=='T')
                count++;
        }
        if(count == 4){
            oWin = true;
        }
        count = 0;
        for(int i = 0; i < 4; i++){
            if(data[2][i]== 'O' || data[2][i]=='T')
                count++;
        }
        if(count == 4){
            oWin = true;
        }
        count = 0;
        for(int i = 0; i < 4; i++){
            if(data[3][i]== 'O' || data[3][i]=='T')
                count++;
        }
        if(count == 4){
            oWin = true;
        }



        count = 0;
        for(int i = 0; i < 4; i++){
            if(data[i][0]== 'O' || data[i][0]=='T')
                count++;
        }
        if(count == 4){
            oWin = true;
        }
        count = 0;
        for(int i = 0; i < 4; i++){
            if(data[i][1]== 'O' || data[i][1]=='T')
                count++;
        }
        if(count == 4){
            oWin = true;
        }
        count = 0;
        for(int i = 0; i < 4; i++){
            if(data[i][2]== 'O' || data[i][2]=='T')
                count++;
        }
        if(count == 4){
            oWin = true;
        }


        count = 0;
        for(int i = 0; i < 4; i++){
            if(data[i][3]== 'O' || data[i][3]=='T')
                count++;
        }
        if(count == 4){
            oWin = true;
        }


        count = 0;
        for(int i = 0; i < 4; i++){
            if(data[i][i]== 'O' || data[i][i]=='T')
                count++;
        }
        if(count == 4){
            oWin = true;
        }

        count = 0;
        for(int i = 0; i < 4; i++){
            if(data[i][3-i]== 'O' || data[3][3-i]=='T')
                count++;
        }
        if(count == 4){
            oWin = true;
        }


        cout << "Case #" << z+1 << ": ";

        if(oWin && xWin){
            cout << "Draw" << endl;
        }
        else if(oWin){
            cout << "O won" << endl;
        }
        else if(xWin){
            cout << "X won" << endl;
        }
        else if(isDot){
            cout << "Game has not completed" << endl;
        }
        else//draw
            cout << "Draw" << endl;

    }

}
