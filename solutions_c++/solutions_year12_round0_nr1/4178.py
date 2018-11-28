
#include <cstdio>
#include <iostream>
#include <fstream>

#include <algorithm>
#include <vector>
#include <map>
#include <stack>
#include <set>
#include <list>
#include <queue>
#include <string>

using namespace std;

ifstream file_in("input.txt");
ofstream file_out("output.txt");

void TestCase();

map<char, char> Mapping;

int main()
{
	int n;
	file_in >> n;

	string a = 
		(string)"ejp mysljylc kd kxveddknmc re jsicpdrysi" +
		"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd" +
		"de kr kd eoya kw aej tysr re ujdr lkgc jv";

	string b =
		(string)"our language is impossible to understand" +
		"there are twenty six factorial possibilities" +
		"so it is okay if you want to just give up";

	for (size_t i = 0; i < a.length(); i++)
	{
		Mapping[a[i]] = b[i];
	}

	Mapping['y'] = 'a';
	Mapping['e'] = 'o';
	Mapping['q'] = 'z';
	Mapping['z'] = 'q';

	for (int i = 1; i <= n; i++)
	{
		file_out << "Case #" << i << ": ";
		TestCase();
		file_out << endl;
	}
}

void TestCase()
{
	string input;
	while(input.length() == 0)
		getline(file_in, input);

	string output;
	for (size_t i = 0; i < input.length(); i++)
	{
		output.push_back(Mapping[input[i]]);
	}
	file_out << output;
}
