#include <fstream>
#include <iostream>
#include <list>

using namespace std;

int stringtoint (string input);

int main () {
	// R = times per day roller coaster runs
	// k = capacity of roller coaster
	// N = number of groups
	
	ifstream file ("C.in");
	string line;
	getline (file, line);
	int T = stringtoint (line);
	for (int thing = 0; thing != T; ++thing) {
		getline (file, line);
		size_t space = line.find (" ");
		int R = stringtoint (line.substr (0, space));
		line.erase (0, space + 1);
		space = line.find (" ");
		int k = stringtoint (line.substr (0, space));
		line.erase (0, space + 1);
		space = line.find (" ");
		int N = stringtoint (line.substr (0, space));
		list<int> group;
		getline (file, line);
		for (int n = 0; n != N; ++n) {
			space = line.find (" ");
			group.push_back (stringtoint (line.substr (0, space)));
			line.erase (0, space + 1);
		}
		cout << "Case #" << thing + 1 << ": ";
		int money = 0;
		for (int r = 0; r != R; ++r) {
			int passengers = 0;
			for (int cycle = 0; cycle != N; ++cycle) {
				passengers += group.front();
				group.push_back (group.front());
				group.pop_front();
				if (passengers + group.front() > k)
					break;
			}
			money += passengers;
		}
		cout << money << '\n';
	}
	file.close();

	return 0;
}

int stringtoint (string input) {
	int output = 0;
	for (int counter = 0; counter < input.length(); ++counter) {
		char digit = input.at (counter);				// converts each char to an int
		int value = digit - '0';
		output = output * 10 + value;
	}
	return output;
}
