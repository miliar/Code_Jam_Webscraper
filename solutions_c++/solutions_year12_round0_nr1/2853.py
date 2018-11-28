#include<iostream>
#include<queue>
#include<string>
#include<fstream>

using namespace std;

void Googlerese(string &text);

int main() {
	ifstream inFile("A-small-attempt1.in");
	ofstream outFile("A-small-out.out");
	int T;
	inFile >> T;
	//cin.ignore();
	string temp;
	getline(inFile, temp);
	for(int i=0; i<T; i++) {
		//inFile >> temp;
		getline(inFile, temp);
		Googlerese(temp);
		
		outFile << "Case #" << i+1 << ": "<< temp << endl;
	}

	inFile.close();
	outFile.close();
	return 0;
}


void Googlerese(string &text) {
	for(int i=0; i<text.size(); i++) {
		switch(text[i]) {
		case 'a': text[i] = 'y'; break;
		case 'b': text[i] = 'h'; break;
		case 'c': text[i] = 'e'; break;
		case 'd': text[i] = 's'; break;
		case 'e': text[i] = 'o'; break;
		case 'f': text[i] = 'c'; break;
		case 'g': text[i] = 'v'; break;
		case 'h': text[i] = 'x'; break;
		case 'i': text[i] = 'd'; break;
		case 'j': text[i] = 'u'; break;
		case 'k': text[i] = 'i'; break;
		case 'l': text[i] = 'g'; break;
		case 'm': text[i] = 'l'; break;
		case 'n': text[i] = 'b'; break;
		case 'o': text[i] = 'k'; break;
		case 'p': text[i] = 'r'; break;
		case 'q': text[i] = 'z'; break;
		case 'r': text[i] = 't'; break;
		case 's': text[i] = 'n'; break;
		case 't': text[i] = 'w'; break;
		case 'u': text[i] = 'j'; break;
		case 'v': text[i] = 'p'; break;
		case 'w': text[i] = 'f'; break;
		case 'x': text[i] = 'm'; break;
		case 'y': text[i] = 'a'; break;
		case 'z': text[i] = 'q'; break;
		}
	}
}