#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>



char getKey(char value)
{
	switch (value) {
		case 'a':
			return 'y';
			break;
		case 'b':
			return 'h';
			break;
		case 'c':
			return 'e';
			break;
		case 'd':
			return 's';
			break;
		case 'e':
			return 'o';
			break;
		case 'f':
			return 'c';
			break;
		case 'g':
			return 'v';
			break;
		case 'h':
			return 'x';
			break;
		case 'i':
			return 'd';
			break;
		case 'j':
			return 'u';
			break;
		case 'k':
			return 'i';
			break;
		case 'l':
			return 'g';
			break;
		case 'm':
			return 'l';
			break;
		case 'n':
			return 'b';
			break;
		case 'o':
			return 'k';
			break;
		case 'p':
			return 'r';
			break;
		case 'q':
			return 'z';
			break;
		case 'r':
			return 't';
			break;
		case 's':
			return 'n';
			break;
		case 't':
			return 'w';
			break;
		case 'u':
			return 'j';
			break;
		case 'v':
			return 'p';
			break;
		case 'w':
			return 'f';
			break;
		case 'x':
			return 'm';
			break;
		case 'y':
			return 'a';
			break;
		case 'z':
			return 'q';
			break;
		default:
			//iostream::cout << " ";
			return ' ';
	}
  	
}


using namespace std;

int main(int argc, char *argv[])
{
	if( remove( "example.txt" ) != 0 )
		perror( "Error deleting file" );
	 else
		puts( "File successfully deleted" );

	  ifstream in("A-small-attempt1.in");
	  //ifstream in("sample01.in");  

	 if(!in) {
		cout << "Cannot open input file.\n";
		return 1;
	 }
	

	string valT;
  	getline(in, valT, '\n');
  	long valIntT = atoi (valT.c_str());


	FILE * pFile;
	pFile = fopen ("example.txt", "a");

	ofstream myfile;
	myfile.open ("example.txt", ios::app);

	for(long i = 0; i < valIntT; i++)
	{
		string valG;
		//int valIntG;
		getline(in, valG, '\n');  	
	  	//cout << "valT: " << valT << " valG: " << valG << endl;
		cout << "valG.length: " << valG.size() << endl;
		cout << "Case #" << (i + 1) << ": " << valG << endl;
		cout <<  " After " << endl;
		for(long i = 0; i < valG.size(); i++)
		{		
			
			valG.replace(i, 1, 1, getKey(valG[i]));  
			

		}	

		cout << "Case #" << (i + 1) << ": " << valG << endl << endl;
		
			
		 myfile << "Case #" << (i + 1) << ": " << valG << endl;
		  	

	}

	myfile.close();
	fclose (pFile);


	
	
	

	


  in.close();

  return 0;
}
