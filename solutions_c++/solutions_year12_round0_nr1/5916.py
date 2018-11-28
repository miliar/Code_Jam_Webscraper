#include <map>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

map<char, char> m;

void generateMappings(){
	m['a'] = 'y';
	m['b'] = 'h';
	m['c'] = 'e';
	m['d'] = 's';
	m['e'] = 'o';
	m['f'] = 'c';
	m['g'] = 'v';
	m['h'] = 'x';
	m['i'] = 'd';
	m['j'] = 'u';
	m['k'] = 'i';
	m['l'] = 'g';
	m['m'] = 'l';
	m['n'] = 'b';
	m['o'] = 'k';
	m['p'] = 'r';
	m['q'] = 'z';
	m['r'] = 't';
	m['s'] = 'n';
	m['t'] = 'w';
	m['u'] = 'j';
	m['v'] = 'p';
	m['w'] = 'f';
	m['x'] = 'm';
	m['y'] = 'a';
	m['z'] = 'q';
}

vector<string> split(string s){
	stringstream ss(s);
	string temp("");
	vector<string> v;
	while(ss >> temp){
		for(size_t i = 0; i < temp.size(); i++){
			temp[i] = m[temp[i]];
		}
		v.push_back(temp);
	}
	return v;
}

int main(){
	generateMappings();
	string input("");
	getline(cin, input);
	int x = atoi(input.c_str());
	for(int i = 0; i < x; i++){
		string sentence("");
		getline(cin, sentence);
		vector<string> result = split(sentence);
		cout<<"Case #"<<i + 1<<": ";
		for(size_t j = 0; j < result.size(); j++){
			cout<<result[j];
			if(j != result.size() - 1){
				cout<<" ";
			}
		}
		cout<<endl;
	}
	return 0;
}