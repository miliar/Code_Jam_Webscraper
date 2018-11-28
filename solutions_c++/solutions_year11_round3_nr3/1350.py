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

const string Title = "C-small-attempt4.in";
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
		int players = StringToInteger(temp.substr(0, nextSpace));
		temp = temp.substr(nextSpace + 1);
		nextSpace = temp.find(' ');
		int low = StringToInteger(temp.substr(0, nextSpace));
		temp = temp.substr(nextSpace + 1);
		int high = StringToInteger(temp);
		Vector<int> harm;

		getline(infile, temp);
		cout << "Case" << i << "   " << temp << endl;
		cout << low << "   " << high << endl;
		for(int j = 0; j < players - 1; j ++){
			nextSpace = temp.find(' ');
			int note = StringToInteger(temp.substr(0, nextSpace));
			harm.add(note);
			temp = temp.substr(nextSpace + 1);
		}
		int lastnote = StringToInteger(temp);
		harm.add(lastnote);
		bool answer = false;
		int noteval;
		cout << players - harm.size() << endl;
		for( int k = 0; k < harm.size(); k++){
			cout << harm[k] << "  " ;

		}
		cout << endl;
		for(int j = low; j <= high; j++){
			int counter = 0;
			for(int k = 0; k < harm.size(); k++){
				if((harm[k] % j) == 0 || (j % harm[k]) == 0){
					counter++;
				}
			}
			if(counter == harm.size()){
				noteval = j;
				answer = true;
				break;
			}
		}
		if(answer){
			offile << "Case #" << i + 1 << ": "  << noteval << endl;
		} else {
			offile << "Case #" << i + 1 <<": NO"<< endl;
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