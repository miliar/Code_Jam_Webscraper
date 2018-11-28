// GCJ-2012 - Qualification round - Problem A. Speaking in Tongues

#include "stdafx.h"
#include <iostream>
#include <string>

using namespace std;

string sampleInputs[] = {
	"y qee",
	"ejp mysljylc kd kxveddknmc re jsicpdrysi",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv",
	"z" // only missing letter
};

string sampleOutputs[] = {
	"a zoo",
	"our language is impossible to understand",
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up",
	"q"
};


char convertLower(char c)
{
	for(int i=0; i<sizeof(sampleInputs)/sizeof(*sampleInputs); i++)
	{
		size_t pos = sampleInputs[i].find(c);
		if(pos != string::npos)
		{
			return sampleOutputs[i][pos];
		}
	}

	// Any other (non alphabetic) character => return itself
	return c;
}

char convert(char c)
{
	if('A' <= c && c <= 'Z')
		return toupper(convertLower(tolower(c)));
	else
		return convertLower(c);
}

string convert(string in)
{
	string out = in;

	for(unsigned i=0; i<in.length(); i++)
	{
		out[i] = convert(in[i]);
	}

	return out;
}

int main(int argc, char *argv[])
{
	int T;
	cin >> T;

	string line;
	getline(cin, line);

	for(int i=1; i <= T; i++)
	{
		getline(cin, line);
		cout << "Case #" << i << ": " << convert(line) << endl;
	}

	return 0;
}
