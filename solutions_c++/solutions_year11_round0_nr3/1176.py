#include      <iostream>
#include      <fstream>

void fnPerm(bool bUsed[], int nUsed){
}

int main(int argc, char **argv) {
	int nTests;
	int nCandies;
	int anCandies[1000];
	int i;
	long long nLeft, nRight, nLeftReal, nRightReal;
	long long nMax;
	bool bUsed[1000];

	std::ifstream in("in");
	std::ofstream out("out");
	in >> nTests;

	for (int nTest = 1; nTest <= nTests; ++nTest) {
		in >> nCandies;

		nLeft      = 0;
		nRight     = 0;
		nLeftReal  = 0;
		nRightReal = 0;
		nMax       = -1;

		for (i = 0; i < nCandies; ++i) {
			in >> anCandies[i];

			bUsed[i] = false;
			nLeft ^= anCandies[i];
			nLeftReal += anCandies[i];
		}

		for (int j = 0; j < (2 << (nCandies - 1)) - 2; ++j) {
			i = 0;

			while(bUsed[i] == true && i < nCandies){
				bUsed[i] = false;
				nRight ^= anCandies[i];
				nRightReal -= anCandies[i];
				nLeft ^= anCandies[i];
				nLeftReal += anCandies[i];
				++i;
			}

			if (i < nCandies) {
				bUsed[i] = true;
				nRight ^= anCandies[i];
				nRightReal += anCandies[i];
				nLeft ^= anCandies[i];
				nLeftReal -= anCandies[i];
			}

			//for (int a = 0; a < nCandies; ++a) {
				//std::cout << bUsed[a];
			//}
			//std::cout << " (" << nLeft << ", " << nLeftReal << ") (" << nRight << ", " << nRightReal << ")" << std::endl;

			if (nLeft == nRight) {
				if (nMax < nRightReal) {
					nMax = nRightReal;
				}
				if (nMax < nLeftReal) {
					nMax = nLeftReal;
				}
			}
		}

		out << "Case #" << nTest << ": ";
		if (nMax == -1) {
			out << "NO";
		}else{
			out << nMax;
		}
		out << std::endl;
	}

	in.close();

	return 0;
}
