#include <iostream>
#include <vector>

using namespace std;


unsigned int GetXor(vector<unsigned int> &v) {	
	unsigned int result = 0;
	
	for (unsigned int i=0 ; i<v.size() ; ++i) {
		result ^= v[i];
	}
	
	return result;
}

unsigned int GetSumWithoutMin(vector<unsigned int> &v) {
	unsigned int sum = 0;
	unsigned int min = 1000001;
	
	for (unsigned int i=0 ; i<v.size() ; ++i) {
		sum += v[i];
		
		if (v[i] < min) {
			min = v[i];
		}
	}
	
	return sum - min;	
}

unsigned char tiles[50][50];

int main(void) {
	unsigned int T = 0; // number of test cases
	
	std::cin >> T;
	
	for (unsigned int i=0 ; i<T ; ++i) {
		unsigned int R = 0; // Rows
		unsigned int C = 0; // Cols
		std::cin >> R >> C;
		
//		vector<vector<unsigned int>> tiles;
		for (unsigned int j=0 ; j<R ; ++j) {			
			for (unsigned int k=0 ; k<C ; ++k) {
				unsigned char c = 0;
				std::cin >> c;
				tiles[j][k] = c;
			}
		}

		bool success = true;
		for (unsigned int j=0 ; j<R ; ++j) {			
			for (unsigned int k=0 ; k<C ; ++k) {
				if (tiles[j][k] == '#') {
					if ((j == R-1) || (k == C-1) || (tiles[j+1][k] != '#') || (tiles[j+1][k+1] != '#') || (tiles[j][k+1] != '#')) {
						success = false;
						break;
					} else {
						tiles[j][k] = '/';
						tiles[j][k+1] = '\\';
						tiles[j+1][k] = '\\';
						tiles[j+1][k+1] = '/';
					}
				}
			}
		}
		
		// Print out
		std::cout << "Case #" << i+1 << ":" << std::endl;
		if (!success) {
			std::cout << "Impossible" << std::endl;
		} else {
			for (unsigned int j=0 ; j<R ; ++j) {			
				for (unsigned int k=0 ; k<C ; ++k) {
					std::cout << tiles[j][k];
				}			
				std::cout << std::endl;
			}
		}
	}
}


