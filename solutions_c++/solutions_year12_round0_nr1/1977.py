#include <fstream>
#include <iostream>
#include <string>

using namespace std;

char dict[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main(int argc, char ** argv) {
	ifstream input(argv[1]);
	ofstream out("output.out");
	int noIn;
	string s;

	input >> noIn;
	getline(input, s);
	
	cout << "PROCESSING " << noIn << " LINES" << endl;
	for(int i = 1; i <= noIn; i++) {
		out << "Case #" << i << ": ";
		getline(input, s);
		for(int i = 0; i < s.length(); i++)
			if(s[i] != ' ') s[i] = dict[s[i]-'a'];
		cout << s << endl;
		out << s << endl;
	}	
}
