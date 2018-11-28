#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstring>
using namespace std;

ifstream fin("A-small-attempt1.in");
ofstream fout("A.out");

int mapping[27];

void getMapping()
{
	char str1[64], str2[64];
	strcpy(str1, "ejp mysljylc kd kxveddknmc re jsicpdrysi");
	strcpy(str2, "our language is impossible to understand");
	for(int i = 0; i < strlen(str1); i++)
		if(str1[i] != ' ')
			mapping[str1[i]-97] = str2[i];
	strcpy(str1, "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
	strcpy(str2, "there are twenty six factorial possibilities");
	for(int i = 0; i < strlen(str1); i++)
		if(str1[i] != ' ')
			mapping[str1[i]-97] = str2[i];
	strcpy(str1, "de kr kd eoya kw aej tysr re ujdr lkgc jv");
	strcpy(str2, "so it is okay if you want to just give up");
	for(int i = 0; i < strlen(str1); i++)
		if(str1[i] != ' ')
			mapping[str1[i]-97] = str2[i];
	mapping[25] = 'q';
	mapping[16] = 'z';
}

int main()
{
	getMapping();
	int T;
	fin >> T;
	char str[105];
	fin.getline(str, 104, '\n');
	for(int count = 1; count <= T; count++)
	{
		fin.getline(str, 104, '\n');
		fout << "Case #" << count << ": ";
		for(int i = 0; i < strlen(str); i++)
			if(str[i] == ' ')
				fout << " ";
			else
				fout << (char)(mapping[str[i]-97]);
		fout << endl;
	}
	return 0;
}
