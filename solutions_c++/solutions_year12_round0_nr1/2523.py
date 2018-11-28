#include<iostream>
#include<map>
#include<fstream>

using namespace std;

int main(int argc, char *argv[])
{
	ifstream file;
	ofstream outputFile;
	
	string inputString;
	
	int intTestCases=0,leng=0;
	
	cout << "File = " << argv[2];
	outputFile.open(argv[2]);
	file.open(argv[1]);
	
	//Read integers..
	if(!file.eof())
	{
		file >> intTestCases;
		getline(file, inputString);
	}
	
	map<char,char> myMap;
	map<char,char>::iterator it;

	myMap['a']='y';
	myMap['b']='h';
	myMap['c']='e';
	myMap['d']='s';
	myMap['e']='o';
	myMap['f']='c';
	myMap['g']='v';
	myMap['h']='x';
	myMap['i']='d';
	myMap['j']='u';
	myMap['k']='i';
	myMap['l']='g';
	myMap['m']='l';
	myMap['n']='b';
	myMap['o']='k';
	myMap['p']='r';
	myMap['q']='z';
	myMap['r']='t';
	myMap['s']='n';
	myMap['t']='w';
	myMap['u']='j';
	myMap['v']='p';
	myMap['w']='f';
	myMap['x']='m';
	myMap['y']='a';
	myMap['z']='q';
	myMap[' ']=' ';
	
	for(int i=0; i<intTestCases; ++i)
	{
		getline(file, inputString);		
		leng = inputString.length();
		
		outputFile << "Case #" << i+1 << ": ";
		
		for (int i=0; i<leng; ++i) {
			outputFile << myMap[inputString[i]];
		}
		
		outputFile << endl;
		
		inputString="";
	}

	outputFile.close();
	file.close();
	
	return 0;

}

