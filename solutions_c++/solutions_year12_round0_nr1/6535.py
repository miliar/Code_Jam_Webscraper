#include <string>
#include <iostream>

using namespace std;

char translation[] = "yhesocvxduiglbkrztnwjpfmaq";

int main(void) {
	int tests;
	cin >> tests;
	string emptyline;
	getline(cin, emptyline);
	for(int test = 0; test<tests; ++test) {
		string line;
		getline(cin, line);
		for(int i=0; i<line.length(); ++i)
			if(isalpha(line[i]))
				line[i] = translation[line[i]-'a'];
		cout << "Case #" << test+1 << ": " << line << endl;
	}
}