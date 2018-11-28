

#include <iostream>
#include <fstream> 
#include <string>

using namespace std;

string translate(string theString);
string intToString(int x);

int main()
{

	int inputLines;
	ofstream fout;
	fout.open("file");

	ifstream fin;
	fin.open("A-small-attempt3.in");
	if(!fin.fail())
	{
		string garbage;
		
		fin>>inputLines;
		getline(fin, garbage);

		
		if(inputLines > 0)
		{
									

			for(int i=0; i<inputLines; i++)
			{
				string googlerese;
				string english;
						
				getline(fin, googlerese);
				if(!fin.eof())
				{
					english = translate(googlerese);
					cout<<"Case #" + intToString((i+1)) + ":" + " " + english<<endl<<endl;
					fout<<"Case #" + intToString((i+1)) + ":" + " " + english<<endl<<endl;
				}
				
			}

		}


	}
	fout.close();




	return 0;
}




string translate(string theString)
{

	string englishString = "";
	int length = theString.length();

	for(int i=0; i<length; i++)
	{
		if(theString[i] == 'a')
		{
			englishString += 'y';
		}
		else if(theString[i] == 'b')
		{
			englishString += 'h';
		}
		else if(theString[i] == 'c')
		{
			englishString += 'e';
		}
		else if(theString[i] == 'd')
		{
			englishString += 's';
		}
		else if(theString[i] == 'e')
		{
			englishString += 'o';
		}
		else if(theString[i] == 'f')
		{
			englishString += 'c';
		}
		else if(theString[i] == 'g')
		{
			englishString += 'v';
		}
		else if(theString[i] == 'h')
		{
			englishString += 'x';
		}
		else if(theString[i] == 'i')
		{
			englishString += 'd';
		}
		else if(theString[i] == 'j')
		{
			englishString += 'u';
		}
		else if(theString[i] == 'k')
		{
			englishString += 'i';
		}
		else if(theString[i] == 'l')
		{
			englishString += 'g';
		}
		else if(theString[i] == 'm')
		{
			englishString += 'l';
		}
		else if(theString[i] == 'n')
		{
			englishString += 'b';
		}
		else if(theString[i] == 'o')
		{
			englishString += 'k';
		}
		else if(theString[i] == 'p')
		{
			englishString += 'r';
		}
		else if(theString[i] == 'q')
		{
			englishString += 'z';
		}
		else if(theString[i] == 'r')
		{
			englishString += 't';
		}
		else if(theString[i] == 's')
		{
			englishString += 'n';
		}
		else if(theString[i] == 't')
		{
			englishString += 'w';
		}
		else if(theString[i] == 'u')
		{
			englishString += 'j';
		}
		else if(theString[i] == 'v')
		{
			englishString += 'p';
		}
		else if(theString[i] == 'w')
		{
			englishString += 'f';
		}
		else if(theString[i] == 'x')
		{
			englishString += 'm';
		}
		else if(theString[i] == 'y')
		{
			englishString += 'a';
		}
		else if(theString[i] == 'z')
		{
			englishString += 'q';
		}
		else if(theString[i] == ' ')
		{
			englishString += ' ';
		}

	}


	return englishString;
}


string intToString(int x)  
{
	string result;

	char temp[256];

	_itoa_s(x,temp,255,10);

	result=temp;

	return result;
}