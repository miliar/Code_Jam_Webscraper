#include <iostream>
#include <fstream>
#include <string>

using namespace std;

char ChangeLetter(char sub){
    if(sub == 'a') return 'y';
    else if(sub == 'b') return 'h';
    else if(sub == 'c') return 'e';
    else if(sub == 'd') return 's';
    else if(sub == 'e') return 'o';
    else if(sub == 'f') return 'c';
    else if(sub == 'g') return 'v';
    else if(sub == 'h') return 'x';
    else if(sub == 'i') return 'd';
    else if(sub == 'j') return 'u';
    else if(sub == 'k') return 'i';
    else if(sub == 'l') return 'g';
    else if(sub == 'm') return 'l';
    else if(sub == 'n') return 'b';
    else if(sub == 'o') return 'k';
    else if(sub == 'p') return 'r';
    else if(sub == 'q') return 'z';
    else if(sub == 'r') return 't';
    else if(sub == 's') return 'n';
    else if(sub == 't') return 'w';
    else if(sub == 'u') return 'j';
    else if(sub == 'v') return 'p';
    else if(sub == 'w') return 'f';
    else if(sub == 'x') return 'm';
    else if(sub == 'y') return 'a';
    else if(sub == 'z') return 'q';
    else if(sub == ' ') return ' ';
}

int main() {
	ifstream file("A-small-attempt0.in");
	ofstream outfile("Output.in");
	for (int i = 0; file.good(); ++i) {
		cout << "I:" << i << endl;
		string temp;
		getline(file, temp);
		if (i == 0) continue;
		cout << "TEMP:" << temp << endl;
		for (int j = 0; j < temp.length(); ++j) {
			cout << "\tJ:" << j << endl;
			temp[j] = ChangeLetter(temp[j]);
		}
		outfile << "Case #" << i << ": " << temp << endl;
	}
	file.close();
	outfile.close();
	cout << "Done!" << endl;
	cin.get();
	return 0;
}