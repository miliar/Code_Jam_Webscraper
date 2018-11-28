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

int badadd(int a, int b){
	return a^b;
}

pair<int,int> samesum(vector<int> vals, pair<int,int> a, pair<int,int> b){
	if (vals.size() > 0){
		int bada = badadd(a.first, vals.back());
		int badb = badadd(b.first, vals.back());
		int truea = a.second + vals.back();
		int trueb = b.second + vals.back();
		vals.pop_back();
		pair<int,int> resulta = samesum(vector<int>(vals), make_pair(bada,truea), b);
		pair<int,int> resultb = samesum(vector<int>(vals), a, make_pair(badb,trueb));
		return resulta.second > resultb.second ? resulta : resultb;

	}
	else {
		if (a.second == 0 || b.second == 0){
			return make_pair(0,0);
		}
		else if (a.first == b.first){
			if (a.second > b.second){
				return a;
			}
			else {
				return b;
			}
		}
		else {
			return make_pair(0,0);
		}
	}
}

int main(){
	ifstream input("C-small-attempt1.in");
	ofstream output("result.txt");
	string line;
	getline(input, line);
	int numcases = strtoint(line);
	for(int i = 0; i < numcases; i++){
		getline(input, line);
		int numcandies = strtoint(line);
		getline(input, line);
		vector<string> tokens = tokenize(line);
		vector<int> vals;
		for (int j = 0; j < numcandies; j++){
			vals.push_back(strtoint(tokens[j]));
		}
		pair<int,int> result = samesum(vector<int>(vals), make_pair(0,0), make_pair(0,0));
		output << "Case #" << i+1 << ": ";
		if (result.second > 0){
			output << result.second << "\n";
		}
		else {
			output << "NO" << "\n";
		}
	}
	return 0;
}
