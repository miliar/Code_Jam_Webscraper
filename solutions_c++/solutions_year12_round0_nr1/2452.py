#include <iostream.h>
#include <fstream.h>

// Code Jam 2012
// Qualification Round
// Problem A. Speaking in Tongues



int main(int argc, char *argv[])
{
	int T;
	int t;
	char c;
	char G[101];
	char S[101];
	
	char map[27] = "yhesocvxduiglbkrztnwjpfmaq";
	
	/*
		abcdefghijklmnopqrstuvwxyz
		yhesocvxduiglbkrztnwjpfmaq
		 
	*/
	
	int i;
	
	ifstream inFile;
	
	//inFile.open("test.in");
	if ( argc < 2 )
	{
		cout << "No input file given!" << endl;
		exit(1);
	}
	inFile.open(argv[1]);
	if ( !inFile )
	{
		cout << "Error opening file!" << endl;
		exit(1);
	}
	
	inFile >> T;
	
	inFile.getline(S,101);
	
	for (t=0;t<T;t++)
	{
		inFile.getline(S,101);
		
		for (i=0;i<101;i++)
		{
			G[i] = 0;
		}
		
		for (i=0;i<101;i++)
		{
			if (S[i] == 0)
			{
				G[i] = 0;
				break;
			}
			if ( S[i] == ' ' )
			{
				G[i] = ' ';
			}
			else
			{
				G[i] = map[S[i]-'a'];
			}
		}
		
		
		cout << "Case #" << t+1 << ": "<< G << endl;
	}
		
		
	
	inFile.close();
	return 0;
}