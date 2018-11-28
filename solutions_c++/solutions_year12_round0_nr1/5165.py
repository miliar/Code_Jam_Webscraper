#include <iostream>
#include <string.h>
#include <string>
using namespace std;

string decode(string line){
	string buffer;
//	cout << line.size() << endl;
	for (int i = 0 ; i < line.size();i++){
		switch(line[i]){
		case 'a':
				buffer.push_back('y');
				break;
		case 'b':
				buffer.push_back('h');

				break;
		case 'c':
			buffer.push_back('e');
			break;
		case 'd':
			buffer.push_back('s');
			break;
		case 'e':
			buffer.push_back('o');
			break;
		case 'f':
			buffer.push_back('c');
			break;
		case 'g':
			buffer.push_back('v');
			break;
		case 'h':
			buffer.push_back('x');
			break;
		case 'i':
			buffer.push_back('d');
			break;
		case 'j':
			buffer.push_back('u');
			break;
		case 'k':
			buffer.push_back('i');
			break;
		case 'l':
			buffer.push_back('g');
			break;
		case 'm':
			buffer.push_back('l');
			break;
		case 'n':
			buffer.push_back('b');
			break;
		case 'o':
			buffer.push_back('k');
			break;
		case 'p':
			buffer.push_back('r');
			break;
		case 'q':
			buffer.push_back('z');
			break;
		case 'r':
			buffer.push_back('t');
			break;
		case 's':
			buffer.push_back('n');
			break;
		case 't':
			buffer.push_back('w');
			break;
		case 'u':
			buffer.push_back('j');
			break;
		case 'v':
			buffer.push_back('p');
			break;
		case 'w':
			buffer.push_back('f');
			break;
		case 'x':
			buffer.push_back('m');
			break;
		case 'y':
			buffer.push_back('a');
			break;
		case 'z':
			buffer.push_back('q');
			break;
		default:
			buffer.push_back(' ');
			break;
		}
	}


	return buffer;
}




int main(){
	int inputs;
	string line;
	string output;
	cin >> inputs;
	getline(cin,line);
	for(int round = 0; round < inputs; round++){
		//read in the entire line
		getline(cin,line); //have our data
		output = decode(line);

		cout << "Case #"<< round+ 1 << ": " << output << endl;
	}




}
