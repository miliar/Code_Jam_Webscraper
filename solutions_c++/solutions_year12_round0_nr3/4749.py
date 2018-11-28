#include <iostream>
#include <set>
#include <string>
#include <algorithm>
#include <sstream>

bool isRecycledPair(int n, int m)
{
	std::stringstream buf;
	std::string nStr, mStr;

	buf << n;
	nStr = buf.str();
	buf.str("");
	buf << m;
	mStr = buf.str();
	buf.str("");

	if(nStr.length() != mStr.length())
		return false;

	for(int i = nStr.length() - 1; i >= 0; i--) {
		std::string cStr;

		cStr = nStr.substr(i);
		cStr += nStr.substr(0, i);
		
		if(cStr == mStr)
			return true;
	}

	return false;
}

int main(int argc, char *argv[])
{
	int num_inputs;

	isRecycledPair(12345, 34512);

	std::cin >> num_inputs;

	for(int cs = 1; cs <= num_inputs; cs++) {
		int lbound, ubound;
		int pairs = 0;

		std::cin >> lbound >> ubound;

		for(int i = lbound; i <= ubound; i++) {

			for(int j = i + 1; j <= ubound; j++) {
				
				if(isRecycledPair(i, j))
					pairs++;

			}

		}

		std::cout << "Case #" << cs << ": " << pairs << std::endl;

	}
}