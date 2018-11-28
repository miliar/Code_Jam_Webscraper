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

	if(input && output) {
		string currentLine;
		int inputs;
		getline(input, currentLine);
		valueOf(currentLine, inputs);

		//cout << inputs << endl;

		string fPart, sPart;
		int second;
		size_t position;

		int casen = 0;

		string result;



		while(getline(input, currentLine)) {

		    int N = 0; // number of buttons needed to be pressed
            int posO = 1; // position of orange
            int posB = 1; // position of blue

            vector<int> positionsO;
            vector<int> positionsB;
            vector<string> robot;

            int time=0;
            string tmpF;
            int tmpVal;

			casen++;

			position = currentLine.find(" ");
			fPart = currentLine.substr(0, position);
			valueOf(fPart, N);
			sPart = currentLine.substr(position+1);

			for(int i=0; i<N; i++) {
			    position = sPart.find(" ");
                fPart = sPart.substr(0, position);
                tmpF = fPart;
                sPart = sPart.substr(position+1);

                position = sPart.find(" ");
                fPart = sPart.substr(0, position);
                valueOf(fPart, tmpVal);

                if(tmpF=="O")
                    positionsO.push_back(tmpVal);
                else if(tmpF=="B")
                    positionsB.push_back(tmpVal);

                robot.push_back(tmpF);
                cout << tmpF;

                sPart = sPart.substr(position+1);
			}
			cout << endl;

			int countsO=0;
			int countsB=0;

			for(int i=0; i<N; i++)
                cout << robot[i];
            cout << endl;

			for(int i=0; i<N; i++) {
                if(robot[i]== "O") {
                    //cout << "O";
                    while(posO != positionsO[countsO]) {
                        time++;
                        if(posO > positionsO[countsO])
                            posO--;
                        else
                            posO++;
                        if(countsB<positionsB.size()) {
                            if(posB > positionsB[countsB])
                                posB--;
                            else if(posB < positionsB[countsB])
                                posB++;
                        }
                    }
                    time++;
                    countsO++;
                    if(countsB<positionsB.size()) {
                        if(posB > positionsB[countsB])
                            posB--;
                        else if(posB < positionsB[countsB])
                            posB++;
                    }
                }
                else if(robot[i]=="B") {
                  //  cout << "B";
                    while(posB != positionsB[countsB]) {
                        time++;
                        if(posB > positionsB[countsB])
                            posB--;
                        else
                            posB++;
                        if(countsO<positionsO.size()) {
                            if(posO > positionsO[countsO])
                                posO--;
                            else if(posO < positionsO[countsO])
                                posO++;
                        }
                    }
                    time++;
                    countsB++;
                    if(countsO<positionsO.size()) {
                        if(posO > positionsO[countsO])
                            posO--;
                        else if(posO < positionsO[countsO])
                            posO++;
                    }
                }

			}
			cout << endl;

            ostringstream oss;
            oss << time;
            result = oss.str();

			output << "Case #" << casen << ": " << result << endl;
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
