#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "stdio.h"
#include <math.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <sstream>
#include <fstream>
#include <list>

int winXO(std::string table[4],char xo) {
std::string table_aux[4];

	for (int i=0;i<4;i++)
		table_aux[i] = table[i];

	for (int i=0;i<4;i++)
		replace(table_aux[i].begin(), table_aux[i].end(), 'T', xo);
	
	for (int i=0;i<4;i++)
		if ((table_aux[i].at(0)==xo) && 
			(table_aux[i].at(1)==xo) &&
			(table_aux[i].at(2)==xo) &&
			(table_aux[i].at(3)==xo))
			return 1;

	for (int i=0;i<4;i++)
		if ((table_aux[0].at(i)==xo) && 
			(table_aux[1].at(i)==xo) &&
			(table_aux[2].at(i)==xo) &&
			(table_aux[3].at(i)==xo))
			return 1;

	if ((table_aux[0].at(0) == xo) &&
		(table_aux[1].at(1) == xo) &&
		(table_aux[2].at(2) == xo) &&
		(table_aux[3].at(3) == xo) )
			return 1;

	if ((table_aux[0].at(3) == xo) &&
		(table_aux[1].at(2) == xo) &&
		(table_aux[2].at(1) == xo) &&
		(table_aux[3].at(0) == xo) )
			return 1;
	return 0;//WinX
}

int Gamming(std::string table[4]) {
std::string table_aux[4];

	for (int i=0;i<4;i++)
		table_aux[i] = table[i];

	for (int i=0;i<4;i++) {
		int found=table_aux[i].find('.');
  		if (found!=std::string::npos)
  			return 1;
  	}
		

	return 0;
}


int main(void) {
	std::ifstream inputFile;
	int test_cases =0;
	std::string line;
	std::string table[4];
	std::string result ="";

	inputFile.open("input.txt");
    inputFile >> test_cases ;
    std::getline(inputFile,line);

    for(int cases_executed=1;cases_executed<=test_cases;cases_executed++){
    	for(int aux=0;aux<4;aux++)
			std::getline(inputFile,table[aux]);

		if(winXO(table,'X'))
			result = "X won";
		else if(winXO(table,'O'))
			result = "O won";
		else if(Gamming(table))
			result = "Game has not completed";
		else 
			result = "Draw";

		std::getline(inputFile,line); //blank line
		std::cout << "Case #" << cases_executed << ": " << result  << std::endl;
	}

    inputFile.close();
    return 1;
}
