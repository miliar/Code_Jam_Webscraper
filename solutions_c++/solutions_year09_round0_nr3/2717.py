#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>


using namespace std;

int INT_CodeJam(int, string);

int main()
{
	cout << "CodeJam: " << "\n";
	//char CHR_Entrada[] = "elcomew elcome to code jam"; //longitud 27
	//char CHR_Entrada[] = "wweellccoommee to code qps jam"; //longitud 30
	//string STR_Entrada = "wweellccoommee to code qps jam";
	string STR_Entrada = "elcomew elcome to code jam";
	//string STR_Entrada = "welcome to codejam";
	cout << "Cantidad de veces: " << INT_CodeJam(STR_Entrada.length(), STR_Entrada) << "\n";

	ifstream IFS_Entrada;
	IFS_Entrada.open("C-small-attempt0.in");
	//ofstream OFS_Salida("salida",ios_base::trunc);
	FILE *FILE_Salida = fopen( "salida", "w" );
	int INT_Contador = 1;
	string STR_Auxiliar;
	//getline(IFS_Entrada,STR_Auxiliar);
	int INT_Cantidad;
	IFS_Entrada >> INT_Cantidad;
	cout << INT_Cantidad << "\n";
	IFS_Entrada.close();
	IFS_Entrada.open("C-small-attempt0.in");
	getline(IFS_Entrada,STR_Auxiliar);
	while(INT_Contador <= INT_Cantidad){
		getline(IFS_Entrada,STR_Auxiliar);
		//cout << STR_Auxiliar << "\n";
		//OFS_Salida << "Case #" << INT_Contador << ": " << INT_CodeJam(STR_Auxiliar.length(), STR_Auxiliar) << "\n";
		fprintf(FILE_Salida, "Case #%d: %.4d\n", INT_Contador, INT_CodeJam(STR_Auxiliar.length(), STR_Auxiliar));
		printf("Case #%d: %.4d\n", INT_Contador, INT_CodeJam(STR_Auxiliar.length(), STR_Auxiliar));
		//cout << "Case #" << INT_Contador << ": " << INT_CodeJam(STR_Auxiliar.length(), STR_Auxiliar) << "\n";
		INT_Contador++;
	}
	IFS_Entrada.close();
	//OFS_Salida.close();
	fflush(FILE_Salida);
	fclose(FILE_Salida);

    return 0;
}

int INT_CodeJam(int INT_Longitud,string STR_Entrada){
	bool FLAG = true;
	bool FLAG_W = false;
	int INT_Respuesta = 0;
	char CHR_Solucion[] = "welcome to code jam";
	int INT_Indice_Palabra = 0;
	int INT_Indice_Total = 0;
	int INT_Posiciones[19];
	while(FLAG){
		if (STR_Entrada[INT_Indice_Total] == CHR_Solucion[INT_Indice_Palabra]){
			FLAG_W = true;
			INT_Posiciones[INT_Indice_Palabra] = INT_Indice_Total;
			if(INT_Indice_Palabra == 19){
				INT_Respuesta++;
				INT_Respuesta = INT_Respuesta % 1000; //Asi puedo usar siempre INT
			}else{
				INT_Indice_Palabra++;
			}
		}
		INT_Indice_Total++;
		if(INT_Indice_Total >= INT_Longitud + 1){//Llegue al final de la frase
			//if(INT_Indice_Palabra > 0)
			if(FLAG_W){
				if(INT_Indice_Palabra == 0 /*&& INT_Indice_Total >= INT_Longitud*/){
					FLAG = false;
				}
				INT_Indice_Palabra--;
				INT_Indice_Total = INT_Posiciones[INT_Indice_Palabra] + 1;
			}
			else{
				FLAG = false;
			}
		}
	}
	return INT_Respuesta;
}







