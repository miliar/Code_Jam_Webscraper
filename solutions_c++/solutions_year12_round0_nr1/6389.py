#include <iostream>

using namespace std;

void main() {
	char mapping[]= "yhesocvxduiglbkrztnwjpfmaq";
	int t;
	cin >> t;
	cin.ignore(numeric_limits<streamsize>::max(),'\n') ;

	char** lines = new char*[t]; 
	for(int i=0; i<t; i++) {
		char* l = new char[100];
		cin.getline(l,101);
		lines[i]=l;
	}
	for(int i=0; i<t; i++) {
		for(int j=0; j<strlen(lines[i]); j++) {
			if(lines[i][j] != ' ') {
				lines[i][j] = mapping[(int)lines[i][j]-97];
			}
		}
		cout<<"Case #"<<i+1<<": "<<lines[i]<<endl;
		delete[] lines[i];
	}
	delete[] lines;
}