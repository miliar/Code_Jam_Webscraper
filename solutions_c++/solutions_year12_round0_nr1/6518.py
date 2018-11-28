#include <iostream>
#include <string>
using namespace std;

char map[26];

int main() {

	map[4] = 'o' ; 
	map[9] = 'u' ; 
	map[15] = 'r' ; 
	map[12] = 'l' ; 
	map[24] = 'a' ; 
	map[18] = 'n' ; 
	map[11] = 'g' ; 
	map[9] = 'u' ; 
	map[24] = 'a' ; 
	map[11] = 'g' ; 
	map[2] = 'e' ; 
	map[10] = 'i' ; 
	map[3] = 's' ; 
	map[10] = 'i' ; 
	map[23] = 'm' ; 
	map[21] = 'p' ; 
	map[4] = 'o' ; 
	map[3] = 's' ; 
	map[3] = 's' ; 
	map[10] = 'i' ; 
	map[13] = 'b' ; 
	map[12] = 'l' ; 
	map[2] = 'e' ; 
	map[17] = 't' ; 
	map[4] = 'o' ; 
	map[9] = 'u' ; 
	map[18] = 'n' ; 
	map[8] = 'd' ; 
	map[2] = 'e' ; 
	map[15] = 'r' ; 
	map[3] = 's' ; 
	map[17] = 't' ; 
	map[24] = 'a' ; 
	map[18] = 'n' ; 
	map[8] = 'd' ; 
	map[17] = 't' ; 
	map[1] = 'h' ; 
	map[2] = 'e' ; 
	map[15] = 'r' ; 
	map[2] = 'e' ; 
	map[24] = 'a' ; 
	map[15] = 'r' ; 
	map[2] = 'e' ; 
	map[17] = 't' ; 
	map[19] = 'w' ; 
	map[2] = 'e' ; 
	map[18] = 'n' ; 
	map[17] = 't' ; 
	map[0] = 'y' ; 
	map[3] = 's' ; 
	map[10] = 'i' ; 
	map[7] = 'x' ; 
	map[22] = 'f' ; 
	map[24] = 'a' ; 
	map[5] = 'c' ; 
	map[17] = 't' ; 
	map[4] = 'o' ; 
	map[15] = 'r' ; 
	map[10] = 'i' ; 
	map[24] = 'a' ; 
	map[12] = 'l' ; 
	map[21] = 'p' ; 
	map[4] = 'o' ; 
	map[3] = 's' ; 
	map[3] = 's' ; 
	map[10] = 'i' ; 
	map[13] = 'b' ; 
	map[10] = 'i' ; 
	map[12] = 'l' ; 
	map[10] = 'i' ; 
	map[17] = 't' ; 
	map[10] = 'i' ; 
	map[2] = 'e' ; 
	map[3] = 's' ; 
	map[3] = 's' ; 
	map[4] = 'o' ; 
	map[10] = 'i' ; 
	map[17] = 't' ; 
	map[10] = 'i' ; 
	map[3] = 's' ; 
	map[4] = 'o' ; 
	map[14] = 'k' ; 
	map[24] = 'a' ; 
	map[0] = 'y' ; 
	map[10] = 'i' ; 
	map[22] = 'f' ; 
	map[0] = 'y' ; 
	map[4] = 'o' ; 
	map[9] = 'u' ; 
	map[19] = 'w' ; 
	map[24] = 'a' ; 
	map[18] = 'n' ; 
	map[17] = 't' ; 
	map[17] = 't' ; 
	map[4] = 'o' ; 
	map[20] = 'j' ; 
	map[9] = 'u' ; 
	map[3] = 's' ; 
	map[17] = 't' ; 
	map[11] = 'g' ; 
	map[10] = 'i' ; 
	map[6] = 'v' ; 
	map[2] = 'e' ; 
	map[9] = 'u' ; 
	map[21] = 'p' ; 
	map[25] = 'q';
	map[16] = 'z';
	
	for (int i=0; i<26; i++) {
		//cout << (char)(i+'a') << " " << map[i] << endl;
	}

	int T;
	cin >> T;
	cin.ignore();
	for (int j=0; j<T; j++) {
		string input = "";
		getline (cin,input);
		cout << "Case #"<<(j+1) << ": ";
		//cout << input;
		for (int i=0; i<input.length(); i++) {
			if (input[i] != ' ') cout << map[input[i]-'a'];
			else cout << " ";
		}
		cout << endl;
	}

	return 0;
}

/*
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv


Output
Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up
*/

