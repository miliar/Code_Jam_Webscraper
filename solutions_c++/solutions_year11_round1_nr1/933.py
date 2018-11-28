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
	ifstream input("A-small-practice.in", ios::in);
	ofstream output("A-small-practice.out", ios::out | ios::trunc);
	ofstream log("logs", ios::out | ios::trunc);
	if(input && output) {
		string currentLine;
		int inputs;
		getline(input, currentLine);
		valueOf(currentLine, inputs);
		string fPart, sPart, tPart;
		int N, PD, PG;
		size_t position;
		int casen = 0;
		string result;
		while(getline(input, currentLine)) {
		    result.clear();
			casen++;
			position = currentLine.find(" ");
			fPart = currentLine.substr(0, position);
			valueOf(fPart, N);
			sPart = currentLine.substr(position+1);

			position = sPart.find(" ");
			tPart = sPart.substr(position+1);
			valueOf(tPart, PG);

			sPart = sPart.substr(0, position);
			valueOf(sPart, PD);

			cout << N << " " << PD << " " << PG << endl;

			bool diff = true;
			int min = N;
			for(int i=N; i>0; i--) {
                if(PD*i%100==0) {
                    diff = false;
                    min = i;
                    break;
                }
			}
			if(diff)
                result = "Broken";
            else {
                if((PG==100 && PD != 100) || (PG==0 && PD!=0))
                    result = "Broken";
                else {
                    result = "Possible";
                }
            }

			//algorithm

			/*ostringstream oss;
			oss << ;
			result = oss.str();*/
			output << "Case #" << casen << ": " << result << endl;
		}
		if(!casen == inputs)
			cerr << "Not the good amount of cases" << endl;
		input.close();
		output.close();
		log.close();
	}
	else
		cerr << "Unable to open input or output file" << endl;
	return 0;
}
