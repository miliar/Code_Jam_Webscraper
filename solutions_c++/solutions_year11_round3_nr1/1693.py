#include <stdio.h>
#include <stdlib.h>
#include <string> 
#include <iostream>
#include <queue>

using namespace std;


int main(void)
{
    
    int casos;
    int c = 1;

    cin >> casos;

    while(casos){
        int alt;
        int wid;
        
        cin >> alt;
        cin >> wid;

        int dat[100][100] = {{0}};
        string temp;
        int cuantosG = 0;

        for (int i = 0; i < alt; i++) {
            cin >> temp;
            for (int y = 0; y < wid; y++) {
                if(temp[y] == '.'){
                    dat[i][y] = 0;
                }
                else{
                    dat[i][y] = 1;
                    cuantosG++;
                }
            }
        }

        for(int i = 0; i < alt; i++){
            for (int y = 0; y < wid; y++) {
                if(dat[i][y] == 1){
                    if(dat[i+1][y]==1 && dat[i][y+1]==1 && dat[i+1][y+1]==1){
                        dat[i][y+1] = 3;
                        dat[i+1][y+1] = 2;
                        dat[i+1][y] = 3;
                        dat[i][y] = 2;
                        cuantosG=cuantosG-4;
                    }
                }
            }
        }

        if(cuantosG){
            cout << "Case #" << c << ": " <<  "\nImpossible" << endl;
        }
        else{
            cout << "Case #" << c << ":" << endl;
            for(int i = 0; i < alt; i++){
                for (int y = 0; y < wid; y++) {
                    if(dat[i][y] == 0)
                        cout << ".";
                    else if(dat[i][y] == 2)
                        cout << "/";
                    else
                        cout << "\\";
                }
                cout << endl;
            }
        }

        casos--; 
        c++;
    }

    return 0;
}
