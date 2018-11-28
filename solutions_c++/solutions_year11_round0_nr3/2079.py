#include <sstream>
#include <fstream>
#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

template<typename T>
inline bool valueOf(const string &s, T &obj) {
	istringstream is(s);
	return is >> obj;
}

int main(int argc, char *argv[]) {
	ifstream input("C-small-practice.in", ios::in);
	ofstream output("C-small-practice.out", ios::out | ios::trunc);

	if(input && output) {
		string currentLine;
		int inputs;
		getline(input, currentLine);
		valueOf(currentLine, inputs);

		//cout << inputs << endl;

		string fPart, sPart;
		size_t position;

		int casen = 0;

		string result;

		while(getline(input, currentLine)) {
			casen++;
			int tableSize = 0;
			int min;

			valueOf(currentLine, tableSize);

			getline(input, sPart);
			int numberTmp;
			vector<int> table;

			position = sPart.find(" ");
            fPart = sPart.substr(0, position);
            valueOf(fPart, numberTmp);
            table.push_back(numberTmp);
            sPart = sPart.substr(position+1);

            min = numberTmp;

			for(int i=1; i<tableSize; i++) {
                position = sPart.find(" ");
                fPart = sPart.substr(0, position);
                valueOf(fPart, numberTmp);
                table.push_back(numberTmp);
                sPart = sPart.substr(position+1);
                if(numberTmp<min)
                    min = numberTmp;
			}
			//valueOf(sPart, numberTmp);
			//table.push_back(numberTmp);

			int sumXor = 0;
			for(int i=0; i<tableSize; i++)
                sumXor ^= table[i];

            int resultTmp=0;
			if(sumXor != 0)
                result = "NO";
            else {
                for(int i=0; i<tableSize; i++)
                    resultTmp+=table[i];

                resultTmp-=min;

                cout << resultTmp;

                ostringstream oss;
                oss << resultTmp;
                result = oss.str();
            }

            //cout << tableSize << endl;

            //cout << sumXor << endl;

			// algorithm

			output << "Case #" << casen << ": " << result << endl;
			result.clear();
		}

		if(!casen == inputs)
			cerr << "Not the good amount of cases" << endl;

		input.close();
		output.close();
	}
	else
		cerr << "Unable to open input or output file" << endl;
	return 0;
}
