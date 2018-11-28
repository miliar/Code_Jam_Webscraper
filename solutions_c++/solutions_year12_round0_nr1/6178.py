#include <iostream>
#include <stdio.h>
#include <string.h>
#include <fstream>
using namespace std;
int main(int argc, char** argv) {
	char abc [30] = { 'y' , 'h' , 'e' , 's' , 'o', 'c', 'v' , 'x', 'd', 'u', 'i' , 'g' , 'l', 'b', 'k'
        , 'r' , 'z', 't' , 'n', 'w' , 'j' , 'p', 'f' , 'm' , 'a' , 'q'};
	int n, i;
        ofstream salida;
        ifstream entrada;
        entrada.open("in.txt");
        salida.open("out.txt");
	entrada >> n;
	char cadena[200];
        entrada.getline(cadena,200);
	for ( i = 1 ; i <= n; i++){
		entrada.getline(cadena, 200);
		salida << "Case #" << i << ": ";
                for (int j = 0 ; j < strlen(cadena); j++) {
                    int index = cadena[j] - 'a';
                    if ( index >= 0 && index < 26 ){
                        salida  << abc[index];
                    }else {
                        salida  << cadena[j];
                    }
                }
                salida << endl;
	}
	return 0;
}
