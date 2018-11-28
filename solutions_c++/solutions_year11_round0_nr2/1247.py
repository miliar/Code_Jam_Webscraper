
#include "genlib.h"
#include "simpio.h"
#include <iostream>
#include <fstream>
#include "lexicon.h"
#include "scanner.h"
#include "strutils.h"
#include "map.h"
#include "foreach.h"
const string Title = "B-large.in";
const string Test = "test2.txt";

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
	for(int i = 0; i < Numb; i++){
		string temp;
		getline(infile, temp);
		Map<char> combine;
		Lexicon opposed;
		int numOfCombine;
		int nextSpace = temp.find(' ');
		numOfCombine = StringToInteger(temp.substr(0, nextSpace));
		temp = temp.substr(nextSpace + 1);
	
		for(int j = 0; j < numOfCombine; j++){
			string triple = temp.substr(0, 3);
		
			combine.put(triple.substr(0,2), triple.at(2));
			string switching = "";
			switching  = switching + triple[1] + triple[0];
			
			combine.put(switching, triple[2]);
			temp = temp.substr(4);
		}
		
		nextSpace = temp.find(' ');	
		numOfCombine = StringToInteger(temp.substr(0, nextSpace));
		temp = temp.substr(nextSpace + 1);
	
		for(int j = 0; j < numOfCombine; j++){
			string doubled = temp.substr(0, 2);
			opposed.add(doubled);
			string switching = "";
			switching  = switching + doubled[1] + doubled[0];
			opposed.add(switching);
			temp = temp.substr(3);
		}
	
		nextSpace = temp.find(' ');
		numOfCombine = StringToInteger(temp.substr(0, nextSpace));
		temp = temp.substr(nextSpace + 1);
		foreach(string key in opposed){
			cout << "Number" << i << "Opposed: " << key<< endl;
		}
		foreach(string key in combine){
			cout << "Number" << i << "Opposed: " << key<< endl;
		}
		string develop = "";
		develop = develop + temp[0];
		for(int j = 1; j < temp.length(); j++){
			develop = develop + temp[j];
			cout << "Number" << i << "A: " << develop << endl;
			if(develop.length() > 1){
				string pair = "";
				pair = pair + develop[develop.length() - 2] + develop[develop.length() - 1];
				cout << pair << endl;
				if(combine.containsKey(pair)){
					char letter = combine.get(pair);
					develop = develop.substr(0, develop.length() - 2);
					develop = develop + letter;
				}
			}
			cout << "Number" << i << "B: " << develop << endl;
			bool deletion = false;
			if(develop.length() > 1){
				for(int k = 0; k < develop.length() - 1; k++){
					for(int l = k + 1; l < develop.length(); l++){
						string isItABomb = "";
						isItABomb = isItABomb + develop[k] + develop[l];
						if(opposed.containsWord(isItABomb))
							deletion = true;
						
					}
				}
			}
			
			if(deletion)
				develop = "";
			cout << "Number" << i << "C: " << develop << endl;
		}
		cout << develop.length() << " A" << develop << "A " <<endl;
		
		offile <<"Case #" << i + 1 << ": [";
		if(develop.length() == 0){
			offile << "]" << endl;
		}else{
			for(int z = 0; z < develop.length() - 1; z++){
				offile << develop[z] << ", ";
			}
		
			if(develop.length() > 0){
				offile << develop[develop.length() - 1] << "]" << endl;
			} else {
				offile << "]" << endl;
			}
		}
	}
	return 0;
}
