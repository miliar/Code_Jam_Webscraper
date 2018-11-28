#include <map>
#include <iostream>
#include <string>
#include <cstdio>
using namespace std;

int main()
{
	char s[120];
	map < char, char > m;
	m['a'] = 'y';
	m['b'] = 'h';
	m['c'] = 'e';
	m['d'] = 's';
	m['e'] = 'o';
	m['f'] = 'c';
	m['g'] = 'v';
	m['h'] = 'x';
	m['i'] = 'd';
	m['j'] = 'u';
	m['k'] = 'i';
	m['l'] = 'g';
	m['m'] = 'l';
	m['n'] = 'b';
	m['o'] = 'k';
	m['p'] = 'r';
	m['q'] = 'z';
	m['r'] = 't';
	m['s'] = 'n';
	m['t'] = 'w';
	m['u'] = 'j';
	m['v'] = 'p';
	m['w'] = 'f';
	m['x'] = 'm';
	m['y'] = 'a';
	m['z'] = 'q';
	m[' '] = ' ';
	freopen("input.txt","r",stdin);
	freopen("output.txt", "w",stdout);
	int n;
	cin>>n;
	getchar();
	for( int i = 1; i <= n; i++ )
	{
		gets(s);
				
		cout << "Case #" << i << ": ";
		for( int j = 0; j < strlen(s); j++ )
		{
			cout<<m[ s[j] ];
		}
		if( i != n )
		cout<<endl;
	}
	
}