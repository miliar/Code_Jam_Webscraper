#include <iostream>
#include <map>
#include <string>

#include <stdio.h>

using namespace std;

int main(int argc, char *argv[])
{
    int testcases, i, j;
    scanf("%d", &testcases);
    cin.ignore();
    
    map<char, char> translation;
    translation['a'] = 'y';	translation['k'] = 'i';        translation['u'] = 'j';
    translation['b'] = 'h';	translation['l'] = 'g';        translation['v'] = 'p';
    translation['c'] = 'e';	translation['m'] = 'l';        translation['w'] = 'f';
    translation['d'] = 's';	translation['n'] = 'b';        translation['x'] = 'm';
    translation['e'] = 'o';	translation['o'] = 'k';        translation['y'] = 'a';
    translation['f'] = 'c';	translation['p'] = 'r';        translation['z'] = 'q';
    translation['g'] = 'v';	translation['q'] = 'z';	       translation[' '] = ' ';
    translation['h'] = 'x';	translation['r'] = 't';
    translation['i'] = 'd';	translation['s'] = 'n';
    translation['j'] = 'u';	translation['t'] = 'w';
    for( i = 1; i <= testcases; i++ )
    {
	string googlerese;
	getline(cin, googlerese);
	
	for( j = 0; j < googlerese.length(); j++ )
	{
	    if( googlerese[j] >= 'a' && googlerese[j] <= 'z' )
		googlerese[j] = translation[ googlerese[j] ];
	}
	cout<<"Case #"<<i<<": "<<googlerese<<endl;
    }
    
    return 0;
}