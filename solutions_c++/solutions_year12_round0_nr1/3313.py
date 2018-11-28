// SpeakingInTongues.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <hash_map>
#include <algorithm>
#include <stdio.h>

using namespace std;

void fillMap(char* coded, char* plain, hash_map<char,char>& ciphered) 
{
	int size = strlen(coded);
	for (int i=0; i< size; ++i)
	{
		ciphered[coded[i]] = plain[i];
	}
}

int main(int argc, char* argv[])
{
	int i, numCase;
	hash_map<char, char> trans;
	
	freopen("c://temp//A-small-attempt1.in", "r+", stdin);
	freopen("c://temp//out2.txt", "w+", stdout);

	char coded[3][100] = {
						"ejp mysljylc kd kxveddknmc re jsicpdrysi",
						"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
						"de kr kd eoya kw aej tysr re ujdr lkgc jv"};

	char plain[3][100]  = {
						"our language is impossible to understand",
						"there are twenty six factorial possibilities",
						"so it is okay if you want to just give up"
						};

	for (int i=0; i<3; ++i)
		fillMap(coded[i], plain[i], trans);

	trans['y'] = 'a';
	trans['e'] = 'o';
	trans['q'] = 'z';
	//and the missing letter is; 
	//I felt like watching sesame Street
	//if you are reading this; drop me a line :D
	trans['z'] = 'q';

	trans[' ']=' ';

	for (hash_map<char, char>::iterator it = trans.begin(); it!= trans.end(); ++it)
		printf(" %c -> %c\n", it->first, it->second);

	printf("\n");


	char line[110];


	scanf("%i", &numCase);
	gets(line);

	for (int i=1; i<= numCase; ++i)
	{
		gets(line);
		printf("Case #%i: ",i);
		for (int j=0 ; j<strlen(line);++j)
			line[j] = trans[line[j]];
		printf("%s\n",line);

	}

	return 0;
}

