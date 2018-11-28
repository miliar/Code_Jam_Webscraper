/*
 * Solver.cpp
 *
 *  Created on: Jul 17, 2008
 *      Author: peresz
 */

#include "Solver.h"

Solver::Solver() {
	// TODO Auto-generated constructor stub

}

Solver::~Solver() {
	// TODO Auto-generated destructor stub
}

const uint INF = 2000;

void Solver::solve(ifstream& inputfile, ofstream& outputfile){
	uint S;
	inputfile >> S;
	string temps;
	getline(inputfile, temps);
//	cout << "S: " << S << endl;

	vector<string> se(S);
	for(uint i = 0; i < S; ++i){
		getline(inputfile, se[i]);
		//cout << "read '" << se[i] << "'" << endl;
	}

	uint Q;
	inputfile >> Q;
	getline(inputfile, temps);
//	cout << "Q: " << Q << endl;

	if(Q == 0){
		outputfile << 0;
		return;
	}

	vector<string> query(Q);
	for(uint i = 0; i < Q; ++i){
		getline(inputfile, query[i]);
		//cout << "read '" << query[i] << "'" << endl;
	}

	vector< vector<uint> > T(S);

	uint i = 0;
	uint j = 0;
	for(; i < S; ++i){
		T[i].resize(Q);
		if(se[i] == query[0]) T[i][0] = INF;
		else T[i][0] = 0;
	}

	for(j = 1; j < Q; ++j)
		for(i = 0; i < S; ++i){
			if(se[i] == query[j]) T[i][j] = INF;
			else{
				T[i][j] = INF;
				for(uint k = 0; k < S; ++k){
					uint newVal = T[k][j-1];
					if(k != i) ++newVal;
					if(newVal < T[i][j]) T[i][j] = newVal;
				}
			}
			//cout << "T[" << i << "][" << j << "] = " << T[i][j] << endl;
		}

	uint result = INF;
	for(i = 0; i < S; ++i)
		if(T[i][Q-1] < result) result = T[i][Q-1];

	outputfile << result;
}
