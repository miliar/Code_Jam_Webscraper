#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>


using namespace std;

void processLine(string line, int lineN, ostream& out)
{
	std::string str = "welcome to code jam";

	int len = str.length();
	size_t len2 = line.length();

	std::vector<int> prevFreq(len2, 1);

	for (int i=len; --i>=0; ) {
		std::vector<int> freq(len2, 0);
		char curLetter = str[i];

		for (size_t j=0; j<len2; j++) {
			if (line[j] == curLetter) {
				if (i == len-1) {
					freq[j] = 1;
				} else {
					int accum = 0;
					for (size_t k=j+1; k<len2; k++) {
						accum += prevFreq[k];
						accum %= 10000;
					}
					freq[j] = accum;
				}
			}
		}

		prevFreq = freq;
	}

	int result = 0;
	for (size_t k=0; k<len2; k++) {
		result += prevFreq[k];
		result %= 10000;
	}

	out << "Case #" << lineN << ": " << std::setfill('0') << std::setw(4) << result << endl;
}

int main()
{
	ifstream in("C-large.in");
	ofstream out("C-large.out", std::ios_base::out | std::ios_base::binary);
	//ostream& out = cout;

	int nLines;
	in >> nLines;
	char buffer[1024];
	in.getline(buffer, 1024);
	for (int i=0; i<nLines; i++) {
		in.getline(buffer, 1024);
		string line(buffer);
		processLine(line, i+1, out);
	}

	out.flush();
}
