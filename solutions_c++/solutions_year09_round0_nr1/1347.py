#include <fstream>
#include <string>
#include <vector>
using namespace std;

int main () {

	ifstream fin("in.txt");
	ofstream fout("out.txt");	

	int l,d,n;
	fin >> l >> d >> n;

	vector <string> words(d);
	for (int i = 0; i < d; i++) fin >> words[i];

	string patt;
	for (int i = 1; i <= n; i++) {
		fin >> patt;
		vector <string> tokens;
		for (int j = 0; j < patt.size(); ) {
			string s;
			if (patt[j] == '(') {
				j++;
				while (patt[j] != ')') {
					s += patt[j];
					j++;
				}
			} else {
				s += patt[j];	
			}
			tokens.push_back(s);
			j++;
		}
		
		int cnt = 0;
		for (int j = 0; j < d; j++) {
			int k;
			for (k = 0; k < words[j].size(); k++) {
				if (tokens[k].find(words[j][k]) == -1) break;
			}
			if (k == words[j].size()) cnt++;
		}
		fout << "Case #" << i << ": " << cnt << "\n";
	}
	return 0;
}