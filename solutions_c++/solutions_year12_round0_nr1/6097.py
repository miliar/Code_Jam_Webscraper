#include <iostream>
#include <cstdlib>
#include <cstring>
#include <fstream>

using namespace std;

void main()
{
	ifstream inStream;
	int testCases;

	inStream.open("A-small-attempt5.in");
	if(inStream.fail()){
		exit(1);
	}
	ofstream SaveFile("answer.txt");
	inStream>>testCases;
	testCases++;
	char **string = new char*[testCases];
	for(int i=0;i<testCases;i++){
		string[i] = new char[101];
	}
	for(int j=0;j<testCases;j++){
		inStream.getline(string[j],101);
	}
	for(int j=0;j<testCases;j++){
		int length = strlen(string[j]);
		for(int i=0;i<length;i++){
			if( string[j][i] == ' ') continue;
			else if( string[j][i] == 'a') string[j][i] = 'y';
			else if( string[j][i] == 'b') string[j][i] = 'h';
			else if( string[j][i] == 'c') string[j][i] = 'e';
			else if( string[j][i] == 'd') string[j][i] = 's';
			else if( string[j][i] == 'e') string[j][i] = 'o';
			else if( string[j][i] == 'f') string[j][i] = 'c';
			else if( string[j][i] == 'g') string[j][i] = 'v';
			else if( string[j][i] == 'h') string[j][i] = 'x';
			else if( string[j][i] == 'i') string[j][i] = 'd';
			else if( string[j][i] == 'j') string[j][i] = 'u';
			else if( string[j][i] == 'k') string[j][i] = 'i';
			else if( string[j][i] == 'l') string[j][i] = 'g';
			else if( string[j][i] == 'm') string[j][i] = 'l';
			else if( string[j][i] == 'n') string[j][i] = 'b';
			else if( string[j][i] == 'o') string[j][i] = 'k';
			else if( string[j][i] == 'p') string[j][i] = 'r';
			else if( string[j][i] == 'q') string[j][i] = 'z';
			else if( string[j][i] == 'r') string[j][i] = 't';
			else if( string[j][i] == 's') string[j][i] = 'n';
			else if( string[j][i] == 't') string[j][i] = 'w';
			else if( string[j][i] == 'u') string[j][i] = 'j';
			else if( string[j][i] == 'v') string[j][i] = 'p';
			else if( string[j][i] == 'w') string[j][i] = 'f';
			else if( string[j][i] == 'x') string[j][i] = 'm';
			else if( string[j][i] == 'y') string[j][i] = 'a';
			else if( string[j][i] == 'z') string[j][i] = 'q';
		}
	}
	for(int i=1;i<testCases;i++){
		SaveFile<<"Case #"<<i<<": "<<string[i]<<endl;
	}

	for(int i=0;i<testCases;i++){
		delete []string[i];
	}
	delete []string;
	inStream.close();
	SaveFile.close();
}