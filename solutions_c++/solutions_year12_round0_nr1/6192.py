#include <iostream>
#include <string>
#include <map>
#include <fstream>

using namespace std;

map<char, char> replacementMap;

void FillMap()
{
	replacementMap.insert(make_pair('e', 'o'));
	replacementMap.insert(make_pair('j', 'u'));
	replacementMap.insert(make_pair('p', 'r'));
	replacementMap.insert(make_pair('m', 'l'));
	replacementMap.insert(make_pair('y', 'a'));
	replacementMap.insert(make_pair('s', 'n'));
	replacementMap.insert(make_pair('l', 'g'));
	replacementMap.insert(make_pair('k', 'i'));
	replacementMap.insert(make_pair('d', 's'));
	replacementMap.insert(make_pair('x', 'm'));
	replacementMap.insert(make_pair('v', 'p'));
	replacementMap.insert(make_pair('n', 'b'));
	replacementMap.insert(make_pair('r', 't'));
	replacementMap.insert(make_pair('i', 'd'));
	replacementMap.insert(make_pair('t', 'w'));
	replacementMap.insert(make_pair('h', 'x'));
	replacementMap.insert(make_pair('g', 'v'));
	replacementMap.insert(make_pair('q', 'z'));
	replacementMap.insert(make_pair('c', 'e'));
	replacementMap.insert(make_pair('a', 'y'));
	replacementMap.insert(make_pair('o', 'k'));
	replacementMap.insert(make_pair('b', 'h'));
	replacementMap.insert(make_pair('w', 'f'));
	replacementMap.insert(make_pair('m', 'l'));
	replacementMap.insert(make_pair('u', 'j'));
	replacementMap.insert(make_pair('f', 'c'));
	replacementMap.insert(make_pair('z', 'q'));
}

char ReplaceCharacter(char x)
{
	return (replacementMap.find(x))->second;
}

void TranslateGooglerese(string& input)
{
	for(int i = 0; i < input.length(); ++i)
	{
		if(input[i] != ' ')
			input[i] = ReplaceCharacter(input[i]);
	}
}

int main()
{
	ifstream in("A-small-attempt1.in");
	ofstream out("output.txt");
	FillMap();
	string x;
	int n;
	in >> n;
	in.ignore();
	if(n > 0)
	{
		getline(in, x);
		TranslateGooglerese(x);
		out << "Case #1: " << x;
		for(int i = 2; i < n + 1; ++i)
		{
			getline(in, x);
			TranslateGooglerese(x);
			out << endl << "Case #" << i << ": " << x;
		}
	}
	return 0;
}