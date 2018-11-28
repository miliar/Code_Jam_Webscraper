#include <fstream>
#include <iostream>
#include <string>
#include "pattern.h"

using std::string;
using std::cout;
using std::endl;
using std::ifstream;
using std::ofstream;

int main(int argc, char **argv)
{
#ifdef CMD_TEST
	string s = argv[1];
	pattern p(argv[2]);

	p.print();

	if (p.match(s)) cout << "YES!" << endl;
	else cout << "NO!" << endl;
#else
	ifstream infile(argv[1]);
	ofstream outfile(argv[2]);

	list<string> words;
	list<pattern> patterns;

	int l;
	int d;
	int n;
	string s;

	infile >> l;
	infile >> d;
	infile >> n;

	for (int i = 0; i < d; i++)
	{
		infile >> s;
		words.push_back(s);
	}

	for (int i = 0; i < n; i++)
	{
		infile >> s;
		//patterns.push_back(pattern(s));
		pattern p(s);
		int matchnum = 0;

		for (list<string>::iterator wi = words.begin(); wi != words.end(); wi++)
		{
			matchnum += p.match(*wi);
		}
		
		outfile << "Case #" << i + 1 << ": " << matchnum << endl;
	}
#endif
}
