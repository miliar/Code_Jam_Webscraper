/**
	Written by Gaurav Ahuja
	gauravahuja9@gmail.com
**/


#include <iostream>
#include <cstdio>

namespace IO
{
	const int SIZE = 1 << 20;
	char buff[SIZE], *p = buff + SIZE;

	inline char read_char()
	{
	    if( p == buff + SIZE )
	    {
	        fread( buff, 1, SIZE, stdin );
	        p = buff;
	    }
	    return *(p++);
	}

	inline int read_int()
	{
	    char c;
	
	    while( !isdigit( c = read_char() ) );
	
	    int r = c-'0';
	    while( isdigit( c = read_char() ) ) r = 10*r + c - '0';

	    return r;
	}
}

using namespace IO;
using namespace std;

int main()
{
	int t, td = 1;
	int Map[26];
	Map['a' - 'a'] = 'y';
	Map['b' - 'a'] = 'h';
	Map['c' - 'a'] = 'e';
	Map['d' - 'a'] = 's';
	Map['e' - 'a'] = 'o';
	Map['f' - 'a'] = 'c';
	Map['g' - 'a'] = 'v';
	Map['h' - 'a'] = 'x';
	Map['i' - 'a'] = 'd';
	Map['j' - 'a'] = 'u';
	Map['k' - 'a'] = 'i';
	Map['l' - 'a'] = 'g';
	Map['m' - 'a'] = 'l';
	Map['n' - 'a'] = 'b';
	Map['o' - 'a'] = 'k';
	Map['p' - 'a'] = 'r';
	Map['q' - 'a'] = 'z';
	Map['r' - 'a'] = 't';
	Map['s' - 'a'] = 'n';
	Map['t' - 'a'] = 'w';
	Map['u' - 'a'] = 'j';
	Map['v' - 'a'] = 'p';
	Map['w' - 'a'] = 'f';
	Map['x' - 'a'] = 'm';
	Map['y' - 'a'] = 'a';
	Map['z' - 'a'] = 'q';
	
	t = read_int();
	char temp;
	while(td <= t)
	{
		printf("Case #%d: ", td);
		
		temp = read_char();
		while(temp != '\n')
		{
			if(temp == ' ')
				printf(" ");
			else
				printf("%c", Map[temp - 'a']);
			temp = read_char();
		}
		printf("\n");
		td++;

	}
	
	return 0;
}
