#include <string>
#include <vector>
#include <iostream>
#include <fstream>
using namespace std;

string map(string entered){
	string translating = "";
	char translated;	
	for(int i = 0; i < entered.size(); i++){
		if(entered[i] == 'a') translated = 'y';
		else if(entered[i] == 'b') translated = 'h';
		else if(entered[i] == 'c') translated = 'e';
		else if(entered[i] == 'd') translated = 's';
		else if(entered[i] == 'e') translated = 'o';
		else if(entered[i] == 'f') translated = 'c';
		else if(entered[i] == 'g') translated = 'v';
		else if(entered[i] == 'h') translated = 'x';
		else if(entered[i] == 'i') translated = 'd';
		else if(entered[i] == 'j') translated = 'u';
		else if(entered[i] == 'k') translated = 'i';
		else if(entered[i] == 'l') translated = 'g';
		else if(entered[i] == 'm') translated = 'l';
		else if(entered[i] == 'n') translated = 'b';
		else if(entered[i] == 'o') translated = 'k';
		else if(entered[i] == 'p') translated = 'r';
		else if(entered[i] == 'q') translated = 'z';
		else if(entered[i] == 'r') translated = 't';
		else if(entered[i] == 's') translated = 'n';
		else if(entered[i] == 't') translated = 'w';
		else if(entered[i] == 'u') translated = 'j';
		else if(entered[i] == 'v') translated = 'p';
		else if(entered[i] == 'w') translated = 'f';
		else if(entered[i] == 'x') translated = 'm';
		else if(entered[i] == 'y') translated = 'a';
		else if(entered[i] == 'z') translated = 'q';
		else translated = entered[i];
		
		translating += translated;		
	}  
	return translating;
}

int main(){
  	vector <string> hold, translated;
  	int i;
	string entered;
	ifstream ifs("A-small-attempt1.in");
	while( getline( ifs, entered ) ){
     		hold.push_back(map(entered));
	}
	for (i = 1; i < hold.size(); i++){ 
		ofstream outputFile;
		outputFile.open("A-small-attempt1.out", ios::app);
		outputFile << "Case #" << i << ": " << hold[i] << endl;	
		outputFile.close();
        }
	
	return 0;
}


