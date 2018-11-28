#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <fstream>
using namespace std;

void main () {
	ifstream f ("input.txt");
	ofstream of ("output.txt");
	int T = 0;
	f >> T;
	for (int i = 0; i < T; ++i) {

		//read combinations
		int C = 0;
		f >> C;
		map<string,char> comb;
		for (int j = 0; j < C; ++j) {
			string combination;
			f >> combination;
			string comb_from = combination.substr(0,2);
			comb[comb_from] = combination[2];
			reverse(comb_from.begin(), comb_from.end());
			comb[comb_from] = combination[2];
		}

		//read disallowed pairs
		int D = 0;
		f >> D;
		map < char, set<char> > dis;
		set<char> emp;
		dis['Q'] = emp; dis['W'] = emp; dis['E'] = emp; dis['R'] = emp;
		dis['A'] = emp; dis['S'] = emp; dis['D'] = emp; dis['F'] = emp;

		for (int j = 0; j < D; ++j) {
			string disall;
			f >> disall;
			char c1 = disall[0];
			char c2 = disall[1];
			dis[c1].insert(c2);
			dis[c2].insert(c1);
		}

		//read input list
		int N = 0;
		f >> N;
		string input;
		f >> input;

		string output = "";
		output += input[0];
		int Len = 1;
		set<char> list;
		list.insert(input[0]);
		for (int j = 1; j < N; ++j) {
			char c = input[j];
			char cl = output[Len-1];
			string t_comb = "  ";
			t_comb[0] = c; t_comb[1] = cl;

			// test combination
			if ( comb.find(t_comb) != comb.end() ) {
				output[Len-1] = comb[t_comb];
				if ( find(output.begin(), output.end(), cl) == output.end() ) {
					list.erase(cl);
				}
			} else {
				//test disallowed
				vector<char> intersect(8,'0');
				vector<char>::iterator it = set_intersection(list.begin(),list.end(),dis[c].begin(),dis[c].end(),intersect.begin());
				if (it - intersect.begin() > 0) {
					j++;
					list.clear();
					if (j < N) {
						Len = 1;
						output = input.substr(j,1);				
						list.insert(input[j]);
					} else {
						Len = 0;
						output = "";
					}
				} else {
					output += c;
					list.insert(c);
					Len++;
				}
			}
		}
		
		//cout << "Case #" << i+1 << ": [";
		of << "Case #" << i+1 << ": [";
		if (output.size() > 0) {
			//cout << output[0];
			of << output[0];
			for (int j = 1; j < output.size(); ++j) {
				//cout << ", " << output[j];
				of << ", " << output[j];
			}
		}
		//cout << "]" << endl;
		of << "]" << endl;
	}
	f.close();
	of.close();
	cin.get();
}