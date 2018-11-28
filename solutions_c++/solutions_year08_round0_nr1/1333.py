#include <iostream>
#include <string>

using namespace std;


void addS(string srch, string * SEngines, int * Pos,int s,int where){
	for (int i = 0; i < s; i++){
		if (srch.compare(SEngines[i]) == 0)
			Pos[i] = where;
	}
}

bool switchT(int * Pos,int s){
	bool switchTime = true;
	for (int i = 0; i < s; i++){
		if (Pos[i] == 0)
			switchTime = false;
	}
	return switchTime;
}

void reset(int * Pos,int s){	
	for (int i = 0; i < s; i++){
		Pos[i] = 0;
	}
}

int main () {
	
	int n;
	cin >> n;
	for (int i = 0; i < n; i++){
		int nse;
		cin >> nse;
		string tmp = "";
		getline(cin,tmp); 
		//Set up arrays
		string* searchE = new string[nse];
		int* posSearch = new int[nse];
		//cout << nse <<endl;
		//Read inputs
		for (int j = 0; j < nse; j++){
			getline(cin,searchE[j]);
			posSearch[j] = 0;
			//cout << searchE[j] << endl;
		}		
		int switches = 0;
		int ns;
		cin >> ns;
		getline(cin,tmp); 
		for (int j = 0; j < ns; j++){
			string search;
			getline(cin,search);
			addS(search,searchE,posSearch,nse,j+1);
			//Check if a switch is necessary
			if (switchT(posSearch,nse)){
				switches++;
				reset(posSearch,nse);
				addS(search,searchE,posSearch,nse,j+1); 
				//cout << j <<search << endl;
			}
		}
		delete [] posSearch;
		delete [] searchE;
		cout << "Case #" << i + 1 << ": " << switches << endl;
	}		
	return 0;
}
