#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <string.h>
#define MAXSIZE 1000
using namespace std;

bool search(char x1, char x2, char x3);

int main(int argc, char* argv[]){

    if (argc != 2){
        fprintf(stderr, "Usage: ./rpi [Input File]\n");
        return 1;
    }

    ifstream in(argv[1], ifstream:: in);
    ofstream out("bluetiles.out", ofstream:: out);
    char buffer[MAXSIZE];

    in.getline(buffer, MAXSIZE);
    int cases = atoi(buffer);

    for (int i = 1; i <= cases; i++){

        in.getline(buffer, MAXSIZE);
        int rows = atoi(strtok(buffer, " "));
        int columns = atoi(strtok(NULL, " "));
        char picture[rows][columns];
        for (int j = 0; j < rows; j++){
            in.getline(buffer, MAXSIZE);
            for (int k = 0; k < columns; k ++){
                picture[j][k] = buffer[k];

            }

        }
        bool possible;
        possible = true;

        for (int j= 0; j < rows; j++){
            for (int k = 0; k < columns; k++){
                 if(possible){
                    if(picture[j][k] == '#'){

                        if(k < columns-1  && j < rows -1){
                            possible = search(picture[j+1][k], picture[j][k+1], picture[j+1][k+1]);
                            picture[j][k] = '/'; picture[j+1][k] = 92; picture[j][k+1] = 92; picture[j+1][k+1] = '/';
                        }
                        else if (k == columns-1 && j < rows -1 ){
                            possible = search(picture[j+1][k], picture[j][k-1], picture[j+1][k-1]);
                        }
                        else if (k < columns-1 && j== rows-1 ){
                            possible = search(picture[j-1][k], picture[j][k+1], picture[j-1][k+1]);
                        }
                        else if(k == columns -1 && j == rows -1){
                            possible = search(picture[j-1][k], picture[j][k-1], picture[j-1][k-1]);
                        }
                    }
                 }
            }
        }
        if (possible){
            out << "Case #" << i << ":\n";
            for (int j = 0; j < rows; j++){
                for (int k = 0; k < columns; k++){
                    out << picture[j][k];
                }
                out << "\n";
            }
        }
        else{
            out << "Case #" << i << ":\n";
            out <<"Impossible\n";
        }
    }

    return 0;
}

bool search(char x1, char x2, char x3){

    if (x1 == '#' && x2 == '#' && x3 == '#')
        return true;
    return false;
}
