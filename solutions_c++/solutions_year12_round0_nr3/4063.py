#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstdlib>
using namespace std;

int main(int argc, char ** argv){

	ifstream inFile;
	inFile.open(argv[1]);

	ofstream outFile;
	outFile.open(argv[2]);

	int numCases, A, B;
	inFile >> numCases;

	for (int i = 1; i <= numCases; i++){
		inFile >> A >> B;
		int numMatches = 0;
		for (int n = A; n < B; n++){
			for (int m = n + 1; m <= B; m++){
				//rotate number;
				string num1, num2;
				char buff[8];
				sprintf(buff,"%d", m); 
				num2 = buff;
				int len = num2.length();

				for (int j = 0; j < len; j++){
					rotate(num2.begin(), num2.begin()+1, num2.end());
					if (n == atoi(num2.c_str())){
						numMatches++;
						break;
					}
				}

			}

		}
		outFile << "Case #" << i << ": " << numMatches << endl;
	}
	inFile.close();
	outFile.close();
	return 0;
}
