#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

ifstream fin("input.txt");

int main() {

	int T,N,x;

	fin >> T;

	int hp = 0;	

	for (int t=1;t<=T;++t) {

		hp = 0;

		fin >> N;
		
		for (int i=1;i<=N;i++) {
			fin >> x;
			if (x != i) hp += 1;
		}

		cout << "Case #" << t << ": "<< fixed << setprecision(6) << (double)hp << "\n";

	}
	
	
	
	return 0;

}
