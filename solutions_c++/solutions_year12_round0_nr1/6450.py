#include <iostream>
#include <string>
#include <fstream>
using namespace std;
string translate(string input);

int main(int argc, char * argv[])
{
	if(argc != 3)
	{
	   cout << "Not enough arguments" << endl;
	   return 1;
	}
	ifstream in(argv[1]);
	ofstream outputFile(argv[2]);
	if(!in)
	{
	   cout << "File " << argv[1] << " not found" << endl;
	   return 1;
	}
	
	string str;
	int caseNum = 1;
	int numCase = 0;
	//in >> numCase;
	//getline(in, inp);
	while(getline(in, str))
	{
		if(numCase == 0) //skip first line
		{
			numCase++;
			continue;
		}
		outputFile << "Case #" << caseNum++ << ": " << translate(str) << endl; 
	}
}

string translate(string input)
{
	string result, temp;
  	for(int i = 0; i < input.size(); i++)
	{
	    temp = "";
	    switch(input[i])
	    {
		case 'y': 
			temp = 'a';
			break;
		case 'n': 
			temp = 'b';
			break;
		case 'f': 
			temp = 'c';
			break;
		case 'i': 
			temp = 'd';
			break;
		case 'c': 
			temp = 'e';
			break;
		case 'w': 
			temp = 'f';
			break;
		case 'l': 
			temp = 'g';
			break;
		case 'b': 
			temp = 'h';
			break;
		case 'k': 
			temp = 'i';
			break;
		case 'u': 
			temp = 'j';
			break;
		case 'o': 
			temp = 'k';
			break;
		case 'm': 
			temp = 'l';
			break;
		case 'x': 
			temp = 'm';
			break;
		case 's': 
			temp = 'n';
			break;
		case 'e': 
			temp = 'o';
			break;
		case 'v': 
			temp = 'p';
			break;
		case 'z':
			temp = 'q';
			break;
		case 'p': 
			temp = 'r';
			break;
		case 'd': 
			temp = 's';
			break;
		case 'r': 
			temp = 't';
			break;
		case 'j': 
			temp = 'u';
			break;
		case 'g': 
			temp = 'v';
			break;
		case 't': 
			temp = 'w';
			break;
		case 'h': 
			temp = 'x';
			break;
		case 'a': 
			temp = 'y';
			break;
		case 'q':
			temp = 'z';
			break;
		case ' ':
			temp = ' ';
			break;
	    }
	    result += temp;
	}
	return result;
}
