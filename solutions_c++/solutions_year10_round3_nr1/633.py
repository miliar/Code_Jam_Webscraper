#include <iostream>
#include <sstream>
#include <set>
#include <vector>


int main ()
{
	int	numberOfCases	= 0;
	int	counter			= 0;
	int maxN			= 1000;
	
	std::cin >> numberOfCases;
	
	while (counter < numberOfCases) {
		int	result	= 0;
		int n		= 0;
		int nextIndex	= 0;
		int A[maxN];
		int B[maxN];

		std::cin >> n;
		
		for (int i = 0; i < n; ++i) {
			int coord;
			
			std::cin >> coord;
			A[nextIndex] = coord;

			std::cin >> coord;
			B[nextIndex] = coord;

			++nextIndex;

			for (int j = 0; j < nextIndex - 1; ++j) {
				if ((A[j] > A[nextIndex - 1] && B[j] > B[nextIndex - 1]) ||
					(A[j] < A[nextIndex - 1] && B[j] < B[nextIndex - 1]))
					continue;

				++result;
			}
		}

		std::cout << "Case #" << ++counter << ": " << result << std::endl;
	}
}