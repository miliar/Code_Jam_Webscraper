#include <iostream>
#include <fstream>
#include <string>

using namespace std;

char getchar(char in)
{
	char g[]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
	char e[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	int i=0;
	while (g[i]!=in) 
		++i;
		
	return e[i];
}

int main()
{
	ifstream inFile;
	ofstream outFile;
	inFile.open("A-small-attempt1.in");
	outFile.open("output.txt");	
	int size;
	string sent;
	//getline(inFile,size);	
	inFile >> size;
	string tmp;
	getline(inFile,tmp);
	for (int i=0; i<size; ++i)
	{
		getline(inFile, sent);
		//inFile >> sent;
		//cout << sent.length() << endl;
		outFile << "Case #" << i+1 << ": ";
				
		int j=0;		
		while (j<sent.length())
			{
				if (sent[j]!=' ' and sent[j]!='-')
					outFile << getchar(sent[j]);					
				else	
					outFile << sent[j];					
				++j;
			}
		outFile << '\n';
	}	
	inFile.close();
	outFile.close();
}


