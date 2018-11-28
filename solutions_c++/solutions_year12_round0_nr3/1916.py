#include <fstream>
#include <string>

using namespace std;

const size_t MaxBufferSize = 32;

string shift(const string &shiftWhat) {
	char result[MaxBufferSize];
	for (size_t i = 1; i < shiftWhat.length(); ++i) {
		result[i - 1] = shiftWhat[i];
	}
	result[shiftWhat.length() - 1] = shiftWhat[0];
	result[shiftWhat.length()] = '\0';
	return result;
}

int main(int argc, char *argv[]) {
	ifstream input("input.txt");
	ofstream output("output.txt");
	
	size_t cases;
	input >> cases;

	char buffer[MaxBufferSize];
	for (size_t i = 1; i <= cases; ++i) {
		int lower, upper;
		input >> lower >> upper;

		size_t pairs = 0;
		for (int cur = lower; cur <= upper; ++cur) {
			itoa(cur, buffer, 10);
			string curStr(buffer);
			string shifted = shift(curStr);
			while (shifted != curStr) {
				int shiftedAsNum = atoi(shifted.c_str());
				bool ok = shifted[0] != '0' && shiftedAsNum >= lower && shiftedAsNum <= upper && shiftedAsNum < cur;
				pairs += ok;
				shifted = shift(shifted);
			}
		}

		output << "Case #" << i << ": " << pairs << endl;
	}
}