// reading a text file
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <map>
using namespace std;

int max(int a, int b) {
	return a >= b ? a : b;
}
int abs(int a) {
	return a >= 0 ? a : -a;
}

map<char, int> ix;
map<int, char> tostr;

bool opposed[256][256];
char combine[256][256];

int main () {
	int n, m, c, d;
	string s;
	ifstream fin ("in2.txt");
	ofstream fout ("out2.txt");
	fin >> m;
	for(int j = 0; j < m; j++) {
		for(int i = 0; i < 256; i++) for(int j = 0; j < 256; j++) {
			opposed[i][j] = false;
			combine[i][j] = '-';
		}
		fin >> c;
		if (c != 0) for(int i = 0; i < c; i++) {
			fin >> s;
			//cout << s << " ";
			combine[s[0]][s[1]] = s[2];
			combine[s[1]][s[0]] = s[2];
		}
		//cout << " thru!\n";
		fin >> d;
		if (d != 0) for(int i = 0; i < d; i++) {
			fin >> s;
			//cout << s << " ";
			opposed[s[0]][s[1]] = true;
			opposed[s[1]][s[0]] = true;
		}
		//cout << " thru!\n";
		fin >> n;
		//cout << n << "\n";
		fin >> s;
		string curs = "";
		char cur;
		for(int i = 0; i < n; i++) {
			cur = s[i];
			//cout << cur << " ";
			int sz = curs.size();
			bool flag = false;
			if(sz > 0) {
				//cout << curs[sz-1] << " " << cur << " " << combine[ix[curs[sz-1]]][ix[cur]] << " ";
				if(combine[curs[sz-1]][cur] != '-') {
					curs[sz-1] = combine[curs[sz-1]][cur];
					flag = true;
				}
			}
			if(j == 99) cout << curs << " ";
			//else cout << 'X' << " ";
			//cout << flag << " ";
			//cout << "SHOULD BE X: " << combine[ix['E']][ix['A']] << " ";
			//cout << curs << flag << " ";
			if(!flag) for(int i = 0; i < sz; i++)
				if(opposed[curs[i]][cur]) {
					curs = "";
					flag = true;
					break;
				}
			if(j == 99) cout << curs << " ";
			//cout << curs << flag << " " ;
			if(!flag) curs = curs + cur;
			if(j == 99) cout << curs << "\n";
		}
		//cin >> c;
		fout << "Case #" << j+1 << ": [";
		for(int i = 0; i < curs.size(); i++) if(i != curs.size()-1) fout << curs[i] << ", ";
		if(curs.size() > 0) fout << curs[curs.size()-1];
		fout << "]\n";
	}
	cin >> n;
  return 0;
}
