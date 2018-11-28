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


int main(void) {
	unsigned int T = 0; // number of test cases
	
	std::cin >> T;
	
	for (unsigned int i=0 ; i<T ; ++i) {
		unsigned int N = 0; // number of candies [2, 1000]
		std::cin >> N;
		
		vector<unsigned int> candies;
		for (unsigned int j=0 ; j<N ; ++j) {
			unsigned int c = 0;
			std::cin >> c;
			candies.push_back(c);
		}
		
		if (GetXor(candies)) {
			std::cout << "Case #" << i+1 << ": NO" << std::endl;
		} else {
			std::cout << "Case #" << i+1 << ": " << GetSumWithoutMin(candies) << std::endl;
		}
	}
}


