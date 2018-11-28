#include <fstream>

#include <map>

#include <string>
#include <algorithm>

#include <vector>

#include <iostream>

using namespace std;

typedef map<string, int> dir;
typedef dir::iterator iter;

vector<dir> dirs;

dir root;

int addDirs(string line) {
	vector<string> tokens;
	
	string word = "";
	
	for (int i = 0; i < line.length(); i++) {
		if (line[i] != '/')
			word += line[i];
		else {
			tokens.push_back(word);
			word = "";
		}
	}
	tokens.push_back(word);
	
	
	int pos = 0;
	int actions = 0;
	
	for (int i = 1; i < tokens.size(); i++) {
		iter it = dirs[pos].find(tokens[i]);
		
		if (it == dirs[pos].end()) {
			actions++;			
			dirs[pos][tokens[i]] = dirs.size();
			pos = dirs.size();
			
			dir tmp;
			
			dirs.push_back(tmp);
			continue;
		}
		
		pos = (*it).second;
		
	}
	return actions;
}



int main() {
	fstream fin("A.in");
	ofstream out("A.out");
	int t;
	fin >> t;

	for (int i = 0; i < t; i++) {
		
		dirs.clear();
		dirs.push_back(root);
		int n, m;
		fin >> n >> m;
		
		for (int j = 0; j < n; j++) {
			string line;
			fin >> line;
			addDirs(line);
		}
		
		int actions = 0;
		
		for (int j = 0; j < m; j++) {
			string line;
			fin >> line;
			actions += addDirs(line);
		}
		
		out << "Case #" << i + 1 << ": " << actions << endl;
	}
	fin.close();
	out.close();
	
	return 0;
}