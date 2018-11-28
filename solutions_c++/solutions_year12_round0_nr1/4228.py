#include <iostream>
#include <fstream>
using namespace std;

char dict[26];
char unused[26];

void CreateDict(){
	int counter = 0;
	for(int i = 0; i < 26; i++){
		dict[i] = ' ';
		unused[i] = 'a' + i;
	}
	fstream coded("Coded.txt", fstream::in);
	fstream uncoded("Uncoded.txt", fstream::in);
	while(coded.good()){
		char A, B;
		coded.get(A);
		uncoded.get(B);
		if(A != ' '){
			int index = A - 'a';
			if(dict[index] == ' '){
				dict[index] = B;
				unused[B - 'a'] = ' ';
				counter++;
			}
		}
	}
	int i = 0, j = 0;
	while(dict[i] != ' ') i++;
	while(unused[j] == ' ') j++;
//	cout << "Unused pair: " << char('a' + i) << " - " << unused[j] << endl;
	dict[i] = unused[j];
//	cout << "Dictionary size: " << counter << endl;
}

void Translate(char *str){
	int i = 0;
	while(str[i] != '\0'){
		if(str[i] != ' ')	str[i] = dict[str[i] - 'a'];
		i++;
	}
}

int main(){
	CreateDict();
	char buffer[256];
	fstream in("in.txt", fstream::in);
	fstream out("out.txt", fstream::out);
	int T; in >> T; in.get();
	for(int t = 0; t < T; t++){
		in.getline(buffer, 256);
//		cout << buffer << endl;
		Translate(buffer);
//		cout << buffer << endl;
		out << "Case #" << t + 1 << ": " << buffer << endl;
	}
	return 0;
}
