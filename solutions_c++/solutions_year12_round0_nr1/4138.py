#include<iostream>
#include<fstream>
#include<string>

using namespace std;
char transChar(char aCharacter);
int main()
{
  string theData;
  int numExamples;
  char theChar;
  ifstream ipfile1;
  ipfile1.open("input.txt");
 
  ipfile1>>numExamples;
  getline(ipfile1, theData);
  for (int i=0; i<numExamples; i++)
  {
	theData.clear();
	getline(ipfile1, theData);
	cout<<"Case #"<<i+1<<":"<<" ";
	for (int j=0; j<theData.length(); j++)
	{
		cout<<transChar(theData.at(j));
	}
	cout<<endl;	
  }  
   
}


char transChar(char aCharacter)
{
   switch(aCharacter)
   {
	case 'y' : return 'a';
	case 'n' : return 'b';
	case 'f' : return 'c';
	case 'i' : return 'd';
	case 'c' : return 'e';
	case 'w' : return 'f';
	case 'l' : return 'g';
	case 'b' : return 'h';
	case 'k' : return 'i';
	case 'u' : return 'j';
	case 'o' : return 'k';
	case 'm' : return 'l';
	case 'x' : return 'm';
	case 's' : return 'n';
	case 'e' : return 'o';
	case 'v' : return 'p';
	case 'z' : return 'q';
	case 'p' : return 'r';
	case 'd' : return 's';
	case 'r' : return 't';
	case 'j' : return 'u';
	case 'g' : return 'v';
	case 't' : return 'w';
	case 'h' : return 'x';
	case 'a' : return 'y';
	case 'q' : return 'z';
	case ' ' : return ' ';
   }
}
