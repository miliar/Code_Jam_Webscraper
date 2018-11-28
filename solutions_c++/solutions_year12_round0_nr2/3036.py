#include <fstream>
#include <algorithm>
#include <iostream>

using namespace std;

int main() {
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int T;
	fin >> T;
	
	for (int i = 1; i <= T; ++i) {
		int num, s, p;
		fin >> num >> s >> p;
		fout << "Case #" << i << ": ";
		int scores[num];
		for (int j = 0; j < num; ++j) {
			fin >> scores[j];
		}
		sort (scores, scores+num);
		int j = num - 1;
		for (; j >= 0; --j) {
			if ((scores[j] + 2)/3 < p){
				if (p > 1)
					for (; s > 0 && j >= 0; --s) {
						if ((scores[j]+4)/3 < p){
							++j;
							s = 0;
						}
						--j;
					}
				fout << (num - j) - 1 << "\n";
				j = 0;
			}
			else if (j == 0){
				fout << num << "\n";
			}
		}
	}
	
	return 0;
}