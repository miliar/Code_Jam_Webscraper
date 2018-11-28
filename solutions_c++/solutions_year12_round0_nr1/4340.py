#include <iostream>
#include <fstream>
#include <string>

using namespace std;

char g2e(char);

int main() {
	ifstream in("A-small-attempt0.in");
	ofstream out("output.txt");
	string in_line, out_line;
	int T;
	
	in >> T;
	getline(in, in_line);
	for (int i = 0; i < T; i++) {
		out << "Case #" << (i+1) << ": "; 
		getline(in, in_line);
		out_line.clear();
		for(unsigned int j = 0; j < in_line.length(); j++) {
			out_line += g2e(in_line[j]);
		}
		out << (out_line + '\n');
	}
	in.close();
	out.close();
}

char g2e(char a) {
	switch (a){
		case 'a': return 'y';
		case 'b': return 'h';
		case 'c': return 'e';
		case 'd': return 's';
		case 'e': return 'o';
		case 'f': return 'c';
		case 'g': return 'v';
		case 'h': return 'x';
		case 'i': return 'd';
		case 'j': return 'u';
		case 'k': return 'i';
		case 'l': return 'g';
		case 'm': return 'l';
		case 'n': return 'b';
		case 'o': return 'k';
		case 'p': return 'r';
		case 'q': return 'z';
		case 'r': return 't';
		case 's': return 'n';
		case 't': return 'w';
		case 'u': return 'j';
		case 'v': return 'p';
		case 'w': return 'f';
		case 'x': return 'm';
		case 'y': return 'a';
		case 'z': return 'q';
		case ' ': return ' ';
		default: return '\n';
	}
	return ' ';
}
