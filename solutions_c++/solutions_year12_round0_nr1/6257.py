#include <iostream>;
#include <windows.h>;
#include <fstream>;
#include <string>;
#include <sstream>;
#include <istream>;
#include <vector>;

using namespace std;

vector<string> lines;

string Convertlanguage (string original);

int main() {
	string line;
	int N = -1;
	int casenr = 1;

	ifstream myfile;
	myfile.open("A-small-attempt0.in");

	ofstream outfile;
	outfile.open("output.txt");

	if (myfile.is_open()){
		while (getline (myfile, line)){
			if (N == -1){
				N = atoi(line.c_str());
			}
			else {
				outfile << "Case #" << casenr << ": " << Convertlanguage(line) << "\n";

				casenr ++;
			}
		}
	}
	else {
		cout << "Failed to open file";
	}

	outfile.close();
	myfile.close();

	Sleep(100000);
}

string Convertlanguage (string original){
	int size = original.size();
	string copy = original;

	for (int ii = 0; ii < size; ii++){
		if (copy[ii] == 'a'){
			copy[ii] = 'y';
		}
		else if (copy[ii] == 'o'){
			copy[ii] = 'k';
		}
		else if (copy[ii] == 'q'){
			copy[ii] = 'z';
		}
		else if (copy[ii] == 'b'){
			copy[ii] = 'h';
		}
		else if (copy[ii] == 'c'){
			copy[ii] = 'e';
		}
		else if (copy[ii] == 'd'){
			copy[ii] = 's';
		}
		else if (copy[ii] == 'e'){
			copy[ii] = 'o';
		}
		else if (copy[ii] == 'f'){
			copy[ii] = 'c';
		}
		else if (copy[ii] == 'g'){
			copy[ii] = 'v';
		}
		else if (copy[ii] == 'h'){
			copy[ii] = 'x';
		}
		else if (copy[ii] == 'i'){
			copy[ii] = 'd';
		}
		else if (copy[ii] == 'j'){
			copy[ii] = 'u';
		}
		else if (copy[ii] == 'k'){
			copy[ii] = 'i';
		}
		else if (copy[ii] == 'l'){
			copy[ii] = 'g';
		}
		else if (copy[ii] == 'm'){
			copy[ii] = 'l';
		}
		else if (copy[ii] == 'n'){
			copy[ii] = 'b';
		}
		else if (copy[ii] == 'p'){
			copy[ii] = 'r';
		}
		else if (copy[ii] == 'z'){
			copy[ii] = 'q';
		}
		else if (copy[ii] == 'r'){
			copy[ii] = 't';
		}
		else if (copy[ii] == 's'){
			copy[ii] = 'n';
		}
		else if (copy[ii] == 't'){
			copy[ii] = 'w';
		}
		else if (copy[ii] == 'u'){
			copy[ii] = 'j';
		}
		else if (copy[ii] == 'v'){
			copy[ii] = 'p';
		}
		else if (copy[ii] == 'w'){
			copy[ii] = 'f';
		}
		else if (copy[ii] == 'x'){
			copy[ii] = 'm';
		}
		else if (copy[ii] == 'y'){
			copy[ii] = 'a';
		}
	}

	return copy;
}