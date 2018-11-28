#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;

#define lint long long
#define uint usigned long long

int main (int argc, char * const argv[]) {
    
	ifstream inFile("../../input.txt");
	ofstream outFile("../../output.txt");
	int numCases;
	
	map<char,char> charMap;
	charMap['a'] = 'y';
	charMap['b'] = 'h';
	charMap['c'] = 'e';
	charMap['d'] = 's';
	charMap['e'] = 'o';
	charMap['f'] = 'c';
	charMap['g'] = 'v';
	charMap['h'] = 'x';
	charMap['i'] = 'd';
	charMap['j'] = 'u';
	charMap['k'] = 'i';
	charMap['l'] = 'g';
	charMap['m'] = 'l';
	charMap['n'] = 'b';
	charMap['o'] = 'k';
	charMap['p'] = 'r';
	charMap['q'] = 'z';
	charMap['r'] = 't';
	charMap['s'] = 'n';
	charMap['t'] = 'w';
	charMap['u'] = 'j';
	charMap['v'] = 'p';
	charMap['w'] = 'f';
	charMap['x'] = 'm';
	charMap['y'] = 'a';
	charMap['z'] = 'q';
	
	
	inFile >> numCases;
	string test;
	getline(inFile,test);
	for(int caseNum =1; caseNum <=numCases; caseNum++)
	{
		outFile<<"Case #"<<caseNum<<": ";
		string inpt;
		getline(inFile, inpt);
		for(int i =0; i< inpt.length(); i++)
		{
			char c= inpt[i];
			map<char,char>::iterator it = charMap.find(c);
			if(it!= charMap.end())
				outFile<<it->second;
			else
				outFile<<c;
		}
		outFile<<'\n';
		
		
	}
	inFile.close();
	outFile.close();
	std::cout << "Done!\n";
    return 0;
}
