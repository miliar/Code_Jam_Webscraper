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
float WPsoFar(int Team, int Match, vector<string> Matches) {
    float won = 0;
    float total = 0;
    for(int i=0; i<(int)Match; i++) {
        if(Matches.at(Team).at(i) != '.') {
            total++;
            if(Matches.at(Team).at(i) == '1')
                won++;
        }
    }
    return won/total;
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
		string fPart, sPart;
		int casen = 0;
		string result;
		vector<string> lines;
		string line;
		int R = 0;
		int C = 0;
		size_t position;
		bool possible = true;
		bool currently = false;

		while(getline(input, currentLine)) {
		    casen++;
		    result.clear();
		    lines.clear();
		    possible = true;
		    currently = false;
            position = currentLine.find(" ");
			fPart = currentLine.substr(0, position);
			valueOf(fPart, R);
			sPart = currentLine.substr(position+1);
			valueOf(sPart, C);
			for(int i=0; i<R; i++) {
			    getline(input, line);
                lines.push_back(line);
			}

			for(int i=0; i<R && possible; i++) {
                for(int j=0; j<C && possible; j++) {
                    if(lines.at(i).at(j) == '#')
                        currently = !currently;
                    else {
                        if(currently)
                            possible = false;
                    }
                }
                if(currently)
                    possible = false;
			}
            for(int j=0; j<C && possible; j++) {
                    for(int i=0; i<R && possible; i++) {
                        if(lines.at(i).at(j) == '#')
                            currently = !currently;
                        else {
                            if(currently)
                                possible = false;
                        }
                    }
                    if(currently)
                        possible = false;
            }

            if(possible) {
                if(lines.at(0).at(0) == '#')
                    lines.at(0).at(0) = '/';
                for(int i=1; i<C; i++) {
                    if(lines.at(0).at(i) == '#') {
                        if(lines.at(0).at(i-1) == '/')
                            lines.at(0).at(i) = '\\';
                        else
                            lines.at(0).at(i) = '/';
                    }
                }
                currently = false;
                for(int i=1; i<R; i++) {
                    if(lines.at(i).at(0) == '#') {
                        if(lines.at(i-1).at(0) == '/')
                            lines.at(i).at(0) = '\\';
                        else
                            lines.at(i).at(0) = '/';
                    }
                }

                for(int i=1; i<R; i++) {
                    currently = false;
                    for(int j=1; j<C; j++) {
                        if(lines.at(i).at(j) == '#') {
                            currently = !currently;
                            if(lines.at(i).at(j-1) == '/' && lines.at(i-1).at(j-1) != '\\') {
                                lines.at(i).at(j) = '\\';
                            }
                            else if(lines.at(i-1).at(j) == '/') {
                                lines.at(i).at(j) = '\\';
                            }
                            else {
                                lines.at(i).at(j) = '/';
                            }
                        }
                    }
                }
                for(int i=0; i<R; i++) {
                    result.append(lines.at(i));
                    if(i!=R-1)
                        result.append("\n");
                }
            }
            else {
                result = "Impossible";
            }

			//algorithm

			ostringstream oss;
			oss << result;
			result = oss.str();
			output << "Case #" << casen << ":" << endl << result << endl;
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
