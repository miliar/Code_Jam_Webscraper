#include <fstream>
#include <iostream>
using namespace std;

int main() {
	int N, index, set, mask, leftP, rightP, leftS, rightS, profit;
	long long limit;
	int inputs[15];

	ifstream fin("C.in");
	ofstream fout("C.out");

	int test_cases;
	fin >> test_cases;

	for (int current_case = 0; current_case < test_cases; current_case++) {
		fin >> N;
		for (index = 0; index < N; index++)
			fin >> inputs[index];

		profit = -1;
		limit = (1 << N) - 1;

		for (set = 1; set < limit; set++) {
			leftP = rightP = leftS = rightS = 0;
			for (index = 0, mask = 1; index < N; index++) {
				if (mask & set) {
					leftP ^= inputs[index];
					leftS += inputs[index];
				} else {
					rightP ^= inputs[index];
					rightS += inputs[index];
				}
				
				mask <<= 1;
			}
			
			if (leftP == rightP) {
				if (profit < leftS)
					profit = leftS;
				if (profit < rightS)
					profit = rightS;
			}
		}
		
		if (profit == -1)
			fout << "Case #" << (current_case + 1) << ": NO" << endl;
		else
			fout << "Case #" << (current_case + 1) << ": " << profit << endl;
	}
}
