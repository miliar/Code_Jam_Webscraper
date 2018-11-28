#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;
int TESTS;

vector<string> matrix;
vector<double> OOWP,OWP,WP;
vector<double> winnings, played;

double calcWP(int index){
	double wins = 0, tot = 0;
	for(int i = 0; i<matrix[index].size(); i++){
		if(matrix[index][i] == '.') continue;
		tot++;
		if(matrix[index][i] == '1') wins++;
	}
	winnings.push_back(wins);
	played.push_back(tot);
	return wins/tot;
}

double calcOWP(int index){
	double tot = 0, wpa = 0;
	for(int opponent = 0; opponent<matrix[index].size(); opponent++){
		if(matrix[index][opponent] == '.') continue;
		if(matrix[index][opponent] == '1') wpa += (winnings[opponent])/(played[opponent]-1);
		if(matrix[index][opponent] == '0') wpa += (winnings[opponent]-1)/(played[opponent]-1);
		tot++;
	}
	return wpa/tot;
}

double calcOOWP(int index){
	double owpa = 0, tot = 0;
	for(int i = 0; i<matrix[index].size(); i++){
		if(matrix[index][i] == '.') continue;
		tot++;
		owpa += OWP[i];
	}
	return owpa/tot;
}

int main(){
	ifstream in("Input.in");
	ofstream out("Output.out");
	in >> TESTS;
	string c;
	for(int test = 1; test<=TESTS; test++){
		winnings.clear(); played.clear();
		OOWP.clear(); OWP.clear(); matrix.clear();
		WP.clear();
		vector<double> ret;
		int N;
		in >> N;
		for(int i = 0; i<N; i++){
			in >> c;
			matrix.push_back(c);
		}

		for(int i = 0; i<N; i++)
			WP.push_back(calcWP(i));
		for(int i = 0; i<N; i++)
			OWP.push_back(calcOWP(i));
		for(int i = 0; i<N; i++) 
			OOWP.push_back(calcOOWP(i));

		for(int i = 0; i<N; i++){
			ret.push_back(0.25*WP[i] + 0.50*OWP[i] + 0.25*OOWP[i]);
		}

		out << "Case #" << test << ":" << endl;
		for(int u = 0; u<ret.size(); u++)
			out << ret[u] << endl;
	}
} 

