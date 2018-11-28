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

unsigned int freqs[100];

int main(void) {
	unsigned int T = 0; // number of test cases
	
	std::cin >> T;
	
	for (unsigned int i=0 ; i<T ; ++i) {
		unsigned int N = 0; // Num of other players
		unsigned int L = 0; // Low
		unsigned int H = 0; // High
		std::cin >> N >> L >> H;
		
//		vector<vector<unsigned int>> tiles;
		for (unsigned int j=0 ; j<N ; ++j) {			
			std::cin >> freqs[j];
		}
		
		bool success = true;
		
		for (unsigned int k=L ; k<=H ; ++k) {
			success = true;
			
			for (unsigned int j=0 ; j<N ; ++j) {	
	//			std::cout << "Testing " << freqs[j] << " " << k << std::endl;
				//std::cout << 8 % 1 << std::endl;
				
				if (!(freqs[j] == k)) {
	//				std::cout << "False success1" << std::endl;
					if (!((freqs[j] > k) && ((freqs[j] % k) == 0))) {
	//					std::cout << "False success2" << std::endl;
	//					std::cout << (k > freqs[j]);
						if (!((k > freqs[j]) && ((k % freqs[j]) == 0))) {
	//						std::cout << "False success3" << std::endl;
							success = false;
							break;
						}
					}
				}

				/*
				if ( (freqs[j] == k) || 
					 ((freqs[j] > k) && ((freqs[j] % k) == 0)) || 
					 ((k > freqs[j]) && ((k % freqs[j]) == 0)) ) {
				} else {
					std::cout << "False success" << std::endl;
					success = false;
					break;
				}
				 */
				
			}
			
			if (success) {
				std::cout << "Case #" << i+1 << ": " << k << std::endl;
				break;
			}
		}

		if (!success) {
			std::cout << "Case #" << i+1 << ": NO" << std::endl;
		}
	}
}


