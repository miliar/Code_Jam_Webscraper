#include <iostream>
#include <fstream>
#include <string>

using namespace std;
char code(char);
void main()
{
	string infile, outfile, line;
	ifstream source;
	ofstream target;
	int T;
	char c;
	int l;
	int j;


    cout << " Please, enter the INPUT file name" << endl;
    cin >> infile;
   cout << " Please, enter the OUTPUT file name" << endl;
    cin >> outfile;
	source.open(infile.c_str());
	target.open(outfile.c_str());
	if (source.fail())
	{
		cout <<"failed" << endl;
	}

	source >> T;
	cout << " the number of cases is " << T <<endl;
	source.get(c);

		for ( int i = 1; i <=T; i++)
		{
			j =0;
			target <<"Case #" << i << ": ";
			getline(source,line);
			l = line.length();
			while( j < l)
			{
				c = line.at(j);
				j++;
				if (!( (c == ' ') || (c == '/n') ))
					{
						target.put(code(c));
					
					}
				else
					if (c == ' ')
						target.put(c);
			}
			target << endl;
		}	
	}

	
char code ( char c)
{
	switch (c)
	{
		case 'a':
			return 'y';
		case 'b':
			return 'h';
		case 'c':
			return 'e';
		case 'd':
			return 's';
		case 'e':
			return 'o';
		case 'f':
			return 'c';
		case 'g':
			return 'v';
		case 'h':
			return 'x';
		case 'i':
			return 'd';
		case 'j':
			return 'u';
		case 'k':
			return 'i';
		case 'l':
			return 'g';
		case 'm':
			return 'l';
		case 'n':
			return 'b';
		case 'o':
			return 'k';
		case 'p':
			return 'r';
		case 'q':
			return 'z';
		case 'r':
			return 't';
		case 's':
			return 'n';
		case 't':
			return 'w';
		case 'u':
			return 'j';
		case 'v':
			return 'p';
		case 'w':
			return 'f';
		case 'x':
			return 'm';
		case 'y':
			return 'a';
		case 'z':
			return 'q';
	}
	}