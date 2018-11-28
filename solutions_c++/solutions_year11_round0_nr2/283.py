#include <vector>
#include <list>
#include <map>
#include <string>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <cmath>

using namespace std;

string getline(){
	string tmp;
	getline(cin, tmp);
	return tmp;
}

static const char bases[] = "QWERASDF";

char getBaseId(char in){
	for(int i=0; i<sizeof(bases); i++)
		if(in == bases[i])
			return i;
	
	return -1;
}

char getBaseChar(char in){
	return bases[in];
}

void solveCase(){
	char combine[sizeof(bases)][sizeof(bases)];
	bool opposed[sizeof(bases)][sizeof(bases)];
	
	for(int i=0; i<sizeof(bases); i++){
		for(int j=0; j<sizeof(bases); j++){
			combine[i][j] = 0;
			opposed[i][j] = false;
		}
	}
	
	stringstream line(getline());
	int C, D, N;
	
	line >> C;
	string comb;
	for(int c=0; c<C; c++){
		line >> comb;
		comb[0] = getBaseId(comb[0]);
		comb[1] = getBaseId(comb[1]);
		if(comb[0]<0 || comb[1]<0){
			cerr << "not only bases can be combined";
			continue;
		}
		combine[comb[0]][comb[1]] = combine[comb[1]][comb[0]] = comb[2];
	}
	
	line >> D;
	string opps;
	for(int d=0; d<D; d++){
		line >> opps;
		opps[0] = getBaseId(opps[0]);
		opps[1] = getBaseId(opps[1]);
		if(opps[0]<0 || opps[1]<0){
			cerr << "not only bases can be opposed";
			continue;
		}
		opposed[opps[0]][opps[1]] = opposed[opps[1]][opps[0]] = true;
	}
	
	line >> N;
	vector<char> elements;
	string invoked;
	line >> invoked;
	for(int n=0; n<N; n++){
		char elem = getBaseId(invoked[n]);
		if(elem < 0){
			cerr << "not only bases can be invoked";
			continue;
		}
		
		if(!elements.size()){
			elements.push_back(elem);
			continue;
		}
		
		if(elements.back() < 10 && combine[elements.back()][elem]){
			elements.back() = combine[elements.back()][elem];
			continue;
		}
		
		for(int i=0; i<elements.size(); i++){
			if(elements[i] < 10 && opposed[elements[i]][elem]){
				elements.clear();
				break;
			}
		}
		
		if(elements.size())
			elements.push_back(elem);
	}
	
	cout << "[";
	for(int i=0; i<elements.size(); i++){
		if(i) cout << ", ";
		if(elements[i] < 10)
			cout << getBaseChar(elements[i]);
		else
			cout << elements[i];
	}
	cout << "]" << endl;
}

int main(int argc, char *argv[]){
	stringstream line(getline());
	unsigned int T;
	
	line >> T;
	
	for(unsigned int t=1; t<=T; t++){
		cout << "Case #" << t << ": ";
		solveCase();
	}
	
	return 0;
}

