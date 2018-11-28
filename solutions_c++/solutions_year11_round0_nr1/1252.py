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

const string Title = "A-large.in";
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
	//cout << "This far" << endl;
	Vector<string> Commands;
	for(int i = 0; i < Numb; i++){
		string temp;
		getline(infile, temp);
		Vector<int> orange;
		Vector<int> blue;
		Vector<char> order;
		int numOfButtons;
		int nextSpace = temp.find(' ');
		numOfButtons = StringToInteger(temp.substr(0, nextSpace));
		temp = temp.substr(nextSpace + 1);
		cout << numOfButtons << endl;
		for(int j = 0; j < numOfButtons - 1; j++){
			if(temp[0] == 'O'){
				order.add('O');
				temp = temp.substr(2);
				nextSpace = temp.find(' ');
				cout << nextSpace << endl;
				orange.add(StringToInteger(temp.substr(0, nextSpace)));
				temp = temp.substr(nextSpace + 1);
			} else {
				order.add('B');
				temp = temp.substr(2);
				nextSpace = temp.find(' ');
				blue.add(StringToInteger(temp.substr(0, nextSpace)));
				temp = temp.substr(nextSpace + 1);
			}
		}
		if(temp[0] == 'O'){
			order.add('O');
			orange.add(StringToInteger(temp.substr(2)));
		} else {
			order.add('B');
			nextSpace = temp.find(' ');
			blue.add(StringToInteger(temp.substr(2)));
		}
		orange.add(0);
		blue.add(0);
		cout << "Orange" << endl;
		for(int i = 0; i < orange.size(); i++){
			cout << orange[i] << endl;
		}
		cout << "Blue" << endl;
		for(int i = 0; i < blue.size(); i++){
			cout << blue[i] << endl;
		}
		cout << "Order" << endl;
		for(int i = 0; i < order.size(); i++){
			cout << order[i] << endl;
		}
		int counter = 0;
		int oRobot = 1;
		int bRobot = 1;
		bool bFound = false;
		bool oFound = false;
		while(!order.isEmpty()){
			if(orange[0] != 0){
				int orangeTarget = orange[0];
				if(orangeTarget > oRobot){
					oRobot = oRobot + 1;
				} else if(orangeTarget < oRobot){
					oRobot = oRobot - 1;
				} else {
					oFound = true;
				}
			}
			if(blue[0] != 0){
				int blueTarget = blue[0];
				if(blueTarget > bRobot){
					bRobot = bRobot + 1;
				} else if(blueTarget < bRobot){
					bRobot = bRobot - 1;
				} else {
					bFound = true;
				}
			}
			if(order[0] == 'O'){
				if(oFound){
					orange.removeAt(0);
					order.removeAt(0);
					oFound = false;
				}
			} else {
				if(bFound){
					blue.removeAt(0);
					order.removeAt(0);
					bFound = false;
				}
			}
			counter++;
		}
		offile <<"Case #" << i + 1 << ": " << counter << endl;
	}
	
			

	return 0;
}
