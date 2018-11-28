#include <iostream>
#include <list>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	
	ifstream fin ("q2input.txt");
	ofstream fout ("q2output.txt");
	
	int T, C, D, N, cSize, oSize, sSize;
	char first, second;
	char tmp;
	vector<char> series, temp;
	vector< vector<char> > comb, opp;
	char last;
	fin >> T;
	
	for (int i=0; i<T; i++) {
		fin >> C;
		for (int j=0; j<C; j++) {
			for (int h =0; h<3; h++) {
				fin >> tmp;
				temp.push_back(tmp);
			}
			comb.push_back(temp);
			temp.clear();
		}
		fin >> D;
		for (int j=0; j<D; j++) {
			for (int h=0; h<2; h++) {
				fin >> tmp;
				temp.push_back(tmp);
			}
			opp.push_back(temp);
			temp.clear();
		}
		fin >> N;
		series.push_back('0');
		for (int j=0; j<N; j++) {
			fin >> tmp;
			series.push_back(tmp);
			cSize = comb.size();
			for (int k=0; k<cSize; k++) {
				first = comb[k][0];
				second = comb[k][1];
				last = series[series.size()-2];
				if ((last == first && series.back() == second) || (last == second && series.back() == first)){
					series.pop_back();
					series.pop_back();
					series.push_back(comb[k][2]);
				}
			}
			oSize = opp.size();
			for (int k=0; k<oSize; k++) {
				first = opp[k][0];
				second = opp[k][1];
				if (series.back() == first && count(series.begin(), series.end(), second) != 0) {
					series.clear();
					series.push_back('0');
				}
				else if (series.back() == second && count(series.begin(), series.end(), first) != 0) {
					series.clear();
					series.push_back('0');
				}
			}
			
		}
		fout << "Case #" << i+1 << ": [";
		sSize = series.size(); 
		sSize--;
		for (int y=1; y<sSize; y++) {
			fout << series[y] << ", ";
		}
		if (series.back() != '0')
			fout << series.back();
		fout << "]" << endl;

		comb.clear();
		series.clear();
		opp.clear();
	}
	
	return 0;
}