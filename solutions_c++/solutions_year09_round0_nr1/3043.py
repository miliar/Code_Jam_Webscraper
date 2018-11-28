// Alien Language.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>

using namespace std;

void main(){
	ifstream inputFile("A-large.in", ios::in);

	if(!inputFile)
	{
		cout<<"File could not be opened"<<endl;
		exit(1);
	}

	int wordLen;
	inputFile >> wordLen;
	int wordNum;
	inputFile >> wordNum;
	int caseNum;
	inputFile >> caseNum;
	
	char **wordArray = new char*[wordNum];	
	for(int i=0;i<wordNum;i++){
		wordArray[i] = new char[wordLen];
		inputFile >> wordArray[i];
		wordArray[i][wordLen] = 0;
	}

	//for(int i=0;i<wordNum;i++)
	//	cout<<wordArray[i]<<"\n";
	//system("pause");
	char *testStr = new char[wordLen*(32)];
	for(int j=1;j<=caseNum;j++){
		inputFile >> testStr;		
		int matchWord = 0;
		
		for(int k=0;k<wordNum;k++){
			bool match = false;
			int curChar = 0;
			for(int m=0;m<wordLen;m++){
				match = false;
				if(testStr[curChar] == '('){
					curChar++;
					while(testStr[curChar] != ')'){						
						if(testStr[curChar] == wordArray[k][m])
							match = true;
						curChar++;
					}
				}
				else if(testStr[curChar] == wordArray[k][m])
					match = true;

				if(!match)
					break;
				curChar++;
			}
			if(match)
				matchWord++;
		}
		cout<<"Case #"<<j<<": "<<matchWord<<"\n";
	}
}
