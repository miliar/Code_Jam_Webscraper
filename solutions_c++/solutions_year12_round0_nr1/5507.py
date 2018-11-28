#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

static char map[26];

int main()
{
	//fill map
	map['a'-97]='y';
	map['b'-97]='h';
	map['c'-97]='e';
	map['d'-97]='s';
	map['e'-97]='o';
	map['f'-97]='c';
	map['g'-97]='v';
	map['h'-97]='x';
	map['i'-97]='d';
	map['j'-97]='u';
	map['k'-97]='i';
	map['l'-97]='g';
	map['m'-97]='l';
	map['n'-97]='b';
	map['o'-97]='k';
	map['p'-97]='r';
	map['q'-97]='z';
	map['r'-97]='t';
	map['s'-97]='n';
	map['t'-97]='w';
	map['u'-97]='j';
	map['v'-97]='p';
	map['w'-97]='f';
	map['x'-97]='m';
	map['y'-97]='a';
	map['z'-97]='q';

	int count;
	string* line;
	string buff;

	ifstream file;
	file.open("input.txt");

	//get count
	getline(file,buff);
	sscanf(buff.c_str(),"%d",&count);
	
	line=new string[count];
	for(int i=0;i<count;i++)
	{
		getline(file,line[i]);
		printf("%d. %s\n",i+1,line[i].c_str());
	}
	file.close();

	printf("\n---\n");

	ofstream out;
	out.open("output.txt");

	for(int i=0;i<count;i++)
	{
		for(int b=0;b<line[i].length();b++)
		{
			if(line[i][b]!=' ')
				line[i][b]=map[line[i][b]-97];
		}
		
		char buff[100];
		sprintf(buff,"Case #%d: %s\n",i+1,line[i].c_str());

		out.write(buff,strlen(buff));
		printf("%d. %s\n",i+1,line[i].c_str());
	}

	out.close();

	system("PAUSE");
	return 0;
}