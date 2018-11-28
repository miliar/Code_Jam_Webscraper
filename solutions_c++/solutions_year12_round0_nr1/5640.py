#include <iostream>
#include <fstream>
using namespace std;

string evaluate(string word);

int main(){
	
	ofstream fcout("a.sal");
	ifstream fcin("a.in");
	int num;
	
	fcin >> num;
	fcin.ignore();
	string word;
	
	for(int i=1 ; i<=num ; i++){
		getline(fcin,word);
		fcout << "Case #" << i << ": " << evaluate(word) << endl;
	}

}

string evaluate(string word){
	
	string newWord = "";
	
	for(int i=0 ; i<word.length() ; i++){
	
		switch (word[i]){
		
			case 'a':
				newWord += "y";
				break;
			case 'b':
				newWord += "h";
				break;
			case 'c':
				newWord += "e";
				break;
			case 'd':
				newWord += "s";
				break;
			case 'e':
				newWord += "o";
				break;
			case 'f':
				newWord += "c";
				break;
			case 'g':
				newWord += "v";
				break;
			case 'h':
				newWord += "x";
				break;
			case 'i':
				newWord += "d";
				break;
			case 'j':
				newWord += "u";
				break;
			case 'k':
				newWord += "i";
				break;
			case 'l':
				newWord += "g";
				break;
			case 'm':
				newWord += "l";
				break;
			case 'n':
				newWord += "b";
				break;
			case 'o':
				newWord += "k";
				break;
			case 'p':
				newWord += "r";
				break;
			case 'q':
				newWord += "z";
				break;
			case 'r':
				newWord += "t";
				break;
			case 's':
				newWord += "n";
				break;
			case 't':
				newWord += "w";
				break;
			case 'u':
				newWord += "j";
				break;
			case 'v':
				newWord += "p";
				break;
			case 'w':
				newWord += "f";
				break;
			case 'x':
				newWord += "m";
				break;
			case 'y':
				newWord += "a";
				break;
			case 'z':
				newWord += "q";
				break;
			case ' ':
				newWord += ' ';
		}
	}
	
	return newWord;
}