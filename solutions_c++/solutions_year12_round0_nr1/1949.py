// Google CodeJAM 2012
// Author: Syed Ghulam Akbar

#define _CRT_SECURE_NO_WARNINGS
#define _CRT_NONSTDC_NO_DEPRECATE

#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
#include <sstream>
#include <math.h>

using namespace std;
char char_map[250];

void createmap(string src, string des)
{
	for (int i=0; i < src.length(); i++)
		char_map[src[i]]=des[i];
}

int main() {
	int C;
	char source_lin[500];

	FILE *in = freopen( "Debug\\input.txt", "r", stdin );
	FILE *out = freopen( "Debug\\output.txt", "w", stdout );

	// create the start-up example map
	createmap("abcdefghijklmnopzrstuvwxyq","abcdefghijklmnopqrstuvwxyz");
	createmap("ejp mysljylc kd kxveddknmc re jsicpdrysi","our language is impossible to understand");
	createmap("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","there are twenty six factorial possibilities");
	createmap("de kr kd eoya kw aej tysr re ujdr lkgc jv","so it is okay if you want to just give up");

	scanf("%d",&C);
	cin.ignore();

	string input;
	string output("");

	for (int test=1;test<=C;test++) {
		getline(cin, input);
		output = "";

		for (int i=0; i<input.length(); i++)
		{
			if (char_map[input[i]] != 0)
				output += char_map[input[i]];
		}

		// Set the answer depending on the found state
		cout << "Case #" << test << ": " << output << endl;
	}

	fclose( out );
}