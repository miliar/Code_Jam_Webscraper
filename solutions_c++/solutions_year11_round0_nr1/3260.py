#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <string.h>
#define MAXSIZE 1000
using namespace std;

int main(int argc, char* argv[]){

    if (argc != 2){
        cout << "Falta el archivo de entrada"<< endl;
        return -1;
    }
    ifstream in(argv[1], ifstream::in);
    ofstream out("result.out", ofstream:: out);
    int cases;
    char buff[MAXSIZE];
    // Primero se lee el numero de casos ...
    in.getline(buff, 10);
    cases = atoi(buff);
    // Con el numero de casos se inicia el ciclo ....
    for (int i = 1; i <= cases; i++){

        int numButtons;
        in.getline(buff, MAXSIZE);
        numButtons = atoi(strtok(buff," "));
        int OrangeB[numButtons];
        // Se inician los contadores del trabajo asigando a cada robot....
        int orangeCont = 0, blueCont = 0;
        // Se inician las posiciones de los Robots...
        int BluePos = 1, OrangePos = 1;
        // Se inicia el contador del tiempo ...
        int segs = 0;
        // Se inicia el contador de los botones presionados..
        int Bpressed = 0, Opressed = 0, Gpressed = 0;
        int BlueB[numButtons];
        char* order[numButtons];

        for (int j = 0 ; j < numButtons ; j++){
                order[j] = (strtok(NULL," "));
            if (strcmp(order[j],"O") == 0){
                OrangeB[orangeCont] = atoi(strtok(NULL," "));
                orangeCont++;
            }
            else if(strcmp(order[j], "B") == 0){
                BlueB[blueCont] = atoi(strtok(NULL, " "));
                blueCont++;
            }
        }
        // Mientras quede trabajo por hacer ....
        bool turno;
        while (blueCont +orangeCont > 0 ){
            turno = true;
            if (orangeCont > 0){
                if (OrangePos == OrangeB[Opressed]){
                    if (strcmp(order[Gpressed], "O") == 0 && turno){
                        Opressed++; Gpressed++; orangeCont--;
                        // Indica que ya se gasto el turno ...
                        turno = false;
                    }
                }
                // Se mueve un paso en la direccion que corresponda
                else{
                    if (OrangePos < OrangeB[Opressed])
                        OrangePos++;
                    else
                        OrangePos--;
                    }
            }
            if (blueCont > 0){
                    if (BluePos == BlueB[Bpressed]){
                        if (strcmp(order[Gpressed], "B") == 0 && turno){
                            Bpressed++; Gpressed++; blueCont--;
                            // Indica que ya se gasto el turno ...
                            //return 3;
                            turno = false;
                        }
                    }
                    // Se mueve un paso en la direccion que corresponda
                    else{
                        if (BluePos  < BlueB[Bpressed])
                            BluePos++;
                        else
                            BluePos--;
                    }
            }
            segs++;
        }
        out << "Case #" << i << ": " << segs << endl;
    }
    return 0;
}
