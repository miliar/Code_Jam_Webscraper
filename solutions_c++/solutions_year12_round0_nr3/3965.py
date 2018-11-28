#include <cstdlib>
#include <string>
#include <sstream>
#include <iostream>
#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <deque>
#include <set>
#include <algorithm>


using namespace std;


vector<string> number_list;

set<pair<string, string> > recycled_list;

int input_min = 0;
int input_max = 0;

void addToRecycled(const std::string& number, const std::string& shifted) {

	int number_as_int = atoi(number.c_str());
	int shifted_as_int = atoi(shifted.c_str());

	if (shifted_as_int >= input_min &&
	    shifted_as_int <= input_max &&
	    shifted_as_int > number_as_int) { 
		recycled_list.insert(pair<string, string>(number, shifted));
		//cerr << "    - shifted: " << shifted;
		//cerr << "      - pair: (" << number << ", " << shifted << ")" << endl;
	}
}

string shift(const std::string& input, int n) {
	//cerr << "                -> shifting <" << input << "> " << n << " positions: ";

	int shift_position = input.size() - n;
	string shifted = input.substr(shift_position, input.size()) +
		input.substr(0, shift_position);

	//cerr << "<" << shifted << ">" << endl;
	return shifted;
}


int main() {
	string basename = "C-large.";
	ifstream input_file(string(basename + "in").c_str());
	ofstream output_file(string(basename + "out").c_str());

	string line;
	string line_out;

	if (input_file.is_open()) {
		getline(input_file, line); // consume first line
		int numlines = atoi(line.c_str());

		int counter = 0;
		while (input_file.good() && (counter < numlines)) {

			number_list.clear();
			recycled_list.clear();

			getline(input_file, line);
			size_t pos = line.find_first_of(' ');
			input_min = atoi(line.substr(0, pos).c_str());
			input_max = atoi(line.substr(pos, line.size()).c_str());
			//cerr << " < min: " << input_min << endl;
			//cerr << " < max: " << input_max << endl;


			for (int i = input_min; i <= input_max; ++i) {
				int n = i;
				string number;
				while (n > 0) {
					number.insert(number.begin(), (n % 10) + '0');
					n /= 10;
				}
				number_list.push_back(number);

				//cerr << "    - number: " << number << endl;
			}


			for (int i = 0; i < number_list.size(); ++i) {
				string number = number_list[i];
				string shifted = number_list[i];

				for (int i = 1; i < number.size(); ++i) {
					addToRecycled(number, shift(number, i));
				}
			}


			output_file << "Case #" << ++counter << ": " << recycled_list.size() << endl;
			cout << "Case #" << counter << ": " << recycled_list.size() << endl;
		}
		input_file.close();
		output_file.close();
	} else {
		cerr << "ERROR: Unable to open file" << endl;
	}

	return 0;
}
