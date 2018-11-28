//============================================================================
// Name        : CJam1.cpp
// Author      : Daniel Gomez
// Version     :
// Copyright   :
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <String.h>

using namespace std;

char arr[16];
short verificar(char c);

int main(void) {

	 ifstream myReadFile;
	 ofstream myWriteFile;
	 int T, E;

	 myReadFile.open("A-large.in");
	 myWriteFile.open("A-large.out");

	 if (myReadFile.is_open()) {
		 myReadFile >> T;
		 for(int i=0; i<T; i++){

			 //printf("Case #%i \n", (i+1));
			 E=0;
			 for(int j=0; j< 16 ; j++) {
				 myReadFile >> arr[j];
				 if(arr[j]=='.') E++;
				 //printf("%c ", arr[j]);
				 //if((j+1)%4==0 && j!=0)printf("\n");
			 }
			 printf("\n");

			 if(verificar('X')) myWriteFile << "Case #"<< (i+1) <<": X won";
			 else if(verificar('O')) myWriteFile << "Case #"<< (i+1) <<": O won";
			 else if(E==0) myWriteFile << "Case #"<< (i+1) <<": Draw";
			 else myWriteFile << "Case #"<< (i+1) <<": Game has not completed";
			 if(i!=T-1) myWriteFile << "\n";
		 }
	}
	myReadFile.close();
	myWriteFile.close();


	system("pause");
	return EXIT_SUCCESS;
}


short verificar(char c){

	//Verificacion de que la ficha gano
	for(int i=0; i<4 ; i++){
		//Verificacion Vertical
		if((arr[i]==c||arr[i]=='T') && (arr[i+4]==c||arr[i+4]=='T') && (arr[i+8]==c||arr[i+8]=='T') && (arr[i+12]==c||arr[i+12]=='T'))return 1;
		//Verificacion Horizontal
		if((arr[4*i]==c||arr[4*i]=='T') && (arr[4*i+1]==c||arr[4*i+1]=='T') && (arr[4*i+2]==c||arr[4*i+2]=='T') && (arr[4*i+3]==c||arr[4*i+3]=='T'))return 1;
	}
	//Verificacion de diagonales
	if((arr[0]==c||arr[0]=='T') && (arr[5]==c||arr[5]=='T') && (arr[10]==c||arr[10]=='T') && (arr[15]==c||arr[15]=='T'))return 1;
	if((arr[3]==c||arr[3]=='T') && (arr[6]==c||arr[6]=='T') && (arr[9]==c||arr[9]=='T') && (arr[12]==c||arr[12]=='T'))return 1;

	//Si gana se devuelve 1, sino 0
	return 0;
}

