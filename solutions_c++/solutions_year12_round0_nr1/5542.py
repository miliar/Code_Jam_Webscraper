#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

void problemA();

int main () {

	problemA();

	return 0;
}

void problemA(){
	string line;
	string alpha = "abcdefghijklmnopqrstuvwxyz";
	string key = "ynficwlbkuomxsevzpdrjgthaq";
	string *prob;
	string *answ;
	int rows = 0;

	ifstream problem ("problemA.txt");
	if (problem.is_open())
	{
		getline (problem,line);
		rows = atoi(line.c_str());
				
		prob = new string[rows];
		answ = new string[rows];
		
		int i = 0;
		while ( problem.good() )
		{
			getline (problem,line);
			prob[i] = line;
			i++;
		}
		problem.close();
	}
	else cout << "Unable to open problem file"; 	
	
	for(int i = 0; i < rows; i++){
		cout << "Case #" << (i + 1) << ": ";
		for(int j = 0; j < prob[i].size(); j++){
			if(prob[i][j] != ' '){
				cout << alpha[key.find(prob[i][j])];
			}
			else
				cout << " ";
		}
		cout << endl;	
	}
}