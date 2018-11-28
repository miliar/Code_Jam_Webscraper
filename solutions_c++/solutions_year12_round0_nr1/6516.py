#include<iostream>
#include<stdio.h>
#include<fstream>

using namespace std;

char lookup(char input)
{
	int i,flag=0;
	char gCode[26];
	char dCode[26];
	gCode[0]='a';gCode[1]='b';gCode[2]='c';gCode[3]='d';gCode[4]='e';gCode[5]='f';gCode[6]='g';gCode[7]='h';
	gCode[8]='i';gCode[9]='j';gCode[10]='k';gCode[11]='l';gCode[12]='m';gCode[13]='n';gCode[14]='o';gCode[15]='p';
	gCode[16]='q';gCode[17]='r';gCode[18]='s';gCode[19]='t';gCode[20]='u';gCode[21]='v';gCode[22]='w';gCode[23]='x';
	gCode[24]='y';gCode[25]='z';
	
	dCode[0]='y';dCode[1]='h';dCode[2]='e';dCode[3]='s';dCode[4]='o';dCode[5]='c';dCode[6]='v';dCode[7]='x';
	dCode[8]='d';dCode[9]='u';dCode[10]='i';dCode[11]='g';dCode[12]='l';dCode[13]='b';dCode[14]='k';dCode[15]='r';
	dCode[16]='z';dCode[17]='t';dCode[18]='n';dCode[19]='w';dCode[20]='j';dCode[21]='p';dCode[22]='f';dCode[23]='m';
	dCode[24]='a';dCode[25]='q';
	
	for(i=0;i<26;i++)
	{
		if(input==gCode[i])
		{
			flag=1;
			return dCode[i];
		}
	}
	if(flag==0)
		return '0';	
	
}

int main()
{
	char googlechar,dichar='y';
	int i=1,readlines=0;
	ifstream infile ("input.in");
	ofstream outfile;
	outfile.open ("out.txt");
	infile>>readlines;
	googlechar=infile.get();
	while(readlines>0)
	{
		fflush(stdin);
		googlechar=infile.get();
		outfile<<"Case #"<<i<<": ";
		while (googlechar!='\n')
		{
			dichar=lookup(googlechar);
			if(dichar!='0')
				outfile<<dichar; 
			else
				outfile<<" ";
			cout<<dichar;
			fflush(stdin);
			googlechar=infile.get();
		}
		outfile<<'\n';
		readlines-=1;
		i++;
	}

	outfile.close();
}
