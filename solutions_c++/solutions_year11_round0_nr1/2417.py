#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <list>

using namespace std;
int main (int argc, char * const argv[]) {
    
	ifstream input(argv[1], ifstream::in);
	
	int testsNb;
	string s;
	getline(input, s);
	istringstream stream(s);
	stream >> testsNb;
	
	ofstream outfile(argv[2]);
	
	cout << "Testing " << testsNb << " cases..." << endl;
	
	int cases = 0;
	while (input.good() && getline(input, s) && !input.eof()) {
		// Get necessary information from first line
		char *tmp = strdup(s.c_str());
		char *token = strtok(tmp, " ");
		list<int> values, orange, blue;
		list<string> sequence;
		int count = 1, buttons = 0;
		while (token != NULL) {
			if (count == 1)
				buttons = atoi(token);
			else if (!strcmp(token, "O")) {
				sequence.push_back("orange");
				token = strtok(NULL, " ");
				orange.push_back(atoi(token));
			}
			else {
				sequence.push_back("blue");
				token = strtok(NULL, " ");
				blue.push_back(atoi(token));
			}
			token = strtok(NULL, " ");
			count++;
		}	
		free(tmp);
		cases++;
		int o = 1, b = 1;
		int time = 0;
		for (time = 0; buttons > 0 ; time++) {
			bool pushed = false;
			// Actions orange
			if (abs(orange.front() - o) != 0)
				o = orange.front() - o > 0 ? o + 1 : o - 1;
			else if (sequence.front() == "orange") {
				// push button
				orange.pop_front();
				buttons--;
				pushed = true;
			}
			// Actions blue
			if (abs(blue.front() - b) != 0)
				b = blue.front() - b > 0 ? b + 1 : b - 1;
			else if (sequence.front() == "blue") {
				// push button
				blue.pop_front();
				buttons--;
				pushed = true;
			}
			if (pushed)
				sequence.pop_front();
		}
		cout << "Time is " << time << endl; 
		outfile << "Case #" << cases << ": " << time << endl; 
		
	}	
	
	input.close();
	outfile.close();
    return 0;
	
}


/*ifstream input(argv[1], ifstream::in);

int testsNb;
string s;
getline(input, s);
istringstream stream(s);
stream >> testsNb;

ofstream outfile(argv[2]);

cout << "Testing " << testsNb << " cases..." << endl;

int cases = 0;
while (input.good() && getline(input, s) && !input.eof()) {
	// Get necessary information from first line
	char *tmp = strdup(s.c_str());
	char *token = strtok(tmp, " ");
	vector<int> values;
	while (token != NULL) {
		values.push_back(atoi(token));
		token = strtok(NULL, " ");
	}	
	free(tmp);
	cases++;
	for (int i = 0; i < values.size(); i++) {
		cout << values[i] << " ";
	}
	cout << endl;
	//outfile << "Case #" << cases << ": " << money << endl; 
	
}	

input.close();
outfile.close();
return 0;*/
