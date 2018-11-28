#include <stdio.h>
#include <iostream>
using namespace std;




int main()
{
    char map[128];
  /*  map['a'] = 'y';
    map['b'] = 'n';
    map['c'] = 'f';
    map['d'] = 'i';
    map['e'] = 'c';
    map['f'] = 'w';
    map['g'] = 'l';
    map['h'] = 'b';
    map['i'] = 'k';
    map['j'] = 'u';
    map['k'] = 'o';
    map['l'] = 'm';
    map['m'] = 'x';
    map['n'] = 's';
    map['o'] = 'e';
    map['p'] = 'v';
    map['q'] = 'z';
    map['r'] = 'p';
    map['s'] = 'd';
    map['t'] = 'r';
    map['u'] = 'j';
    map['v'] = 'g';
    map['w'] = 't';
    map['x'] = 'h';
    map['y'] = 'a';
    map['z'] = 'q';*/

    map['a'] = 'y';
    map['b'] = 'h';
    map['c'] = 'e';
    map['d'] = 's';
    map['e'] = 'o';
    map['f'] = 'c';
    map['g'] = 'v';
    map['h'] = 'x';
    map['i'] = 'd';
    map['j'] = 'u';
    map['k'] = 'i';
    map['l'] = 'g';
    map['m'] = 'l';
    map['n'] = 'b';
    map['o'] = 'k';
    map['p'] = 'r';
    map['q'] = 'z';
    map['r'] = 't';
    map['s'] = 'n';
    map['t'] = 'w';
    map['u'] = 'j';
    map['v'] = 'p';
    map['w'] = 'f';
    map['x'] = 'm';
    map['y'] = 'a';
    map['z'] = 'q';
    map[' '] = ' ';
    map['.'] = '.';
    map['?'] = '?';
    map['!'] = '!';
    map[','] = ',';
    map[':'] = ':';
    

    
    char line[200];
    int T;
    cin >> T;
    cin.get();

    for (int i = 0 ; i < T ; i++)
    {
	cin.getline(line,200);
	printf("Case #%d: ",i+1);
	int pos = 0;
	char ch;
	while (true)
	{
	    ch = line[pos++];
	    if (ch)
	    {
		printf("%c", map[ch]);
	    }
	    else
		break;
	}
	printf("\n");
    }
    
    return 0;
}
