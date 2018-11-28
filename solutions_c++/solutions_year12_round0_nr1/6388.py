#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

vector<string> translate(vector<string> t);
void readfile(string filename);
void writefile(vector<string> text);

vector<string> res;

int main() {
	string filename;
	cout<<"Input filename:"<<endl;
	getline(cin,filename);
	readfile(filename);

	char a;
	cin>>a;
	return 0;
}

void readfile(string filename) {
	ifstream file;
	file.open("input.txt");
	string line;
	vector<string> msg;
	getline(file, line);
	int t = atoi(line.c_str());
	for(int i=0; i<t; i++) {
		getline(file, line);
		msg.push_back(line);
	}
	vector<string> res = translate(msg);
	writefile(res);
	file.close();
}

void writefile(vector<string> text) {
	ofstream file;
	file.open("output.txt");
	if (file) {
		for(int i=0; i<text.size(); i++) {
			file<<"Case #"<<i+1<<": "<<text[i]<<endl;
		}
	}
	cout<<"My work here is done"<<endl;
	file.close();
}

vector<string> translate(vector <string> t) {
	vector <string> v;
	for (int i=0; i<t.size(); i++) {
		string line = t[i];
		for(int l=0; l<line.length();l++) {
			switch (line[l]) {
			case 'y':
			case 'Y':
				line[l] = 'a';
				break;
			case 'n':
			case 'N':
				line[l] = 'b';
				break;
			case 'f':
			case 'F':
				line[l] = 'c';
				break;
			case 'i':
			case 'I':
				line[l] = 'd';
				break;
			case 'c':
			case 'C':
				line[l] = 'e';
				break;
			case 'w':
			case 'W':
				line[l] = 'f';
				break;
			case 'l':
			case 'L':
				line[l] = 'g';
				break;
			case 'b':
			case 'B':
				line[l] = 'h';
				break;
			case 'k':
			case 'K':
				line[l] = 'i';
				break;
			case 'u':
			case 'U':
				line[l] = 'j';
				break;
			case 'o':
			case 'O':
				line[l] = 'k';
				break;
			case 'm':
			case 'M':
				line[l] = 'l';
				break;
			case 'x':
			case 'X':
				line[l] = 'm';
				break;
			case 's':
			case 'S':
				line[l] = 'n';
				break;
			case 'e':
			case 'E':
				line[l] = 'o';
				break;
			case 'v':
			case 'V':
				line[l] = 'p';
				break;
			case 'z':
			case 'Z':
				line[l] = 'q';
				break;
			case 'p':
			case 'P':
				line[l] = 'r';
				break;
			case 'd':
			case 'D':
				line[l] = 's';
				break;
			case 'r':
			case 'R':
				line[l] = 't';
				break;
			case 'j':
			case 'J':
				line[l] = 'u';
				break;
			case 'g':
			case 'G':
				line[l] = 'v';
				break;
			case 't':
			case 'T':
				line[l] = 'w';
				break;
			case 'h':
			case 'H':
				line[l] = 'x';
				break;
			case 'a':
			case 'A':
				line[l] = 'y';
				break;
			case 'q':
			case 'Q':
				line[l] = 'z';
				break;
			default: break;
			}
		}
		v.push_back(line);
	}
	return v;
}