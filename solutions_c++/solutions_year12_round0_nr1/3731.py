// Qualification.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "fstream"
#include "string.h"
using namespace std;

#define INFILE "A-small-attempt1.in"
#define INFILE2 "A-small-help.out"
#define OUTFILE "A-small.out"

char strIn[50][120];
char strOut[30][120];
int mark[500];

char strMap[500];

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream infile(INFILE);
	ifstream infile2(INFILE2);
	ofstream outfile(OUTFILE);

	char str[500];
	infile2.getline(str,1000);
	for (int i='a'; i<='z'; i++)
	{
		strMap[i] = str[i-'a'];
	}

	//for (int i='a'; i<='z'; i++)
	//	printf("%c",strMap[i]);
	int t;
	infile>>t;
	infile.getline(strIn[0],1000);
	//printf("%d\n",t);
	for (int i=0; i<t; i++)
	{
		infile.getline(strIn[i],1000);
		//printf("%d",strlen(strIn[i]));
		outfile<<"Case #"<<i+1<<": ";
		for (int j=0; j<strlen(strIn[i]); j++)
			outfile<<strMap[strIn[i][j]];
			//strOut[i][j]=strMap[strIn[i][j]];
			//printf("%c",strIn[i][j]);
		//printf("\n");
		outfile<<"\n";
	}
	
	infile.close();
	infile2.close();
	outfile.close();

	return 0;
}

