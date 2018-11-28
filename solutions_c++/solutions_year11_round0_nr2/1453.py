#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <map>
#include <set>
#include <vector>

using namespace std;

void solve(string &invoke, map < pair <char, char>, char > &combinations, map < char, vector< char> > &opposed, string &solution){
	set<char> currentOpposed;
	set<char> pendingOpposed;
	solution = "";
	for (int i = 0; i < invoke.size(); i++){
		if (solution.size() > 0){
			if (combinations.count(pair<char,char>(solution[solution.size()-1], invoke[i])) == 1){//Combina con el ultimo
				solution[solution.size()-1] = combinations[pair<char,char>(solution[solution.size()-1], invoke[i])];
				pendingOpposed.clear();
				continue;
			}
		}
		//No combina con el ultimo
		if ((currentOpposed.count(invoke[i]) == 1) || (pendingOpposed.count(invoke[i]) == 1)){
			solution = "";
			currentOpposed.clear();
			pendingOpposed.clear();
		} else {
			//current = current U pending
			for (set<char>::iterator it1 = pendingOpposed.begin(); it1 != pendingOpposed.end(); it1++){
				currentOpposed.insert(*it1);
			}
			pendingOpposed.clear();
			for (int j = 0; j < opposed[invoke[i]].size(); j++){
				pendingOpposed.insert(opposed[invoke[i]][j]);
			}
			solution += invoke[i];
		}
	}
}

int main(int argc, char *argv[]){
	if (argc != 2){
		cerr << "Error: " << argv[0] << " file" << endl;
		exit(-1);
	}
	ifstream file(argv[1]);
	if (!file.is_open()){
		cerr << "Error: file " << argv[0] << " could not be opened" << endl;
	}
	int N;
	file >> N;
	for (int i = 0; i < N; i++){
		int C;
		file >> C;
		map < pair <char, char>, char > combinations;
		for (int j = 0; j < C; j++){//Combinaciones
			char base1, base2, combined;
			file >> base1 >> base2 >> combined;
			combinations[pair<char, char>(base1, base2)] = combined;
			combinations[pair<char, char>(base2, base1)] = combined;
		}
		int D;
		file >> D;
		map <char, vector<char > > opposed;
		for (int j = 0; j < D; j++){//Opuestos
			char op1, op2;
			file >> op1 >> op2;
			opposed[op1].push_back(op2);
			opposed[op2].push_back(op1);
		}
		int N;
		file >> N;
		string invoke;
		file >> invoke;
		string solution;
		solve(invoke, combinations, opposed, solution);
		cout << "Case #" << (i+1) << ": [";
		for (int j = 0; j < (int)solution.size() - 1; j++){
			cout << solution[j] << ", ";
		}
		if (solution.size() > 0){
			cout << solution[solution.size() - 1];
		}
		cout << "] " << endl;
	}
}

