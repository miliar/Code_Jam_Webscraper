/*
Autor : Luis Argüelles
*/

#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <string.h>
#include <string>
#define MAXSIZE 1000
#define length(x) (sizeof(x)/sizeof(x[0]))
using namespace std;

char combined( char pair[], char array[][3]);
bool existOppossed(char result[], char array[][2], int tam);

int main(int argc, char* argv[]){
    if (argc < 2){
        cout << "Invalid argument" << endl;
        return -1;
    }
    char buff[MAXSIZE];
    int cases;
    ifstream in(argv[1], ifstream:: in);
    ofstream out("result.out", ofstream:: out);
    in.getline(buff, 10);
    cases = atoi(buff);

    // Comienza el ciclo con el Numero de casos...
    for (int i = 1 ; i <= cases; i++){
        // Se lee la linea correspondiente....
        in.getline(buff, MAXSIZE);
        int combines = atoi(strtok(buff," "));
        //char* combArray[combines];
        char combinesArray[combines][3];
        for (int j = 0 ; j < combines; j++){
            string temp = strtok(NULL, " ");
            strcpy(combinesArray[j], temp.c_str());
        }
        // Se lee el numero de combinaciones que se oponen a todo ...
        int opposed = atoi(strtok(NULL," "));

        char opposedArray[opposed][2];
        // Se leen las combinaciones de opposed...
        for (int j = 0; j < opposed ; j++){
            string temp = strtok(NULL, " ");
            strcpy(opposedArray[j],temp.c_str()) ;
        }
        // Ahora se lee la longitud de la entrada a procesar...
        int size = atoi(strtok(NULL, " "));
        //Ahora se lee la entrada ...
        string entry;
        entry = strtok(NULL," ");
        char cEntry[size];
        strcpy(cEntry, entry.c_str());

        // Ahora se inicia con el procesamiento de la entrada....
        //Se crea un arreglo para guerdar la salida...
        char result[size];
        //Se crea un contador de inserciones a la salida ...
        int contResult = 0;
        char pair[2];
        char transform;
        for (int j = 0 ; j < size; j++){
            //Se agrega un caracter a la salida...
            result[contResult] = cEntry[j];
            contResult++;
            if (contResult > 1){
                //Se guarda la ultima pareja de caracteres ......
                  pair[0] = result[contResult-2];
                  pair[1] = result[contResult -1];
                // Ahora se mira si es una combinacion...
                //Si existe se borra el ultimo elemento y se pone la tranformacion en el penultimo...
                transform = combined(pair, combinesArray);
                if (transform != ' '){
                    result[contResult -1] = 0;
                    result[contResult - 2] = transform;
                    contResult--;
                }
                // Ahora se mira si existe un "opposed" y se borra la pila en caso de
                // ser necesario....
                if (existOppossed(result, opposedArray , contResult)){
                    //Se limpia el arreglo y se reinicia el contador..
                    memset(&result, 0, size);
                    contResult = 0;
                }
            }
        }
        //Se imprime el resultado al archivo...
        out << "Case #"<< i<< ": [";
        for (int k = 0 ; k < contResult -1; k++)
            out << result[k] <<", ";
        if (contResult)
            out << result[contResult -1];
            out << "]" << endl;


    }
    return 0;
}

// Mira si existe una combinacion y devuelve la tranformacion
// Si no existe devuelve el caracter espacio (' ')...
char combined( char pair[], char array[][3]){
        for( int i = 0; i< length(array); i++){
            if((pair[0] == array[i][0] && pair[1] == array[i][1]) || (pair[0] == array[i][1] && pair[1]== array[i][0]))
                return array[i][2];
        }
        return ' ';
}

// Verifica si existe una combinacion "opposed" en el resultado ...
bool existOppossed(char result[], char array[][2], int tam){
    char first;
    for (int i = 0 ; i < length(array) ; i ++){
        first = 0;
        for(int j= 0 ; j < tam ; j++){
            if (result[j] == array[i][0] || result[j] == array[i][1])
                if (first == 0)
                    first = result[j];
                else{
                    if (result[j] != first)
                        return true;
                }
        }
    }
    return false;
}
