#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <fstream>

using namespace std;

char a[26];
char b[26];

char mapper(char x){
	if (x == '\n') return '\n';
	int i;
	for(i = 0; i < 26; i++) {
			if(x == (char)b[i]) return a[i];
	}
	return ' ';
}
int main(int argc, char** argv){

		a[0] = 'a';
		a[1] = 'b';
		a[2] = 'c';
		a[3] = 'd';
		a[4] = 'e';
		a[5] = 'f';
		a[6] = 'g';
		a[7] = 'h';
		a[8] = 'i';
		a[9] = 'j';
		a[10] = 'k';
		a[11] = 'l';
		a[12] = 'm';
		a[13] = 'n';
		a[14] = 'o';
		a[15] = 'p';
		a[16] = 'q';
		a[17] = 'r';
		a[18] = 's';
		a[19] = 't';
		a[20] = 'u';
		a[21] = 'v';
		a[22] = 'w';
		a[23] = 'x';
		a[24] = 'y';
		a[25] = 'z';
		
		b[0] = 'y';//
		b[1] = 'n';//
		b[2] = 'f';//
		b[3] = 'i';//
		b[4] = 'c';//
		b[5] = 'w';//
		b[6] = 'l';//
		b[7] = 'b';//
		b[8] = 'k';//
		b[9] = 'u';//
		b[10] = 'o';//
		b[11] = 'm';//
		b[12] = 'x';//
		b[13] = 's';//
		b[14] = 'e';//
		b[15] = 'v';//
		b[16] = 'z';
		b[17] = 'p';//
		b[18] = 'd';//
		b[19] = 'r';//
		b[20] = 'j';//
		b[21] = 'g';//
		b[22] = 't';//
		b[23] = 'h';//
		b[24] = 'a';//
		b[25] = 'q';//
		
		string s;
		ifstream file;
		ofstream out;

		file.open (argv[1]);
        out.open (argv[2]);

	    getline(file,s); 
		int n = atoi(s.c_str());

		for(int i = 0; i < n; i ++){
			getline(file,s); 
			out << "Case #" << i + 1 << ": ";
			for(unsigned int j = 0; j < strlen(s.c_str()); j ++){
				out <<  mapper(s.c_str()[j]);
			}
			out << endl;
		}
}
