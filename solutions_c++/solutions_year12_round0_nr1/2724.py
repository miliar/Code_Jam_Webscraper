#include<iostream>
#include<string>
#include<fstream>

using namespace std;

char answer(char a){
	
	if(a == 'a')return 'y';
	if(a == 'b')return 'h';
	if(a == 'c')return 'e';
	if(a == 'd')return 's';
	if(a == 'e')return 'o';
	if(a == 'f')return 'c';
	if(a == 'g')return 'v';
	if(a == 'h')return 'x';
	if(a == 'i')return 'd';
	if(a == 'j')return 'u';
	if(a == 'k')return 'i';
	if(a == 'l')return 'g';
	if(a == 'm')return 'l';
	if(a == 'n')return 'b';
	if(a == 'o')return 'k';
	if(a == 'p')return 'r';
	if(a == 'q')return 'z';
	if(a == 'r')return 't';
	if(a == 's')return 'n';
	if(a == 't')return 'w';
	if(a == 'u')return 'j';
	if(a == 'v')return 'p';
	if(a == 'w')return 'f';
	if(a == 'x')return 'm';
	if(a == 'y')return 'a';
	if(a == 'z')return 'q';	
	else	return a;
}

int main(){

	ifstream in_str("1.txt");
	ofstream out_str("2.txt");
	
	int numOfCases = 0;
	in_str >> numOfCases;
	char c;
	in_str.get(c);
	in_str.get(c);
	
	for(int i = 0; i < numOfCases; i++){
		
		string input = "", output = "";
		getline(in_str,input);
		for(int j = 0; j < input.length(); j++){
			char charTemp = ' ';
			charTemp = answer(input[j]);
			output += charTemp;
		}
		
		if(i < numOfCases-1)
			out_str << "Case #" << i+1 << ": " << output << endl;
		else
			out_str << "Case #" << i+1 << ": " << output;
	}
	return 0;
}