/*
Autor: Luis Argüelles
*/

#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <string.h>
#define MAXSIZE 100000
using namespace std;

int menor(int array[],int limit);

int main(int argc, char *argv[]){

    if(argc < 2){
        cout << "Invalid Argmuent" << endl;
        return -1;
    }

    ifstream in(argv[1], ifstream:: in);
    ofstream out("splitting.out", ofstream::out);

    // Se Lee el numero de casos...

    int cases;
    char buff[MAXSIZE];
    in.getline(buff, MAXSIZE);
    cases = atoi(buff);

    for (int i= 1; i <= cases; i++){
        //Ahora se lee el numero de dulces...
        int candies;
        in.getline(buff, MAXSIZE);
        candies = atoi(buff);
        int candArray[candies];
        char *temp;
        in.getline(buff, MAXSIZE);
        temp = strtok(buff, " ");
        int possible = 0, suma = 0;
        //Ahora se leen los valores de los dulces...
        for (int j= 0; j< candies; j++){
            candArray[j] = atoi(temp);
            temp = strtok(NULL, " ");
            possible = possible^candArray[j];
            suma += candArray[j];
        }
        if(possible == 0){
            suma -= menor(candArray, candies);
            out << "Case #" << i <<": " << suma << endl;
        }
        else{
            out <<"Case #" << i << ": NO" << endl;

        }


    }
    return 0;
}

int menor(int array[], int limit){
    int temp = array[0];
    for (int i = 1; i < limit; i++){
        if(temp > array[i])
            temp = array[i];
    }
    return temp;
}
