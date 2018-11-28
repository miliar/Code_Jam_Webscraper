#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <sstream>
using namespace std;

int main() {
	ifstream fin("B-large.in");
	//ifstream fin("test.in");
	ofstream fout("output.txt");
	int T, C, D, N;
	fin >> T;
	for(int i = 0; i < T; i++) {
		map<pair<char, char>, bool> opposed;
		map<pair<char, char>, char> combine;
		//for(int j = 'A'; j <= 'Z'; j++)
		//	for(int k = 'A'; k <= 'Z'; k++)
		//		opposed[make_pair(j, k)] = combine[make_pair(j, k)] = 0;
		string list = "";
		fin >> C;
		for(int j = 0; j < C; j++) {
			char a, b, c;
			fin >> a >> b >> c;
			combine[make_pair(a, b)] = combine[make_pair(b, a)] = c;
		}
		fin >> D;
		for(int j = 0; j < D; j++) {
			char a, b;
			fin >> a >> b;
			opposed[make_pair(a, b)] = opposed[make_pair(b, a)] = true;
		}
		fin >> N;
		for(int j = 0; j < N; j++) {
			char c;
			fin >> c;
			//fout << c;
			bool comb = false;
			if(list.size() > 0) {
				pair<char, char> p = make_pair(c, list[list.size() - 1]);
				char fused = combine[p];
				if(fused) {
					comb = true;
					list = list.substr(0, list.size() - 1) + fused;
				}
			}
			if(!comb) {
				bool opp = false;
				for(unsigned int k = 0; k < list.size(); k++) {
					pair<char, char> p = make_pair(c, list[k]);
					if(opposed[p]) {
						opp = true;
						break;
					}
				}
				if(!opp) {
					stringstream ss("");
					ss << c;
					list += ss.str();
				}
				else
					list = "";
			}
			//fout << list << endl;
		}
		//fout << endl;
		fout << "Case #" << i + 1 << ": [";
		for(unsigned int j = 0; j < list.size(); j++) {
			fout << list[j];
			if(j < list.size() - 1) fout << ", ";
		}
		fout << "]" << endl;
	}
	fin.close();
	fout.close();
	return 0;
}