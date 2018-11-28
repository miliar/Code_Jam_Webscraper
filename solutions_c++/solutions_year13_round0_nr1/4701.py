/* 
 * File:   main.cpp
 * Author: tamer
 *
 * Created on April 13, 2013, 2:03 AM
 */

#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

/*
 * 
 */
int  check(vector< vector <char> > & matrix);
void readSquare(char c,int&x, int&o, int&t, int&dot);

int main(int argc, char** argv) {

    int N=4,M=4,T;
    char ch;
    
    char str [80];
    FILE * pFile;
    FILE * oFile;    
    
    pFile = fopen ("/Users/tamer/Desktop/A-large.in","r");
    oFile = fopen ("/Users/tamer/Desktop/out.txt","w+");
    fscanf (pFile, "%d\n", &T);
    
    for(int t=1;t<=T;t++){
        vector< vector <char> > lawn =   vector< vector<char> >(N, vector<char>(M,'.'));
        for(int n=0;n<N;n++){
            for(int m=0;m<M;m++){
                fscanf (pFile, "%c", &lawn[n][m]);
//                cout<< lawn[n][m]<< " ";
            }
            fscanf(pFile, "%c", &ch );
//            cout<<endl;
        }
        //read separating new line
        fscanf(pFile, "%c", &ch );

        switch(check(lawn)){
            case 1:
                fprintf (oFile, "Case #%d: X won\n", t);
                break;                            
            case 2:
                fprintf (oFile, "Case #%d: O won\n", t);
                break;                            
            case 3:
                fprintf (oFile, "Case #%d: Draw\n", t);
                break;                            
            case 4:
                fprintf (oFile, "Case #%d: Game has not completed\n", t);
                break;                            
        }
    }
    fclose (oFile);
    fclose (pFile);
    return 0;
}


int check(vector< vector <char> > & matrix) {


    int x = 0, o = 0, t = 0, dot = 0;
    //check rows
    for (int i = 0; i < 4; i++) {
        x = o = t = 0;
        for (int j = 0; j < 4; j++) {
            readSquare(matrix[i][j],x,o,t,dot);
        }
        //x won
        if (x == 4 || (x == 3 && t == 1))
            return 1;
        //o won
        if (o == 4 || (o == 3 && t == 1))
            return 2;
    }

    //check columns
    for (int j = 0; j < 4; j++) {
        x = o = t = 0;
        for (int i = 0; i < 4; i++) {
            readSquare(matrix[i][j],x,o,t,dot);
        }
        //x won
        if (x == 4 || (x == 3 && t == 1))
            return 1;
        //o won
        if (o == 4 || (o == 3 && t == 1))
            return 2;
    }

    //check diagonals
    x = o = t = 0;
    for (int i = 0; i < 4; i++) {
        readSquare(matrix[i][i],x,o,t,dot);
    }
    //x won
    if (x == 4 || (x == 3 && t == 1))
        return 1;
    //o won
    if (o == 4 || (o == 3 && t == 1))
        return 2;

    x = o = t = 0;
    for (int i = 0; i < 4; i++) {
        readSquare(matrix[i][3 - i],x,o,t,dot);
    }
    //x won
    if (x == 4 || (x == 3 && t == 1))
        return 1;
    //o won
    if (o == 4 || (o == 3 && t == 1))
        return 2;

    //Nobody won:

    //incomplete
    if (dot > 0)
        return 4;
    //draw
    return 3;
}

void readSquare(char c,int&x, int&o, int&t, int&dot){
    switch (c) {
            case 'X':
                x++;
                break;
            case 'O':
                o++;
                break;
            case 'T':
                t++;
                break;
            case '.':
                dot++;
                break;
        } 
}