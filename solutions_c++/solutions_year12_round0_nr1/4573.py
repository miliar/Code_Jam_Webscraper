#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>

using namespace std;

int main()
{
	int n;
	string str;

	cin >> n;
	getline( cin, str );

	for ( int i = 0; i < n; i++ )
	{
		getline( cin, str );
		
		cout << "Case #" << i + 1 << ": ";

		for ( unsigned int j = 0; j < str.length(); j++ )
		{
			char c = str[j];

			switch ( c )
			{
			case 'y':
				c = 'a';
				break;
			case 'n':
				c = 'b';
				break;
			case 'f':
				c = 'c';
				break;
			case 'i':
				c = 'd';
				break;
			case 'c':
				c = 'e';
				break;
			case 'w':
				c = 'f';
				break;
			case 'l':
				c = 'g';
				break;
			case 'b':
				c = 'h';
				break;
			case 'k':
				c = 'i';
				break;
			case 'u':
				c = 'j';
				break;
			case 'o':
				c = 'k';
				break;
			case 'm':
				c = 'l';
				break;
			case 'x':
				c = 'm';
				break;
			case 's':
				c = 'n';
				break;
			case 'e':
				c = 'o';
				break;
			case 'v':
				c = 'p';
				break;
			case 'z':
				c = 'q';
				break;
			case 'p':
				c = 'r';
				break;
			case 'd':
				c = 's';
				break;
			case 'r':
				c = 't';
				break;
			case 'j':
				c = 'u';
				break;
			case 'g':
				c = 'v';
				break;
			case 't':
				c = 'w';
				break;
			case 'h':
				c = 'x';
				break;
			case 'a':
				c = 'y';
				break;
			case 'q':
				c = 'z';
				break;
			}

			cout << c;
		}

		cout << endl;
	}

	return 0;
}