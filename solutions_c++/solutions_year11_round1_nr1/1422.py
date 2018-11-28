#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>

using namespace std;

int main() {
	
	ifstream fin ("ainput.txt");
	ofstream fout ("aoutput.txt");
	
	int T, N;
	double PD, PG;
	bool solve1, solve = false;
	
	fin >> T;

	for (int i=0; i<T; i++) {
		fin >> N >> PD >> PG;
		solve1 = false;
		if ((PG == 100 && PD != 100) || (PG == 0 && PD != 0)) {
			fout << "Case #" << i+1 << ": " << "Broken" << endl;
			solve1 = true;
			continue;
		}
		solve = false;
		for (int j=N; j>0; j--) {
			if (j * (PD/100) == int(j * (PD/100))){
				fout << "Case #" << i+1 << ": " << "Possible" << endl;
				solve = true;
				break;
			}
		}
		
		if (solve1 == false && solve == false){
			fout << "Case #" << i+1 << ": " << "Broken" << endl;
		}
	}
	
	return 0;

}