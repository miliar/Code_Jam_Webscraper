// gcj2010.cpp : Defines the entry point for the console application.
//

#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

void tokenizer(const string& str,
			  vector<string>& tokens,
			  const string& delimiters = " ")
{
	// Skip delimiters at beginning.
	string::size_type lastPos = str.find_first_not_of(delimiters, 0);
	// Find first "non-delimiter".
	string::size_type pos     = str.find_first_of(delimiters, lastPos);

	while (string::npos != pos || string::npos != lastPos)
	{
		// Found a token, add it to the vector.
		tokens.push_back(str.substr(lastPos, pos - lastPos));
		// Skip delimiters.  Note the "not_of"
		lastPos = str.find_first_not_of(delimiters, pos);
		// Find next "non-delimiter"
		pos = str.find_first_of(delimiters, lastPos);
	}
}

vector<string> p;
vector<string> q;
int c = 0;

bool exists(string path) {
	for (int i = 0; i < p.size(); i++) {
		if (p.at(i) == path)
			return true;
	}

	return false;
}

void process(string s) {
	for (int i = 1; i < s.length(); i++) {
		if (s.at(i) == '/') {
			string t = s.substr(0, i);
			if (!exists(t)) {
				c++;
				p.push_back(t);
			}
		}
	}

	if (!exists(s)) {
		c++;
		p.push_back(s);
	}
}

int main(int argc, char* argv[])
{
	// Read input
	FILE* f = fopen("A-small-attempt2.in", "r");
	FILE* fOut = fopen("output.txt", "w");

	unsigned int nCases, n1, n2;
	fscanf(f, "%i", &nCases);
	for (unsigned int iCase = 0; iCase < nCases; iCase++) {
		printf("Processing case #%i\n", iCase + 1);

		p.clear();
		p.push_back(string(""));
		c = 0;

		fscanf(f, "%i %i", &n1, &n2);
		for (int i = 0; i < n1; i++) {
			char s[200];
			fscanf(f, "%s", s);
			p.push_back(string(s));
		}

		for (int i = 0; i < n2; i++) {
			char bs[200];
			fscanf(f, "%s", bs);
			string s(bs);
			process(s);
		}
		
		fprintf(fOut, "Case #%i: %i\n", iCase + 1, c);
		fflush(fOut);
	}

	fclose(f);
	fclose(fOut);

	return 0;
}

