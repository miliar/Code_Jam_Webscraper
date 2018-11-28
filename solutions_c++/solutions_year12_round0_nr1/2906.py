#include<string>
#include<iostream>
#include<fstream>
using namespace std;

int line=30;
char lib[]="yhesocvxduiglbkrztnwjpfmaq";
char text[31][101];

void loadWords(void)
{
	int n=0;
	ifstream file;
	file.open("A-small-attempt2.in");
	while(file.getline(text[n],101))
		n++;
	file.close();
}

void changeChar(void)
{
	for(int m=1; m<=line; m++)
	{
		for(int n=0; text[m][n] != '\0'; n++)
		{
			if(text[m][n] > 96 && text[m][n] < 123)
				text[m][n] = lib[(int)text[m][n]-97];
		}
	}
}

int main(void)
{
	loadWords();
	changeChar();
	ofstream result;
	result.open("result.out");
	for(int m=1; m<=line; m++)
	{
		if(text[m][0] != 0)
		{
			if(m != 1)
				result << endl;
			result << "Case #" << m << ": ";
			result << text[m] ;
		}
	}
	result.close();

	return 0;
}