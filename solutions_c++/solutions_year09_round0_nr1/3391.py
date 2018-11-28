/*
Google Code Jam 2009 Qualification Round: Alien Language
Stefan Videv
September 03, 2009
*/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int main(){
	//DECLARE
	int L, D, N; // variables
	int i,j,k; // counters
	bool flag; // bool switch if letter in word is found
	string tempWord; // input reading var
	vector<int> possibleMatches;
	
	//INPUT
	ifstream inputFile ("input.in");
	inputFile >> L;
	inputFile >> D;
	inputFile >> N;
	char databaseWords[D][L]; // stores language words
	int numberMatches[N]; // stores number of matches for patterns
	getline(inputFile, tempWord);
	for (i = 0; i< D; i++){
		getline(inputFile, tempWord);
		for (j =0; j < L; j++){
			databaseWords[i][j] = tempWord[j];
		}
	}
	
	//CALCULATE
	for (i = 0; i<N; i++){
		numberMatches[i] = 0;
		getline(inputFile, tempWord);
		char * pattern = new char[tempWord.size() + 1];
		copy(tempWord.begin(), tempWord.end(), pattern);
		pattern[tempWord.size()] = '\0';
		//find number of matches for each word
		if (tempWord.length() == L){
			// simple case
			flag = false;
			for (j = 0; j<D; j++){
				char dbWord[L];
				for (k = 0; k<L; k++){
					dbWord[k] = databaseWords[j][k];
				}
				if (strcmp(pattern,dbWord) == 0){
					flag = true;
				}	
				if (flag == true){
					numberMatches[i] = numberMatches[i] + 1;
				}
				flag = false;
			}
		}
		else {
			//complicated case
			numberMatches[i] = 0;
			bool parenthesis = false;
			int letter = 0;
			for (j = 0; j < tempWord.length(); j++){
				if (tempWord[j] == '('){
					//parenthesis open
					parenthesis = true;
				}
				else if(tempWord[j] == ')'){
					//parenthesis close
					parenthesis = false;
					letter++;
				} else {
					//regular character
					for (k = 0; k<D; k++){
						if (tempWord[j] == databaseWords[k][letter]){
							possibleMatches.push_back(k);
							//cout << tempWord[j] << " vs. " << databaseWords[k][letter] << endl;
							//cout << "possibleMatches contains:";
							//vector<int>::iterator it;
							//for (it=possibleMatches.begin(); it<possibleMatches.end(); it++)
								//cout << " " << *it;
							//cout << endl;
						}
					}
					if (parenthesis == false){
						letter++;
					}
				}
			}
			vector<int>::iterator it, itt;
			for (it = possibleMatches.begin(); it < possibleMatches.end(); it ++){
				int counter = 0;
				int currentMatch = *it;
				for (itt = possibleMatches.begin(); itt < possibleMatches.end(); itt ++){
					if (currentMatch == *itt){
						counter = counter + 1;
						//cout << currentMatch << " vs. " << *itt << endl;
					}
				}
				if (counter == L){
					numberMatches[i] = numberMatches[i] + 1;
				}
			}
			numberMatches[i] = numberMatches[i] / L;
				//cout << endl;
			possibleMatches.clear();
		}
	}
	inputFile.close();
	//print output to file
	ofstream outputFile ("output.out");
	for (i = 0; i<N;i++){
		outputFile << "Case #" << i+1 << ": " << numberMatches[i] << endl;
	}
	outputFile.close();
	return 0;
}

