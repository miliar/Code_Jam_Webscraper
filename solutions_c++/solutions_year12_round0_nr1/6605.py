#include <iostream>
#include <string>
#include <fstream>
#include <sstream>

using namespace std;

char from[] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
char to  [] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
string sFrom = "";
string sTo[] = "";

int getKey(char later) {
	int count = sizeof(from) / sizeof(char);

	for (int i=0; i<=count; i++) {
		if (from[i] == later) {
			return i;
		}
	}
}

char translate(char a) {
	return to[getKey(a)];
}

string convert(string str_in) {
	for(int i = 0; i < str_in.length(); i++) {
		if(str_in[i]!= ' '){str_in[i] = to[getKey(str_in[i])];}
	}

     return str_in;
}

void doIt() {
	ifstream input("A-small-attempt0.in");
	ofstream output("output.txt");

	int lines;

	input >> lines;

	for (int i=0; i<=lines; i++) {
		char line[256];
		input.getline(line, 256);

		if (i>0) {
			output << "Case #" << (i) << ": " << convert(line) << endl;

			cout << convert(line) << endl;
		}
	}
}

int main() {
	doIt();

	return 0;
}
