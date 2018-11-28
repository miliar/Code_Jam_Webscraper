#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	
	char a[101];
	char b[26];
	int t;
	fstream in,out;
	std::string phrase;
	std::string file1= "./input.in";
	std::string file2= "./output.out";
	
	in.open(file1.c_str(),ios::in);
	out.open(file2.c_str(),ios::out);
	b[0]='y';
	b[1]='h';
	b[2]='e';
	b[3]='s';
	b[4]='o';
	b[5]='c';
	b[6]='v';
	b[7]='x';
	b[8]='d';
	b[9]='u';
	b[10]='i';
	b[11]='g';
	b[12]='l';
	b[13]='b';
	b[14]='k';
	b[15]='r';
	b[16]='z';
	b[17]='t';
	b[18]='n';
	b[19]='w';
	b[20]='j';
	b[21]='p';
	b[22]='f';
	b[23]='m';
	b[24]='a';
	b[25]='q';

	int i=0;

	std::getline(in, phrase, '\n');
	
	t=atoi(phrase.c_str());
	
	while(true)
	{
		if(i==t)
			break;
		
		else
		{
			std::getline(in, phrase, '\n');
			out<<"Case #"<<i+1<<": ";
			i++;
			
			
			int j=0;

			while(j!=phrase.size())
			{
				int x;
				
				if(phrase[j]!=' ')
				{
					x=phrase[j]-97;
					phrase[j]=b[x];
				}

	
				j++;
			}
			
			out<<phrase<<'\n';
			

		}

		
	}
	out.close();
	in.close();
	
}