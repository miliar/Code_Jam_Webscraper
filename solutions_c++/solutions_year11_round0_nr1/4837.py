#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <string>
#include <cmath>

using namespace std;

string readfile(char *fn) {
	static ifstream fin;
	
	if( !fin.is_open() ) {
		fin.open(fn);
		//cout << "Open\n";
	}
	
	string s;
	getline(fin, s);
	//cout << s << endl;

	if( fin.eof() ) {
		fin.close();
		//cout << "close\n";
	}

	return s;
}

int m(string s) {
	int time = 0;
	int bla = 0, ola = 0;
	int blp = 1, olp = 1;
	int end, pos, i;
	
	string str_buttons = s.substr(0, s.find(" ", 0));
	int buttons = atoi(str_buttons.c_str());
	s = s.substr(str_buttons.length()+1, s.length());
	//cout << buttons << " --- " << s <<endl;
	
	for(i = 0; i < buttons; i++) {
		string act = s.substr(0, 1);
		end = s.find(" ", 2);
		end = (end > 0)?end:s.length();
		pos = atoi(s.substr(2, end).c_str());

		if(time != 0) {
			if(act.find("B", 0) != string::npos) {
				if(bla == time) {
					time += abs(blp-pos) + 1;
				}
				else {
					if((time-bla) >= abs(blp-pos)) {
						time += 1;
					}
					else {
						time = abs(blp-pos) + bla + 1;
					}
				}
				
				blp = pos;
				bla = time;
			}
			else {
				if(ola == time) {
					time += abs(olp-pos) + 1;
				}
				else {
					if((time-ola) >= abs(olp-pos)) {
						time += 1;
					}
					else {
						time = abs(olp-pos) + ola + 1;
					}
				}
				
				olp = pos;
				ola = time;			
			}
		}
		else {
			time = pos;		// NOT pos + 1 since it is starting from 1
			if(act.find("B", 0) != string::npos) {
				bla = time;
				blp = pos;
			}
			else {
				ola = time;
				olp = pos;
			}
		}

		//cout << time << " : <" << act << "," << pos << "> -- " << bla << " " << blp << " <> " << ola << " " << olp << endl;
		if(i != buttons-1)
			s = s.substr(end+1, s.length());
		//cout << "\t" << act << " ---- " << pos << " |||| " << s <<  "---" << s.length() << endl;
	

	}
	
	return time;
}


int main(int argc, char* argv[]) {

	int res;
	string s = readfile(argv[1]);

	ofstream fout;
	fout.open("output.txt");

	int totalcases = atoi(s.c_str());

	for(int i = 1; i <= totalcases; i++) {
		s = readfile(argv[1]);
		res = m(s);
		fout << "Case #" << i << ": " << res << endl;
	}
	
	fout.close();
	
	return 0;
}
