#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <iterator>
#include <map>
#include <string>

using namespace std;

int strtoint(string str){
	stringstream strstr(str);
	int result;
	return strstr >> result ? result : 0;
}

vector<string> tokenize(string str){
	stringstream strstr(str);
	istream_iterator<string> it(strstr);
	istream_iterator<string> end;
	vector<string> results(it, end);
	return results;
}

void resolve(vector<string>* elements, string newguy, map<string,string>* combomap, map<string,string>* oppmap){
	if(elements->size() > 0){
		stringstream strstr;
		stringstream strstr2;
		strstr << newguy << elements->back();
		strstr2 << elements->back() << newguy;
		string comboresult = ((*combomap)[strstr.str()]).compare("") != 0 ? (*combomap)[strstr.str()] : (*combomap)[strstr2.str()];
		if (comboresult.compare("") != 0){
			elements->pop_back();
			resolve(elements, comboresult, combomap, oppmap);
		}
		else {
			vector<string>::iterator itr = elements->begin();
			while(itr != elements->end()){
				if((*oppmap)[*itr] == newguy || (*oppmap)[newguy] == *itr){
					elements->clear();
					return;
				}
				itr++;
			}
			elements->push_back(newguy);
		}
	}
	else{
		elements->push_back(newguy);
	}
}

int main(){
	ifstream input("B-small-attempt0.in");
	ofstream output("result.txt");
	string line;
	getline(input, line);
	int numcases = strtoint(line);
	for(int i = 0; i < numcases; i++){
		getline(input, line);
		vector<string> tokens = tokenize(line);
		vector<string>::iterator itr = tokens.begin();
		int numcombos;
		int numopps;
		int numelements;
		numcombos = strtoint(*itr);
		itr++;
		map<string,string> combomap;
		for(int j = 0; j < numcombos; j++){
			string::iterator sitr = (*itr).begin();
			stringstream strstr;
			strstr << *sitr;
			sitr++;
			strstr << *sitr;
			sitr++;
			combomap[strstr.str()] = *sitr;
			itr++;
		}
		numopps = strtoint(*itr);
		itr++;
		map<string,string> oppmap;
		for(int j = 0; j < numopps; j++){
			string::iterator sitr = (*itr).begin();
			stringstream strstr;
			strstr << *sitr;
			sitr++;
			oppmap[strstr.str()] = *sitr;
			itr++;
		}
		numelements = strtoint(*itr);
		itr++;
		vector<string> result;
		string::iterator sitr = (*itr).begin();
		while (sitr != (*itr).end()){
			stringstream strstr;
			strstr << *sitr;
			resolve(&result, strstr.str(), &combomap, &oppmap);
			sitr++;
		}
		output << "Case #" << i+1 << ": [";
		itr = result.begin();
		if (itr == result.end()){
			output << "]\n";
		}
		while (itr != result.end()){
			if (itr+1 == result.end()){
				output << (*itr) << "]\n";
			}
			else {
				output << (*itr) << ", ";
			}
			itr++;
		}
	}
	return 0;
}
