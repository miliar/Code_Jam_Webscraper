#include <sstream>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

template<typename T>
inline bool valueOf(const string &s, T &obj) {
	istringstream is(s);
	return is >> obj;
}

int main(int argc, char *argv[]) {
	ifstream input("B-small-practice.in", ios::in);
	ofstream output("B-small-practice.out", ios::out | ios::trunc);

	if(input && output) {
		string currentLine;
		int inputs;
		getline(input, currentLine);
		valueOf(currentLine, inputs);

		//cout << inputs << endl;

		string fPart, sPart;
		int first, second;
		size_t position;

		int casen = 0;

		string result;

		while(getline(input, currentLine)) {
			casen++;

			int nCombine = 0;
			int nOpposed = 0;
			int nInput = 0;
			vector<string> combination;
			vector<string> opposition;
			string inputString;
			string invokeList;

			position = currentLine.find(" ");
			fPart = currentLine.substr(0, position);
			valueOf(fPart, nCombine);
			sPart = currentLine.substr(position+1);

            for(int i=0; i<nCombine; i++) {
                position = sPart.find(" ");
                fPart = sPart.substr(0, position);
                combination.push_back(fPart);
                sPart = sPart.substr(position+1);
            }

            position = sPart.find(" ");
            fPart = sPart.substr(0, position);
            valueOf(fPart, nOpposed);
            sPart = sPart.substr(position+1);

            for(int i=0; i<nOpposed; i++) {
                position = sPart.find(" ");
                fPart = sPart.substr(0, position);
                opposition.push_back(fPart);
                sPart = sPart.substr(position+1);
            }

            position = sPart.find(" ");
            fPart = sPart.substr(0, position);
            valueOf(fPart, nInput);
            inputString = sPart.substr(position+1);

            invokeList = inputString[0];

            int pos;

            for(int i=1; i<nInput; i++) {
                invokeList.push_back(inputString[i]);

                pos = invokeList.size()-1;

                if(invokeList.size()>1) {
                    for(int j=0; j<nCombine; j++) {
                        if(invokeList[pos] == combination[j].at(0) && invokeList[pos-1] == combination[j].at(1)) {
                            invokeList = invokeList.substr(0, pos-1);
                            invokeList.push_back(combination[j].at(2));
                        }
                        else if(invokeList[pos] == combination[j].at(1) && invokeList[pos-1] == combination[j].at(0)) {
                            invokeList = invokeList.substr(0, pos-1);
                            invokeList.push_back(combination[j].at(2));
                        }
                    }

                    for(int j=0; j<nOpposed; j++) {
                        if(invokeList.find(opposition[j].at(0)) != string::npos && invokeList[pos] == opposition[j].at(1))
                            invokeList.clear();

                        if(invokeList.find(opposition[j].at(1)) != string::npos && invokeList[pos] == opposition[j].at(0))
                            invokeList.clear();
                    }
                }
            }

            for(unsigned int i=0; i<invokeList.size(); i++) {
                result.push_back(invokeList[i]);
                if(i!=invokeList.size()-1)
                    result += string(", ");
            }
			output << "Case #" << casen << ": [" << result << "]" << endl;

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
