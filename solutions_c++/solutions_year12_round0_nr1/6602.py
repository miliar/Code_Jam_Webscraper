#include <iostream>
#include <utility>
#include <map>
#include <vector>
#include <algorithm>
#include <string>
#include <fstream>

#include "winapi_file.h"

using namespace std;

typedef unsigned int uint;
typedef vector<char> CharSet;

void ParseInputFile(MemoryMap& mm, CharSet& ip); //let ip := input
bool ParseMapCode(string& s, char& a, char& b);

class DeScrambler
{
public:

	DeScrambler(CharSet& input) : in(input) 
	{
		Init();
	}

	DeScrambler(CharSet& input, CharSet& output) : in(input), out(output)
	{
		Init();
	}

	void Init()
	{
		for ( uint i = 0; i < 26; ++i)
		{
			char index = 'a' + char(i);
			m[index] = '?';
		}
	}
	void push_back(char a, char b)
	{
		m[a] = b;
	}

	// display current mapping a -> b
	void DisplayCurrentMapping()
	{
		CharMap::iterator it;

		for( it = m.begin(); it != m.end(); ++it ) {
			cout << it->first << " ";
		}

		cout << endl;

		for( it = m.begin(); it != m.end(); ++it ) {
			cout << it->second << " ";
		}

		cout << endl;
	}

	void DisplayImage()
	{
		int lineCount = 0;

		for ( CharSet::iterator it = in.begin(); (it != in.end()) && (lineCount < 5); ++it)
		{
			char c = *it;
			if (c == '\n')
				lineCount++;

			if ( (c == ' ') || (c == '\n'))
			{
				cout << c;
			}
			else
				cout << m[c];
		}
	}

	void DisplayDomain()
	{
		int lineCount = 0;
		for ( CharSet::iterator it = in.begin(); (it != in.end()) && (lineCount < 5); ++it)
		{
			char c = *it;
			if (c == '\n')
				lineCount++;

			cout << *it;
		}
	}

	void WriteImage()
	{
		uint caseNumber = 1;

		ofstream fout ("output.txt");
		fout << "Case #" << caseNumber++ << ": ";
		for ( CharSet::iterator it = in.begin(); it != in.end(); ++it)
		{
			char c = *it;
			if ( (c == ' ') || (c == '\n'))
			{
				if ( c == '\n')
					fout << (char)0xa;
				else
					fout << c;

				if ( c == '\n') 
					fout << "Case #" << caseNumber++ << ": ";
			}
			else
				fout << m[c];
		}

		fout.close();

		ifstream file("output.txt",std::ios::binary|std::ios::ate);
		vector<char> buffer(file.tellg());
		file.seekg(0);
		file.read(&buffer[0],buffer.size());

		// prune all '0xd';
		remove(buffer.begin(), buffer.end(), (char)0xd);
		

		std::ofstream ofile("output.txt.temp",std::ios::binary);
		ofile.write(&buffer[0],buffer.size());
	}

	// descramble using our mapping a -> b
	void DeScramble(CharSet& input)
	{
		
	}
	
private:
	typedef map<char, char> CharMap;
	CharMap m; // let m contain the mappings between Googlerese and the english alphabet.
	CharSet in, out;
};

int main()
{

	// load input file
	CharSet input;
	MemoryMap mm(MMAP_FILEMAP, "input.txt", MMAP_READ, 0);
	ParseInputFile(mm, input);

	cout << "\n\n" << endl;

	DeScrambler ds(input);
	
	// set up hint
	ds.push_back('a', 'y'); ds.push_back('o', 'k'); ds.push_back('z', 'q');
	ds.push_back('e', 'o'); ds.push_back('j', 'u'); ds.push_back('p', 'r');
	ds.push_back('m', 'l'); ds.push_back('y', 'a'); ds.push_back('s', 'n');
	ds.push_back('l', 'g'); ds.push_back('j', 'u'); ds.push_back('c', 'e');
	ds.push_back('k', 'i'); ds.push_back('d', 's'); ds.push_back('x', 'm');
	ds.push_back('v', 'p'); ds.push_back('n', 'b'); ds.push_back('r', 't');
	ds.push_back('b', 'h'); ds.push_back('i', 'd'); ds.push_back('h', 'x');
	ds.push_back('t', 'w'); ds.push_back('w', 'f'); ds.push_back('f', 'c');
	ds.push_back('u', 'j'); ds.push_back('g', 'v'); ds.push_back('q', 'z');
	
	while (1)
	{
		// begin guessing routine, goal is to figure out a word or two then move up.
		ds.DisplayCurrentMapping();
		cout << "\n" << endl;

		ds.DisplayDomain();
		cout << "\n" << endl;

		ds.DisplayImage();
		cout << "\n\n" << endl;

		string s;
		getline(cin,s);

		if (cin.good())
		{
			if ( s == "exit" )
				break;

			char a, b;
		
			if ( ParseMapCode(s, a, b) )
			{
				ds.push_back(a, b);
			}

			system("cls");
		}
		else
		{
			cin.clear();
			cout << "Incorrect input..." << endl;
			cin.ignore(10, '\n');
		}
	}	

	ds.WriteImage();

	system("pause");

}

void ParseInputFile(MemoryMap& mm, CharSet& ip)
{
	// file looks like
	// T
	// T input# ....

	char* p = (char*)mm.m_FileMapPtr; // let p := file pointer.

	// how many lines to read in ?
	uint T = 30;/* lexical_cast<uint>(*p); */p+=2; // let T := as the input size ( in lines of text )

	if (!SkipNewLine(p)) // file structure requies we skip a line after reading in T.
		__asm int 13;

	for ( uint line = 0; line < T ; )
	{
		if ( IsNewLine(p) ) {
			++line;
			ip.push_back(*p); ++p; // push back '\n'
			continue;
		}
		else
		{
			ip.push_back(*p);
		}

		++p;
	}

	for (uint i = 0; i < ip.size(); ++i) 
	{
		cout << ip[i];
	}
	cout << "\n" << endl;


	//cout << ip.size() << " =?= " << op.size() << endl;
}

bool ParseMapCode(string& s, char& a, char& b)
{
	a = b = '?';

	string::iterator it = s.begin();

	for (; it != s.end(); ++it)
	{
		char c = *it;

		if ( isalpha(c) && islower(c) ) {
			a = c;
			break;
		}
	}

	if ( a == '?')
		return false;

	for (; it != s.end(); ++it)
	{
		char c = *it;

		if ( ( isalpha(c) && islower(c) ) || c == '?')
			b = c;
	}

	return true;
}
