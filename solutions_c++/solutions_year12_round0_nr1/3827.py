/*
 * driver.cpp
 *
 *  Created on: Apr 13, 2012
 *      Author: crand6
 */
#include <iostream>
#include <map>
#include <string>
#include <fstream>
using namespace std;

int main()
{

	map<char, char> decoder;
	decoder.insert(pair<char, char>('y', 'a'));
	decoder.insert(pair<char, char>('q', 'z'));
	decoder.insert(pair<char, char>('e', 'o'));
	decoder.insert(pair<char, char>(' ', ' '));
	decoder.insert(pair<char, char>('j', 'u'));
	decoder.insert(pair<char, char>('p', 'r'));
	decoder.insert(pair<char, char>('m', 'l'));
	decoder.insert(pair<char, char>('s', 'n'));
	decoder.insert(pair<char, char>('l', 'g'));
	decoder.insert(pair<char, char>('a', 'y'));
	decoder.insert(pair<char, char>('c', 'e'));
	decoder.insert(pair<char, char>('k', 'i'));
	decoder.insert(pair<char, char>('d', 's'));
	decoder.insert(pair<char, char>('a', 'y'));
	decoder.insert(pair<char, char>('x', 'm'));
	decoder.insert(pair<char, char>('v', 'p'));
	decoder.insert(pair<char, char>('a', 'y'));
	decoder.insert(pair<char, char>('n', 'b'));
	decoder.insert(pair<char, char>('r', 't'));
	decoder.insert(pair<char, char>('i', 'd'));
	decoder.insert(pair<char, char>('b', 'h'));
	decoder.insert(pair<char, char>('t', 'w'));
	decoder.insert(pair<char, char>('h', 'x'));
	decoder.insert(pair<char, char>('w', 'f'));
	decoder.insert(pair<char, char>('f', 'c'));
	decoder.insert(pair<char, char>('o', 'k'));
	decoder.insert(pair<char, char>('u', 'j'));
	decoder.insert(pair<char, char>('g', 'v'));
	decoder.insert(pair<char, char>('z', 'q'));

	string input;
	ifstream inFile("A-small-attempt1.in");
	int lineNum;
	inFile >> lineNum;
	//get rid of newline
	inFile.ignore();

	ofstream outFile("attempt1.out");
	//cout << decoder.size() << endl;

	for(int x = 0; x < lineNum; x++)
	{
		outFile << "Case #" << x + 1 << ": ";
		getline(inFile, input);

		for(int i = 0; i < input.length(); i++)
		{
			map<char, char>::iterator it = decoder.find(input[i]);
			if(it == decoder.end())
			{
				outFile << "?";
				continue;
			}
			outFile << it->second;
		}

		outFile << endl;
	}
	cout << "done";
	return 0;
}
