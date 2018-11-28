#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

int main(int argc, char * argv[]) {
	
	fstream dataSet ("data.txt", fstream::in);
	fstream output ("out.txt", fstream::out);

	int testCaseCount;
	dataSet >> testCaseCount;

	for (int z = 0; z < testCaseCount; z++) {
		unsigned int N, K;
		
		dataSet >> N;
		dataSet >> K;

		N = 1 << N;
		K++;

		output << "Case #" << (z+1) << ": " << ((K % N == 0) ? "ON" : "OFF") << endl;
		}


	dataSet.close();
	output.close();

	return 0;
	}
