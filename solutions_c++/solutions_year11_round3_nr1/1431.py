/*
 * File: Combinations.cpp
 * ----------------------
 * Name: [TODO: enter name here]
 * Section: [TODO: enter section leader here]
 * This file is the starter project for the combinations problem.
 * [TODO: rewrite the documentation]
 */

#include "genlib.h"
#include "simpio.h"
#include <iostream>
#include <fstream>
#include "scanner.h"
#include "strutils.h"
#include "vector.h"
#include "queue.h"
#include "grid.h"

const string Title = "A-large2.in";
const string Test = "test.txt";

bool editImage(Grid<char> & pic);
int main() {
	//string Title = GetLine();
	ifstream infile;
	ofstream offile;
	offile.open(Test.c_str());
	infile.open(Title.c_str());
	//if(!infile.fail()) cout <<"Error: File Could Not Be Read"<< endl;
	string num;
	getline(infile, num); 
	int Numb = StringToInteger(num);

	//cout << Numb << endl;
	for(int i = 0; i < Numb; i++){
		string temp;
		getline(infile, temp);
		int nextSpace = temp.find(' ');
		int row = StringToInteger(temp.substr(0, nextSpace));
		temp = temp.substr(nextSpace + 1);
		int col = StringToInteger(temp);
		Grid<char> pic(row, col);
		int counter = 0;
		
		for(int j = 0; j < row; j ++){
			getline(infile, temp);
			for(int k = 0; k < col; k++){
				pic[j][k] = temp[k];
				if(temp[k] == '#') counter++;
			}
		}
		offile << "Case #" << i + 1 << ":"  << endl;
		if((counter % 4) != 0){
			
			offile << "Impossible" << endl;
		} else {
		
			bool answer = editImage(pic);
		
			if(answer){
				for(int j = 0; j < pic.numRows(); j++){
					for(int k = 0; k < pic.numCols(); k++){
						offile << pic[j][k];
					}
					offile << endl;
				}
			} else {
				offile << "Impossible" << endl;
			}
		}
		
	}
	
	return 0;
}

bool editImage(Grid<char> & pic){
	for(int i = 0; i < pic.numRows(); i++){
		for(int j = 0; j < pic.numCols(); j++){
			if(pic[i][j] == '#'){
				if((j + 1) >= pic.numCols() || (i + 1) >= pic.numRows()) return false;
				if(pic[i][j+1] != '#' || pic[i+1][j+1] != '#' || pic[i+ 1][j] != '#') return false;
				pic.setAt(i, j, '/');
				pic.setAt(i, j + 1, '\\');
				pic.setAt(i + 1, j + 1, '/');
				pic.setAt(i + 1, j, '\\');
				return editImage(pic);

			}
		}

	}
	return true;
}