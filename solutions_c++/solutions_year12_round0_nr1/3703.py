#include <iostream>
#include <fstream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

string to, from;
bool used[256];
char encoding[256];

int main()
{
	ifstream key("key.txt");
	int keys;
	key >> keys;
	getline(key, to);

	for (int i = 0; i < keys; i++)
	{
		getline(key, from);
		getline(key, to);
		for (int i = 0; i < from.length(); i++)
			encoding[ from[i] ] = to[i],
			used[ to[i] ] = true;
	}
	encoding['z'] = 'q';
	used['q'] = true;

	for (char c = 'a'; c <= 'z'; c++)
		if (!used[c])
		{
			encoding['q'] = c;
			used[c] = true;
			break;
		}

	for (char i = 'a'; i <= 'z'; i++)
		cout << i << " -> " << encoding[i] << endl;

	key.close();

	ifstream fi("A-small-attempt0.in");
	ofstream fo("output.txt");

	fi >> keys;
	getline(fi, from);

	for (int i = 0; i < keys; i++)
	{
		getline(fi, from);
		fo << "Case #" << i + 1 << ": ";
		for (int j = 0; j < from.length(); j++)
			fo << encoding[ from[j] ];
		fo << endl;
	}

	return 0;
}