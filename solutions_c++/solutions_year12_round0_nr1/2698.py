#include<iostream>
#include<string>

using namespace std;
char replace(char input)
{
	switch(input)
	{
		case 'y': return 'a';
		case 'n': return 'b';
		case 'f': return 'c';
		case 'i': return 'd';
		case 'c': return 'e';
		case 'w': return 'f';
		case 'l': return 'g';
		case 'b': return 'h';
		case 'k': return 'i';
		case 'u': return 'j';
		case 'o': return 'k';
		case 'm': return 'l';
		case 'x': return 'm';
		case 's': return 'n';
		case 'e': return 'o';
		case 'v': return 'p';
		case 'z': return 'q';
		case 'p': return 'r';
		case 'd': return 's';
		case 'r': return 't';
		case 'j': return 'u';
		case 'g': return 'v';
		case 't': return 'w';
		case 'h': return 'x';
		case 'a': return 'y';
		case 'q': return 'z';
		default: return input;
	}
}
int main(void)
{
	int numofcase;
	cin>>numofcase;
	string temp;
	getline(cin, temp);
	for(int i=0; i<numofcase ; i++)
	{
		getline(cin, temp);
		int length = temp.length();
		char* tempchar = new char[length+1];
		int j=0;
		for( j = 0 ; j<length ;j++)
		{
			char out = replace(temp[j]);
			tempchar[j]=out;
		}
		tempchar[j]='\0';
		cout<<"Case #"<<(i+1)<<": "<<tempchar<<endl;
	}
return 0;
}	















