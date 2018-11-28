// LanguageMapping.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <map>
#include <iostream>
#include <fstream>

using namespace std;
#define MAX_LINE_SIZE 128

char samplecharmap[26];
void interpretSampleAndGeneratecharMap(char* samplein, char* sampleout)
{
	for(int i = 0; i< 26; i++)
	{
		samplecharmap[i] = '0';
	}
	for(int i = 0; i < strlen(samplein); i++)
	{
		char c = samplein[i];
		if(c != ' ')
		{
			samplecharmap[(int)c -(int)('a')] = sampleout[i];
		}
	}
	samplecharmap[(int)'z' - int('a')] = 'q';
	samplecharmap[(int)'q' - int('a')] = 'z';
	for(int i = 0; i< 26; i++)
	{
		printf("\n [%c] --> [%c]", (char)('a'+i), samplecharmap[i]);
	}
}

void decodeLine(char* inputline, char* outputline)
{
	char c;
	unsigned int i;
	for( i = 0; i < strlen(inputline); i++)
	{
		c = inputline[i];
		if(c == ' ')
		{
			outputline[i] = inputline[i];
		}
		else
		{
			outputline[i] = samplecharmap[(int)c - (int)('a')];
		}
	}
	outputline[i] = '\0';
}

int main(int argc, char* argv[])
{

	char* samplein = "ejp mysljylc kd kxveddknmc re jsicpdrysi \
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd \
de kr kd eoya kw aej tysr re ujdr lkgc jv";
	char *sampleout = "our language is impossible to understand \
there are twenty six factorial possibilities \
so it is okay if you want to just give up";
	interpretSampleAndGeneratecharMap(samplein, sampleout);
	if(argc < 2)
	{
		printf("\n Input file not specified");
		return -1;
	}

	int i = 0;
	char inputline[MAX_LINE_SIZE];
	char outputline[MAX_LINE_SIZE];
	ifstream infile(argv[1]);
	ofstream outfile("output.txt");
	infile.getline(inputline, MAX_LINE_SIZE);
	int numInputLines = atoi(inputline);
	while(i < numInputLines)
	{
		infile.getline(inputline, MAX_LINE_SIZE, '\n');
		decodeLine(inputline, outputline);
		outfile<<"Case #"<<i+1<<": ";
		outfile<<outputline<<"\n";
		i++;
	}
	return 0;
}

