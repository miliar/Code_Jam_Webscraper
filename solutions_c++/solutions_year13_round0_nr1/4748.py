#include<iostream>
#include <fstream>

using namespace std;

int main() {
    int T;
    ofstream myfile;
    ifstream myReadFile;
    myReadFile.open("A-large.in");
    myfile.open ("Aoutput.txt");
    int caso=0, O1, X1, O2, X2, opciones, O3, X3, X4, O4;
    char mat[4][4];
    string pos[4];
    pos[0]="X won";
    pos[1]="O won";
    pos[2]="Draw";
    pos[3]="Game has not completed";
    myReadFile>>T;
    while(T--) {
        opciones=2;
        for(int i=0; i<4; i++) {
            for(int j=0; j<4; j++) {
                myReadFile>>mat[i][j];
                if(mat[i][j]=='.') {
                    opciones=3;
                }
            }
        }
        caso++;
        O3=0;
        X3=0;
        O4=0;
        X4=0;
        for(int i=0; i<4; i++) {
            O1=0;
            O2=0;
            X1=0;
            X2=0;
            for(int j=0; j<4; j++) {
                if(mat[i][j]=='O') {
                    O1++;
                }
                else if(mat[i][j]=='X'){
                    X1++;
                }
                else if(mat[i][j]=='T'){
                    O1++;
                    X1++;
                }
                if(mat[j][i]=='O') {
                    O2++;
                }
                else if(mat[j][i]=='X') {
                    X2++;
                }
                else if(mat[j][i]=='T'){
                    X2++;
                    O2++;
                }
            }
            if(O1==4||O2==4) {
                opciones=1;
            }
            if(X1==4||X2==4) {
                opciones=0;
            }
            if(mat[i][i]=='O') {
                O3++;
            }
            else if(mat[i][i]=='X') {
                X3++;
            }
            else if(mat[i][i]=='T') {
                X3++;
                O3++;
            }
            if(mat[3-i][i]=='O') {
                O4++;
            }
            else if(mat[3-i][i]=='X') {
                X4++;
            }
            else if(mat[3-i][i]=='T') {
                X4++;
                O4++;
            }
        }
        if(X3==4) {
            opciones=0;
        }
        if(O3==4) {
            opciones=1;
        }
        if(X4==4) {
            opciones=0;
        }
        if(O4==4) {
            opciones=1;
        }
        myfile<<"Case #"<<caso<<": "<<pos[opciones]<<endl;
    }
    myfile.close();
    return 0;
}
