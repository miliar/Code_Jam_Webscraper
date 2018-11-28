// CodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <stack>
#include <math.h>
#include <fstream>
#include <regex> 
using namespace std;
using namespace std::tr1;

unsigned int wordsFound=0;
string tmpString;

inline void Search(char alphabet,char searchedFrom,int position)
{
	for(unsigned int x=position;x<tmpString.length();x++)
	{
		int pos;
		pos=tmpString.find(alphabet,x);
			
		if(pos!=tmpString.npos)
		{
			x=pos;

			//if(alphabet=='w' && searchedFrom=='s'){Search(textLine,'e','w',x+1);} 
			//else if(alphabet=='e' && searchedFrom=='w'){Search(textLine,'l','e',x+1);}
			//else if(alphabet=='l' && searchedFrom=='e'){Search(textLine,'c','l',x+1);} 
			//else if(alphabet=='c' && searchedFrom=='l'){Search(textLine,'o','c',x+1);}
			//else if(alphabet=='o' && searchedFrom=='c'){Search(textLine,'m','o',x+1);} 
			//else if(alphabet=='m' && searchedFrom=='o'){Search(textLine,'e','m',x+1);} 
			//else if(alphabet=='e' && searchedFrom=='m'){Search(textLine,' ','e',x+1);} 
			//else if(alphabet==' ' && searchedFrom=='e'){Search(textLine,'t',' ',x+1);}
			//else if(alphabet=='t' && searchedFrom==' '){Search(textLine,'o','t',x+1);} 
			//else if(alphabet=='o' && searchedFrom=='t'){Search(textLine,' ','o',x+1);} 
			//else if(alphabet==' ' && searchedFrom=='o'){Search(textLine,'c',' ',x+1);} 
			//else if(alphabet=='c' && searchedFrom==' '){Search(textLine,'o','p',x+1);}  //searched from a dummy p 'cuz already searched from a c
			//else if(alphabet=='o' && searchedFrom=='p'){Search(textLine,'d','o',x+1);} 
			//else if(alphabet=='d' && searchedFrom=='o'){Search(textLine,'e','d',x+1);} 
			//else if(alphabet=='e' && searchedFrom=='d'){Search(textLine,' ','p',x+1);} //again dummy p
			//else if(alphabet==' ' && searchedFrom=='p'){Search(textLine,'j',' ',x+1);}
			//else if(alphabet=='j' && searchedFrom==' '){Search(textLine,'a','j',x+1);}
			//else if(alphabet=='a' && searchedFrom=='j'){Search(textLine,'m','a',x+1);}
			//else if(alphabet=='m' && searchedFrom=='a'){wordsFound++;}	
			
			if(alphabet=='w' && searchedFrom=='s'){Search('e','w',x+1);} 
			else if(alphabet=='e' && searchedFrom=='w'){Search('l','e',x+1);}
			else if(alphabet=='l' && searchedFrom=='e'){Search('c','l',x+1);} 
			else if(alphabet=='c' && searchedFrom=='l'){Search('o','c',x+1);}
			else if(alphabet=='o' && searchedFrom=='c'){Search('m','o',x+1);} 
			else if(alphabet=='m' && searchedFrom=='o'){Search('e','m',x+1);} 
			else if(alphabet=='e' && searchedFrom=='m'){Search(' ','e',x+1);} 
			else if(alphabet==' ' && searchedFrom=='e'){Search('t',' ',x+1);}
			else if(alphabet=='t' && searchedFrom==' '){Search('o','t',x+1);} 
			else if(alphabet=='o' && searchedFrom=='t'){Search(' ','o',x+1);} 
			else if(alphabet==' ' && searchedFrom=='o'){Search('c',' ',x+1);} 
			else if(alphabet=='c' && searchedFrom==' '){Search('o','p',x+1);}  //searched from a dummy p 'cuz already searched from a c
			else if(alphabet=='o' && searchedFrom=='p'){Search('d','o',x+1);} 
			else if(alphabet=='d' && searchedFrom=='o'){Search('e','d',x+1);} 
			else if(alphabet=='e' && searchedFrom=='d'){Search(' ','p',x+1);} //again dummy p
			else if(alphabet==' ' && searchedFrom=='p'){Search('j',' ',x+1);}
			else if(alphabet=='j' && searchedFrom==' '){Search('a','j',x+1);}
			else if(alphabet=='a' && searchedFrom=='j'){Search('m','a',x+1);}
			else if(alphabet=='m' && searchedFrom=='a'){wordsFound++;}	
		}

	}	
	
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream inputFile;
	ofstream outputFile;
	string filename,filename2; 

	filename="input.txt";
	filename2="output.txt";

	inputFile.open(filename.c_str());  
	if(!inputFile)
	{
		cout<<"Error Opening File";
	}
	else
	{
		outputFile.open(filename2.c_str());
	
		int noCases;
		inputFile>>noCases;
		getline(inputFile,tmpString);

		for(int i=1;i<=noCases;i++)
		{
			wordsFound=0;
			getline(inputFile,tmpString);
			Search('w','s',0);

			
			string tmpWordsFound;
			int x=0;
			int digit;
			char cdigit[50];

			do
			{				
				digit=wordsFound%10;
				itoa(digit,&cdigit[x],10);				
				x++;
				wordsFound=wordsFound/10;
			}while(x<4&&wordsFound>0);

			while(x<4)
			{
				cdigit[x]='0';
				x++;
			}
			
			
			outputFile<<"Case #"<<i<<": ";
			for(int x=3;x>=0;x--)
			{
				outputFile<<cdigit[x];
			}
			
			outputFile<<"\n";

			
		}

		outputFile.close();

	}
	
	inputFile.close();
		
	cout<<"\n";
	system ("pause");
	return 0;	
}

