#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;

char a[] = "abcdefghijklmnopqrstuvwxyz";
char b[] = "yhesocvxduiglbkrztnwjpfmaq";

int main () {
	char s[101];
	int T;
	ofstream myoutfile;
	ifstream myinfile;
	myoutfile.open ("ki.txt");
	myinfile.open("be.txt");

	myinfile >> T;
	int i = 1;
	myinfile.getline(s, 1);
	while (i<=T) {
		myinfile.getline(s, 101);
		for(int j = 0; j < strlen(s); j++)
			if(s[j]!=' ')
				s[j] = b[s[j] - 97];
		myoutfile << "Case #" << i << ": " << s << '\n';
		i++;
	}
	myoutfile.close();
	myinfile.close();
	return 0;
}