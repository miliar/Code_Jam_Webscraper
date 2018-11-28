#include <vector>
#include <iostream>
#include <fstream>

using namespace std;

int patrick_add( int num1, int num2 ) {
	int mask = ~( num1 & num2 );

	return ( (num1 & mask) | (num2 & mask) );
}

int testCase(const vector<int>& candies) {
	int best = 0;
	int count = candies.size();

	for (unsigned int i = 1; i < 1<<(count-1); i++) {
		int valA = 0;
		int valB = 0;

		int valA_real = 0;
		int valB_real = 0;

		for (int j = 0; j < count; j++) {
			if ( ((i >> j) & 1) == 1 ) {
				valA = patrick_add( valA, candies[j] );
				valA_real += candies[j];
			} else {
				valB = patrick_add( valB, candies[j] );
				valB_real += candies[j];
			}
		}

		if (valA == valB) {
			if (valA_real > best) {
				best = valA_real;
			}
			
			if (valB_real > best) {
				best = valB_real;
			}
		}
	}
	
	return best;
}

int main(int argc, char** argv) {
	ifstream fin;

	string filename = "c.in";

	if (argc > 1) {
		filename = argv[1];
	}

	fin.open(filename, ios_base::in);

	int T;

	fin >> T;

	for (int i = 0; i < T; i++) {
		int N;
		fin >> N;

		vector<int> candies;

		for (int j = 0; j < N; j++) {
			int Ci;
			fin >> Ci;
			candies.push_back(Ci);
		}

		int result = testCase( candies );

		cout << "Case #" << (i+1) << ": ";
		if (result > 0) {
			cout << result ;
		} else {
			cout << "NO";
		}
		cout << endl;
	}

	//cin.get();

	return 1;
}