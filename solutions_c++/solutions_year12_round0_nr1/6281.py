#include <iostream>
#include <cstring>
#include <fstream>

using namespace std;

char dictionary[26][2];

char translate(char ch) {
	for (int i=0; i<26; i++) {
		if (dictionary[i][1] == ch) 
			return dictionary[i][0];
	}
}

int main() {

	//initialize translator.
	dictionary[0][0] = 'a';dictionary[0][1] = 'y';
	dictionary[1][0] = 'b';dictionary[1][1] = 'n';
	dictionary[2][0] = 'c';dictionary[2][1] = 'f';
	dictionary[3][0] = 'd';dictionary[3][1] = 'i';
	dictionary[4][0] = 'e';dictionary[4][1] = 'c';
	dictionary[5][0] = 'f';dictionary[5][1] = 'w';
	dictionary[6][0] = 'g';dictionary[6][1] = 'l';
	dictionary[7][0] = 'h';dictionary[7][1] = 'b';
	dictionary[8][0] = 'i';dictionary[8][1] = 'k';
	dictionary[9][0] = 'j';dictionary[9][1] = 'u';
	dictionary[10][0] = 'k';dictionary[10][1] = 'o';
	dictionary[11][0] = 'l';dictionary[11][1] = 'm';
	dictionary[12][0] = 'm';dictionary[12][1] = 'x';
	dictionary[13][0] = 'n';dictionary[13][1] = 's';
	dictionary[14][0] = 'o';dictionary[14][1] = 'e';
	dictionary[15][0] = 'p';dictionary[15][1] = 'v';
	dictionary[16][0] = 'q';dictionary[16][1] = 'z';
	dictionary[17][0] = 'r';dictionary[17][1] = 'p';
	dictionary[18][0] = 's';dictionary[18][1] = 'd';
	dictionary[19][0] = 't';dictionary[19][1] = 'r';
	dictionary[20][0] = 'u';dictionary[20][1] = 'j';
	dictionary[21][0] = 'v';dictionary[21][1] = 'g';
	dictionary[22][0] = 'w';dictionary[22][1] = 't';
	dictionary[23][0] = 'x';dictionary[23][1] = 'h';
	dictionary[24][0] = 'y';dictionary[24][1] = 'a';
	dictionary[25][0] = 'z';dictionary[25][1] = 'q';
	
	int n, i = 0;
	ifstream file("A-small-attempt5.in");
	ofstream fileout("x.out");
	string str;
	getline (file, str);
	while(i < 30) {
		getline (file, str);
		
		int len = str.length();
		for (int j=0; j<len; j++) {
			if(str[j] == ' ') {}
			else str[j] = translate(str[j]);
		}
		if (i != 0) fileout<<endl;
		fileout<< "Case #"<<i+1<<": "<<str;
		i++;		
	}
	return -1;
}
