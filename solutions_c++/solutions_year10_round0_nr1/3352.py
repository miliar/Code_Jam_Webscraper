#include <fstream>
#include <iostream>

using namespace std;

int stringtoint (string input);
void switches (int N, int K);
int stringtoint (string input);

int main () {
	// N = number of snappers
	// K = times snapped
	// 0 == off
	// 1 == on
	
	ifstream file ("A-large.in");
	string output1;
	string output2;
	string line;
	getline (file, line);
	int T = stringtoint (line);
	for (int thing = 0; thing != T; ++thing) {
		getline (file, line);
		size_t space = line.find (" ");
		int N = stringtoint (line.substr (0, space));
		int K = stringtoint (line.substr (space + 1));
		cout << "Case #" << thing + 1 << ": ";
		switches (N, K);
	}
	file.close();

	return 0;
}

void switches (int N, int K) {
	if (K % (1 << N) == (1 << N) - 1)
		cout << "ON\n";
	else
		cout << "OFF\n";
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
