/* A.cpp
 * 
 * By: Michael Robertson
 * mikejrobertson AT gmail DOT com
 * Updated: 3 September 2009
 */

#include <iostream>
#include <fstream>
#define INFILE "A-large.in"
#define OUTFILE "data.out"

using namespace std;

void matches (string in,int letter, string words[],int match[][15]);

int l, w, n;
int main() {
 
	ifstream file;
	
	//Read file and get infomation
	file.open(INFILE);
	if (file.is_open()) {
		file >> l;
		file >> w; 
		file >> n; 
	} else {
		cerr << "Error opening file" << endl;
	}
	string words[w]; //stores each word
	int match[w][15]; //stores matches of letters
	int results[n];  //stores final results
	
	for (int i = 0; i < w; i++) {  //gets and stores words
		file >> words[i];
	//	cout << i << ": " <<words[i] <<endl;
	}
	
	for (int caseNum = 0; caseNum < n; caseNum++) {
		
		for (int i = 0; i < w; i++) {  // zero match array
			for (int j = 0; j < l; j++) { 
				match[i][j]=0;
			}
		}
		
		int count = 0;
		int letters;
		string in;
		file >> in;
		for (int i = 0; i < l; i++) { //scan input word
			if (in.substr(count,1) == "(") { //cheeck for brackets
				letters = 0;
				count++;
				while (in.substr(count,1) != ")") { //find contentes of brakets
					letters++;
					count++;
				}
				matches(in.substr(count-letters,letters),i, words, match);
				count++;
			} else {
				matches(in.substr(count,1),i, words, match);
				count++;
			}
		}
		results[caseNum] = 0;
		for (int i = 0; i < w; i++) {
			int num = 0;
			for (int j = 0; j < l; j++) { 
				num += match[i][j];
			}
			if (num == l){
				results[caseNum]++;
			}
		}
	}
	file.close();
	
	ofstream fileout;
	fileout.open(OUTFILE);
	if (fileout.is_open()) {
		for (int i=0; i < n; i++) {
			cout << "Case #" << i+1 << ": " << results[i] << endl;
			fileout << "Case #" << i+1 << ": " << results[i] << endl;
		}
	} else
	cerr << "Error can't open file to write" << endl;
	return 0;
}

void matches (string in,int letter, string words[], int match[][15]) {
//	cout << in << endl;
	for (unsigned int i = 0; i < in.length(); i++) {
		for (int j = 0; j < w; j++) {
			if (in.substr(i,1) == words[j].substr(letter,1)) {
				match[j][letter] = 1;
			}
		}
	}
}
