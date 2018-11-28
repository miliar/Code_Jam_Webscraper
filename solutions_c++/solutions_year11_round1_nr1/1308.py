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

const string Title = "A-small-attempt2.in";
const string Test = "test.txt";

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

	
	for(int i = 0; i < Numb; i++){
		int max, daycent, evercent;
		string temp;
		getline(infile, temp);
		int nextSpace = temp.find(' ');
		max = StringToInteger(temp.substr(0, nextSpace));
		temp = temp.substr(nextSpace + 1);
		nextSpace = temp.find(' ');
		daycent = StringToInteger(temp.substr(0, nextSpace));
		temp = temp.substr(nextSpace + 1);
		nextSpace = temp.find(' ');
		evercent = StringToInteger(temp.substr(0, nextSpace));
		temp = temp.substr(nextSpace + 1);
		bool flag = false;
		for(int j = 1; j <= max; j++){
			if((j * daycent) % 100 == 0){
				if((evercent < 100 && evercent > 0) || (evercent == daycent))
					flag = true;
			}
			if(flag) break;
		}
		if(flag){
			offile <<"Case #" << i + 1 << ": Possible" << endl;
		} else {
			offile <<"Case #" << i + 1 << ": Broken" << endl;
		}
	}
	
			

	return 0;
}

