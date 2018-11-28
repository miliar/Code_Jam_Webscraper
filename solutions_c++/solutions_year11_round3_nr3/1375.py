#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <string.h>
#define MAXSIZE 100000
using namespace std;

bool search(char x1, char x2, char x3);

int main(int argc, char* argv[]){

    if (argc != 2){
        fprintf(stderr, "Usage: ./rpi [Input File]\n");
        return 1;
    }

    ifstream in(argv[1], ifstream:: in);
    ofstream out("notes.out", ofstream:: out);
    char buffer[MAXSIZE];

    in.getline(buffer, MAXSIZE);
    int cases = atoi(buffer);

    for (int i = 1; i <= cases; i++){

        in.getline(buffer, MAXSIZE);

        long players = atol(strtok(buffer, " "));
        long low = atol(strtok(NULL, " "));
        long high = atol(strtok(NULL, " "));


        long notes[players];
        in.getline(buffer, MAXSIZE);
        notes[0] = atol(strtok(buffer, " "));
        for (int j = 1; j < players; j++){
            notes[j] = atol(strtok(NULL, " "));
        }


        bool possible = true;
        int result = 0;


        for (int j = low; j <= high; j++){
            possible = true;
            for (int k = 0; k < players; k++){
                    if ( j% notes[k] != 0 && notes[k] % j != 0 ){
                        possible = false;
                    }
            }
           if(possible){
                result = j;
                break;
           }
        }
        if(possible){
            out << "Case #" << i << ": " << result << "\n";
        }
        else{
            out << "Case #"<< i << ": NO\n";
        }
    }

    return 0;
}
