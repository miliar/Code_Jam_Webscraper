#include <iostream>
#include <fstream>
#include <new>

using namespace std;

char currentletter = 'a';
int **altitudes;
char **salida;
char acomoda(int i,int j);
int row, col;

int main(){
    int i ,j , casenumber, casos;
    char dummy;


    casenumber = 1;
    fstream input;
	input.open("watersheds.in");
    freopen("watersheds.out","w",stdout);
    
    input >> casos;
        
    for(casenumber = 1;casenumber <= casos;casenumber++){
        // Creando los arreglos
        input >> row >> col;
        cout << "Case #" << casenumber << ":\n";
        altitudes = new int*[row];
        salida = new char*[row];
        for(i = 0;i<row;++i){
            altitudes[i] = new int[col];
            salida[i] = new char[col];
        }
        // Leyendo el arreglo de numeros y de blancos el de letras
        for(i = 0;i<row;i++){
            for(j = 0;j<col;j++){
                input >> altitudes[i][j];
                salida[i][j] = ' ';
            }
        }
   
        // Llenando de letras
        for(i = 0;i<row;i++){
            for(j = 0;j<col;j++){
                dummy = acomoda(i,j);
            }
        }
        
        // Imprimiendo el arreglo
        for(i = 0;i<row;i++){
            for(j = 0;j<col;j++){
                cout << salida[i][j] << " ";
            }
            cout << "\n";
        }
        currentletter = 'a';
   }

    //cout << casos;
    
    
}





char acomoda(int i,int j){
    int menor;
    if(salida[i][j] == ' '){
        //Busca a donde corre
        menor = 0;
        if(i > 0){
            if(altitudes[i][j] > altitudes[i-1][j]){
                menor = 1;
            }
        }
        if(j > 0){
            if(altitudes[i][j] > altitudes[i][j-1]){
                if(menor == 1){
                    if(altitudes[i-1][j] > altitudes[i][j-1]){
                        menor = 2;
                    }
                }else{
                    menor = 2;
                }
            }
        }
        if(j < (col-1)){
            if(altitudes[i][j] > altitudes[i][j + 1]){
                if(menor == 1){
                    if(altitudes[i-1][j] > altitudes[i][j+1]){
                        menor = 3;
                    }
                }else if(menor == 2){
                    if(altitudes[i][j-1] > altitudes[i][j+1]){
                        menor = 3;
                    }
                }else{
                    menor = 3;
                }
            }
        }
        if(i < (row - 1)){
            if(altitudes[i][j] > altitudes[i+1][j]){
                if(menor == 1){
                    if(altitudes[i-1][j] > altitudes[i+1][j]){
                        menor = 4;
                    }
                }else if(menor == 2){
                    if(altitudes[i][j-1] > altitudes[i+1][j]){
                        menor = 4;
                    }
                }else if(menor == 3){
                    if(altitudes[i][j+1] > altitudes[i+1][j]){
                        menor = 4;
                    }
                }else{
                    menor = 4;
                }
            }
        }
        // He hencontrado a donde corre
        if(menor == 0){
            salida[i][j] = currentletter;
            currentletter++;
        }else if(menor == 1){
            salida[i][j] = acomoda(i-1,j);
        }else if(menor == 2){
            salida[i][j] = acomoda(i,j-1);
        }else if(menor == 3){
            salida[i][j] = acomoda(i,j+1);
        }else if(menor == 4){
            salida[i][j] = acomoda(i+1,j);
        }
    }
    return salida[i][j];
}
