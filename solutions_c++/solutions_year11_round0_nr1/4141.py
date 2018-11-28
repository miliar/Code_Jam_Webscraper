#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <iterator>

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

int main(){
	ifstream input("A-large.in");
	ofstream output("result.txt");
	string line;
	getline(input, line);
	int numcases = strtoint(line);
	for(int i = 0; i < numcases; i++){
		getline(input, line);
		vector<string> tokens = tokenize(line);
		int numbuttons = strtoint(tokens[0]);
		int totalmoves = 0;
		int ospot = 1;
		int bspot = 1;
		int omoves = 0;
		int bmoves = 0;
		int opresses = 0;
		int bpresses = 0;
		string prevbot = tokens[1];
		for(int j = 1; j < numbuttons*2; j+=2){
			if(tokens[j] == "O"){
				if(prevbot == "B"){
					omoves += (1 + max(abs(strtoint(tokens[j+1]) - ospot), max(bmoves - omoves, 0)));
				}
				else {
					omoves += (1 + abs(strtoint(tokens[j+1]) - ospot));
				}
				ospot = strtoint(tokens[j+1]);
			}
			else {
				if(prevbot == "O"){
					bmoves += (1 + max(abs(strtoint(tokens[j+1]) - bspot), max(omoves - bmoves, 0)));
				}
				else {
					bmoves += (1 + abs(strtoint(tokens[j+1]) - bspot));
				}
				bspot = strtoint(tokens[j+1]);
			}
			prevbot = tokens[j];
		}
		output << "Case #" << i+1 << ": " << max(omoves, bmoves) << "\n";
	}
	return 0;
}
