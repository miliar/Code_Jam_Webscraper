//============================================================================
// Name        : test.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
#include <boost/algorithm/string.hpp>


#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>

#include <stdlib.h>

#include "Number.h"


class ProblemA {
public:
	ProblemA(){

	}

	bool horizontalCheck(char tc[4][4], char cSeek){

		for(int i = 0; i <4; i++){
			int wins = 0;
			for(int j = 0 ; j< 4 ; j++ ){
				if((tc[i][j] ==  cSeek)|| (tc[i][j] == 'T')){
					wins++;
					if(wins == 4){
						return true;
					}
				}else{
					wins=0;
				}
			}
		}
		return false;
	}

	bool verticalCheck(char tc[4][4], char cSeek){

			for(int i = 0; i <4; i++){
				int wins = 0;
				for(int j = 0 ; j< 4 ; j++ ){
					if((tc[j][i] ==  cSeek)|| (tc[j][i] == 'T')){
						wins++;
						if(wins == 4){
							return true;
						}
					}else{
						wins=0;
					}
				}
		}
		return false;
	}

	bool diagCheck(char tc[4][4], char cSeek){
		int wins = 0;
		for(int i = 0; i <4; i++){

			if((tc[i][i] ==  cSeek)|| (tc[i][i] == 'T')){
				wins++;
				if(wins == 4){
					return true;
				}
			}else{
				wins=0;
			}
		}
		wins = 0;
		for(int i = 0; i <4; i++){

			if((tc[i][3-i] ==  cSeek)|| (tc[i][3-i] == 'T')){
				wins++;
				if(wins == 4){
					return true;
				}
			}else{
				wins=0;
			}
		}
		return false;
	}

	bool checkDot(char tc[4][4]){
		for(int i = 0; i <4; i++){
			for(int j = 0 ; j< 4 ; j++ ){
				if(tc[i][j] == '.'){
					return true;
				}
			}
		}
		return false;

	}

	std::string analyseTC(char tc[4][4]){

		char car = 'X';
		//on commence par tester les horizontals
		if(horizontalCheck(tc, car) || verticalCheck(tc, car) || diagCheck(tc, car)){
			return "X won";
		}

		if(horizontalCheck(tc, 'O')
		|| verticalCheck(tc, 'O')
		|| diagCheck(tc, 'O')){
			return "O won";
		}

		if(checkDot(tc)){
			return "Game has not completed";
		}else{
			return "Draw";
		}
	}
};


typedef std::deque<std::pair<int,bool> > deque_res;

int main(int argc, char* argv[]) {

	if(argc == 3){

		//fichier d'entr��e
		std::fstream inputFile;
		inputFile.open(argv[1]);

		//lecture nombre de test case
		std::string sNb;
		std::getline(inputFile, sNb);
		int nb = Number::getInt(sNb);

		//fichier de sortie
		std::fstream outputFile;
		outputFile.open(argv[2],std::fstream::out);

		ProblemA pa;

		//pour chaque test case ou si l'on a atteint la fin du fichier
		for(int i = 0 ; (i < nb)&&(inputFile.eof() == false) ; i++){

			//std::vector<std::string> svLine;
			char tc[4][4] = {{0,0,0,0},{0,0,0,0},{0,0,0,0},{0,0,0,0}};
			//lecture de chaque ligne
			for(int j=0;j<4;j++){
				std::string sLine;

				std::getline(inputFile, sLine);

				if(sLine.empty()){
					std::cout << "errr empty line in test case" << std::endl;
				}
				int k = 0;
				for(std::string::iterator it = sLine.begin(); it != sLine.end();it++){
					tc[j][k] = *it;
					k++;
				}


			}
			outputFile << "Case #" << (i+1) << ": "<< pa.analyseTC(tc) << std::endl;

			std::string sLine;
			std::getline(inputFile, sLine);

		}
		outputFile.close();
		std::cout << "ok" << std::endl;
	}else{
		std::cout << "invalid number of parameter " << std::endl;
	}
	return 0;
}
