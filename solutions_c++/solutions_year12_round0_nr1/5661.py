#include <iostream>
#include <sstream>
#include <string>
#include <map>
#include <iomanip>
using namespace std;

std::map<char, char> translationTable;
void loadOne( std::string from , std::string to){
	for(unsigned int i=0; i < from.length();i++){
		translationTable[from.at(i)]=to.at(i);
	}
}
void LoadMap(){

	loadOne("abcdefghijklmnopqrstuvwxyz ", "abcdefghijklmnopqrstuvwxyz ");
	loadOne("yeqz ", "aozq ");
	loadOne("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand");
	loadOne("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities");
	loadOne("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up");
	
}
void Decode( std::string input, const int &test){
	for(unsigned int i=0; i < input.length();i++){
		input.at(i) = translationTable[input.at(i)];
	}

	cout<< "Case #"<< test << ": " << input  << endl;
}

int main( char * arg, int argc){
	LoadMap();
	int tests;
	cin >> tests;
	
	string line;
	getline(cin, line);
	for( int i = 1 ; i <= tests ; i++ ){
		getline(cin, line);
		Decode(line, i);
	}
	return 0;
}