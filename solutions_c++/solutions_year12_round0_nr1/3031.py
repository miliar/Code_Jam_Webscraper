#include <map>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;
map<char, char> convertMap;

void Convert(string& text)
{
	for(int i = 0; i != text.size(); i++)
	{
		if (text[i] == ' ')
			continue;
		text[i] = convertMap[text[i]];
	}
}

void initConvert()
{

	convertMap['a'] = 'y';
	convertMap['b'] = 'h';
	convertMap['c'] = 'e';
	convertMap['d'] = 's';
	convertMap['e'] = 'o';
	convertMap['f'] = 'c';
	convertMap['g'] = 'v';
	convertMap['h'] = 'x';
	convertMap['i'] = 'd';
	convertMap['j'] = 'u';
	convertMap['k'] = 'i';
	convertMap['l'] = 'g';
	convertMap['m'] = 'l';
	convertMap['n'] = 'b';
	convertMap['o'] = 'k';
	convertMap['p'] = 'r';
	convertMap['q'] = 'z';
	convertMap['r'] = 't';
	convertMap['s'] = 'n';
	convertMap['t'] = 'w';
	convertMap['u'] = 'j';
	convertMap['v'] = 'p';
	convertMap['w'] = 'f';
	convertMap['x'] = 'm';
	convertMap['y'] = 'a';
	convertMap['z'] = 'q';
}

int main()
{
	initConvert();
	ifstream input("c:\\small.in");
	ofstream output("c:\\output.txt");

	int n;

	input >> n;

	string text;

	getline(input, text);
	text.clear();


	char msg[1000];
	for (int i = 1 ; i<=n ; i++)
	{
		string temp = "Case #";

		itoa(i, msg, 10);
		temp += msg;
		temp += ": ";

		getline(input, text);
		Convert(text);
		text += '\n';
		output << temp;
		output << text;
		text.clear();
	}

	output.close();
	input.close();
}

