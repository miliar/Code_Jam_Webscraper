// QualProb1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string.h>
#include <vector>
#include <stack>
#include <queue>
#include<iostream>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	char *current_line = new char[1000];
	cin.getline(current_line, 999);
	int N=0;
	sscanf(current_line,"%d",&N);

	const char *s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	const char *out_s1 = "our language is impossible to understand";

	const char *s2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	const char *out_s2 = "there are twenty six factorial possibilities";

	const char *s3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	const char *out_s3 = "so it is okay if you want to just give up";

	int *mapping = new int[26];

	for(int i=0; i< strlen(s1); i++)
	{
		char c = s1[i];

		mapping[c -'a'] = out_s1[i] - 'a';

	}

	for(int i=0; i< strlen(s1); i++)
	{
		char c = s2[i];

		mapping[c -'a'] = out_s2[i] - 'a';

	}
	
	for(int i=0; i< strlen(s1); i++)
	{
		char c = s3[i];

		mapping[c -'a'] = out_s3[i] - 'a';

	}

	mapping['q'-'a'] = 'z' -'a';
	mapping[25] = 16;

	for(int j=0; j<N; j++)
	{
		cin.getline(current_line, 999);
		cout<<"Case #"<<j+1<<": ";
		for(int k=0; k<strlen((const char *)current_line); k++)
			cout<<(char)(mapping[current_line[k] - 'a'] + 'a');
		cout<<endl;
	}
	return 0;
}

