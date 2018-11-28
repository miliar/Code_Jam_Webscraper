#include <iostream>
#include <fstream>
#include <map>
#include <exception>
using namespace std;

template<class Key, class T>
map<Key, T> MakeMap(Key keys[], T data[], size_t size) // Returns a map with keys[] and their data[]
{
	map<Key, T> retnMap;
	try
	{
		for(int n = 0; n < size; ++n)
		{
			retnMap[keys[n]] = data[n];
		}
	}
	catch(exception& e)
	{
		cout << "Can't make the map: " << e.what() << endl;
	}

	return retnMap;
}

string GtoE(const string& Googlerese, map<char, char>& dict) // Translates from Googlerese to English using dict(ionary)
{
	string En("");
	for(int n = 0; n < Googlerese.length(); ++n)
	{
		if(Googlerese[n] >= 'a' && Googlerese[n] <= 'z') // If a letter between a-z
		{
			En += dict[Googlerese[n]];
		}
		else
		{
			En += Googlerese[n];
		}
	}

	return En;
}

char EnglishAlphabet[26] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};

char GooglereseAlphabet[26] = {'y', 'n', 'f', 'i', 'c', 'w', 'l', 'b', 'k', 'u',
'o', 'm', 'x', 's', 'e', 'v', 'z', 'p', 'd', 'r', 'j', 'g', 't', 'h', 'a', 'q'};

int main()
{
	map<char, char> Dictionary = MakeMap(GooglereseAlphabet, EnglishAlphabet, 26); // Translates from G to E
	unsigned short noCases;
	string Line; // Used for reading lines

	ifstream in("input.in");
	ofstream out("output.out");

	if(!in || !out)
	{
		cout << "Can't open input or output file!" << endl;
		return 1;
	}

	in >> noCases;
	getline(in, Line); // Gets the '\n' character after the number of cases

	for(int n = 0; n < noCases; ++n)
	{
		getline(in, Line);
		Line = GtoE(Line, Dictionary);
		out << "Case #" << n+1 << ": " << Line << endl;
	}

	return 0;
}
