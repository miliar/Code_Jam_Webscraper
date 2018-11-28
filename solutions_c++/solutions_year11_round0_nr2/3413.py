#include <fstream>
#include <iostream>
#include <string>
#include <map>
#include <vector>

using namespace std;

int main() {

	fstream fin, fout;
	int t;
	int n;
	int i, j;
	string str, str2("aa ");
	char  c, aux;
	bool ok;
	map<string, char> combinations;
	map<char, vector<char> > opposits;
	vector<char> list;
	vector<char> incompatible;
	map<string, char>::iterator itr;
	
	fin.open("B-large-0.in", fstream::in);
	fout.open("B-large-0.out", fstream::out);
	
	fin >> t;
	
	for (i = 0; i < t; ++i) {
		list.clear();
		incompatible.clear();
		combinations.clear();
		opposits.clear();
		fin >> n;
		for (j = 0; j < n; ++j) {
			fin >> str;
			c =str[2];
			str[2] = '\0';
			combinations.insert (pair<string, char>(str, c));
			aux = str[0];
			str[0] = str[1];
			str[1] = aux;
			combinations.insert (pair<string, char> (str, c));
		}
		
		fin >> n;
		for (j = 0; j < n; ++j) {
			fin >> str;
			opposits[str[0]].push_back(str[1]);
			opposits[str[1]].push_back(str[0]);
		}
		
		fin >> n;
		fin >> str;
		for (j = 0; j < n; ++j) {
			str2[0] = str2[1];
			str2[1] = str[j];
			if (!list.empty()) {
				for (itr = combinations.begin(); 
							itr != combinations.end(); ++itr) {
						if (itr->first.compare(0, 2, str2, 0, 2) == 0) {
							break;
						}
					}
				if (itr != combinations.end()) {
					list.back() = itr->second;
					incompatible.resize(incompatible.size() - opposits[str2[0]].size(), 0);
					str2[1] = list.back();
					continue;
				}
			}
			ok = true;
			for (vector<char>::iterator it = incompatible.begin(); it != 
					incompatible.end(); ++it) {
				if (*it == str[j]) {
					incompatible.resize(0, 0);
					list.resize(0, 0);
					ok = false;
					break;
				}
			}
			if (!ok) {
				continue;
			}
			list.push_back(str[j]);
			incompatible.insert(incompatible.end(), opposits[str[j]].begin(),	
					opposits[str[j]].end());
		}
		fout << "Case #" << i + 1 << ": [";
		if (!list.empty()) {
			fout << list[0];
		}
		if (list.size() >1) {
			for (vector<char>::iterator it = list.begin() + 1; it != list.end(); ++it) {
				fout << ", " << *it;
			}			
		}
		fout << "]\n";
	}
	
	return 0;
}
