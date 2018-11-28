#include <fstream>
#include <sstream>
#include <iostream>
#include <cstring>

using namespace std;

int main(){
    ifstream cin("in.txt");
    ofstream cout("out.txt");
    int n;
    cin >> n;
    for(int i=0; i < n ; i++){
            bool x = false, o= false, incomp = false;
            char mat[4][4];
            char filas[4];
            char columnas[4];
            bool init1[4];
            memset(init1, false, sizeof(init1));
            bool init2[4];
            memset(init2, false, sizeof(init2));
            for(int j=0; j < 4 ; j++){
                    for(int k=0; k < 4 ; k++){
                            cin >> mat[j][k];
                            if(mat[j][k]=='.'){
                                incomp = true;
                            }
                            if(!init1[j]){
                                if (mat[j][k]!='T'){
                                    filas[j] = mat[j][k];
                                    init1[j] = true;
                                }
                            }
                            if(!init2[k]){
                                if (mat[j][k]!='T'){
                                    columnas[k] = mat[j][k];
                                    init2[k] = true;
                                }
                            }
                            if(mat[j][k]!=filas[j]){
                                 if(mat[j][k]!='T'){
                                     filas[j] ='-';
                                 }
                            }
                            if(mat[j][k]!=columnas[k]){
                                 if(mat[j][k]!='T'){
                                     columnas[k] ='-';
                                 }
                            }
                    }
                    if(filas[j] != '-'){
                        if(filas[j] == 'X'){
                            x=true;
                        }else if(filas[j] == 'O'){
                            o=true;
                        }
                    }
            }

            for(int k=0; k < 4 ; k++){
                if(columnas[k] != '-'){
                    if(columnas[k] == 'X'){
                        x=true;
                    }else if(columnas[k] == 'O'){
                        o=true;
                    }
                }
            }

            char diag[2];
            bool init3[2];
            memset(init3, false, sizeof(init3));
            for(int k=0; k < 4 ; k++){
                if(!init3[0]){
                    if(mat[k][k]!='T'){
                        diag[0] = mat[k][k];
                        init3[0] = true;
                    }
                }
                if(!init3[1]){
                    if(mat[(3-k)][k]!='T'){
                        diag[1] = mat[(3-k)][k];
                        init3[1] = true;
                    }
                }
                if(mat[k][k]!=diag[0]){
                    if(mat[k][k]!='T'){
                        diag[0] = '-';
                    }
                }
                if(mat[(3-k)][k]!=diag[1]){
                    if(mat[(3-k)][k]!='T'){
                        diag[1] = '-';
                    }
                }

            }
            if(diag[0] != '-'){
                if(diag[0] == 'X'){
                    x=true;
                }else if(diag[0] == 'O'){
                    o=true;
                }
            }
            if(diag[1] != '-'){
                if(diag[1] == 'X'){
                    x=true;
                }else if(diag[1] == 'O'){
                    o=true;
                }
            }

            cout << "Case #" << i+1 << ": ";
            if(x){
                cout << "X won" << endl;
            }else if(o){
                cout << "O won" << endl;
            }else if(incomp){
                cout << "Game has not completed" << endl;
            }else{
                cout << "Draw" << endl;
            }


    }
}
