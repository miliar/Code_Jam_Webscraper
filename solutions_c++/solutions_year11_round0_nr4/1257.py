#include <iostream>
#include <vector>
#include <stdio.h>

using namespace std;

int main(void) {
	unsigned int T = 0; // number of test cases
	
	std::cin >> T;
	
	for (unsigned int i=0 ; i<T ; ++i) {
		unsigned int N = 0; // number of elems
		std::cin >> N;
		
		//vector<unsigned int> numbers;
		double result = 0;
		
		for (unsigned int j=1 ; j<=N ; ++j) {
			unsigned int elem = 0;
			std::cin >> elem;
			
			if (elem != j) {
				result++;
			}
		}

		printf("Case #%d: %f\n", i+1, result);
//		std::cout << "Case #" << i+1 << ": " << result << endl;
	}
}


