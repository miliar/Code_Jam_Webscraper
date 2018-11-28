
#include "genlib.h"
#include "simpio.h"
#include <iostream>
#include <fstream>
#include "lexicon.h"
#include "scanner.h"
#include "strutils.h"
#include "vector.h"
#include "queue.h"
#include "map.h"

int addToSean(Vector<int> remainingNumbers, Vector<int> sean, Vector<int> pat);

const string Title = "C-small-attempt0.in";
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
		int piecesOfCandies;
		piecesOfCandies = StringToInteger(temp);
		Vector<int> numbers;
		getline(infile, temp);
		for(int j = 0; j < piecesOfCandies - 1; j++){
			int value;
			int nextSpace = temp.find(' ');
			value = StringToInteger(temp.substr(0, nextSpace));
			numbers.add(value);
			temp = temp.substr(nextSpace + 1);
		}
		int lastValue = StringToInteger(temp);
		numbers.add(lastValue);
		Vector<int> sean;
		Vector<int> pat;
		int max = addToSean(numbers, sean, pat);
		if(max < 0){
			offile << "Case #" << i + 1 << ": NO" << endl;
		} else {
			offile <<"Case #" << i + 1 << ": " << max << endl;
		}
	}	
	return 0;
}

int addToSean(Vector<int> remainingNumbers, Vector<int> sean, Vector<int> pat){
	if(remainingNumbers.isEmpty()){
		int seanTotal = 0;
		int patTotal = 0;
		
		for(int i = 0; i < sean.size(); i++){
			int current = sean[i];
			
			seanTotal = seanTotal ^ current;
		
		}
		
		for(int i = 0; i < pat.size(); i++){
			int current = pat[i];
			patTotal = patTotal ^ current;
		}
		if(patTotal == seanTotal && pat.size() != 0 && sean.size() != 0){
			int realNumber = 0;
			for(int i = 0; i <sean.size(); i++){
				realNumber += sean[i];
			}
			return realNumber;
		}
		return -1;
	}
	int nextNumber = remainingNumbers[0];
	remainingNumbers.removeAt(0);
	Vector<int> newsean;
	Vector<int> newpat;
	newsean = sean;
	newpat = pat;
	newsean.add(nextNumber);
	newpat.add(nextNumber);
	int maxSeanA = addToSean(remainingNumbers, newsean, pat);
	int maxPatA = addToSean(remainingNumbers, sean, newpat);
	if(maxSeanA > maxPatA)
		return maxSeanA;
	return maxPatA;
}

