#include      <iostream>
#include      <fstream>
#include      <vector>

char achCombined[256][256];
bool abOpposed[256][256];

int main(int argc, char **argv) {
	int nTests;
	int nCombinations;
	int nOppposed;
	int nInvoked;
	bool bChanged;

	std::vector<char> VectCurState;

	char chTmp1, chTmp2;

	std::ifstream in("in");
	std::ofstream out("out");
	in >> nTests;

	unsigned int nLastElement;

	for (int nTest = 1; nTest <= nTests; ++nTest) {
		VectCurState.clear();
		for (int i = 0; i < 256; ++i) {
			for (int j = 0; j < 256; ++j) {
				achCombined[i][j] = 0;
				abOpposed[i][j] = 0;
			}
		}

		in >> nCombinations;

		for (int i = 0; i < nCombinations; ++i) {
			in >> chTmp1;
			in >> chTmp2;
			in >> achCombined[(int)chTmp1][(int)chTmp2];
			achCombined[(int)chTmp2][(int)chTmp1] = achCombined[(int)chTmp1][(int)chTmp2];
		}

		in >> nOppposed;

		for (int i = 0; i < nOppposed; ++i) {
			in >> chTmp1;
			in >> chTmp2;
			abOpposed[(int)chTmp1][(int)chTmp2] = true;
			abOpposed[(int)chTmp2][(int)chTmp1] = true;
		}

		in >> nInvoked;

		for (int i = 0; i < nInvoked; ++i) {
			in >> chTmp1;

			VectCurState.push_back(chTmp1);

			bChanged = true;

			while(bChanged){
				bChanged = false;

				while (VectCurState.size() > 1) {
					chTmp1 = achCombined[(int)VectCurState[VectCurState.size() - 1]][(int)VectCurState[VectCurState.size() - 2]];

					if (chTmp1 != 0) {
						VectCurState.pop_back();
						VectCurState.pop_back();
						VectCurState.push_back(chTmp1);
					}else{
						break;
					}
				}

				if (VectCurState.size() > 1) {
					nLastElement = VectCurState.back();
					for (unsigned int nPosStart = 0; nPosStart < VectCurState.size() - 1; ++nPosStart) {
						if (abOpposed[(int)VectCurState[nPosStart]][nLastElement]) {
							//VectCurState.erase(VectCurState.begin() + nPosStart, VectCurState.end());
							//bChanged = true;
							VectCurState.clear();
							break;
						}
					}
				}
			}
		}

		out << "Case #" << nTest << ": [";
		std::vector<char>::const_iterator it = VectCurState.begin();

		if (it != VectCurState.end()) {
			out << *(it++);
		}

		for (; it != VectCurState.end(); ++it) {
			out << ", " << *it;
		}

		out << ']' << std::endl;
	}

	out.close();
	in.close();

	return 0;
}
