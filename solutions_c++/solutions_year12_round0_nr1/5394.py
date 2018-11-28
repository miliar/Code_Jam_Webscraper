#include<cstdio>
#include<iostream>
#include<map>
using namespace std;
int main()
{

	int T;
	char text[101];
	cin >> T;

	std::map<char, char> mDict;

	mDict['e'] = 'o';
	mDict['j'] = 'u';
	mDict['p'] = 'r';
	mDict['m'] = 'l';
	mDict['y'] = 'a';
	mDict['s'] = 'n';
	mDict['l'] = 'g';
	mDict['c'] = 'e';
	mDict['k'] = 'i';
	mDict['d'] = 's';
	mDict['x'] = 'm';
	mDict['v'] = 'p';

	mDict['n'] = 'b';
	mDict['r'] = 't';
	mDict['i'] = 'd';
	mDict['b'] = 'h';
	mDict['w'] = 'f';
	mDict['z'] = 'q';
	mDict['o'] = 'k';
	mDict['a'] = 'y';
	mDict['t'] = 'w';
	mDict['f'] = 'c';
	mDict['g'] = 'v';
	mDict['h'] = 'x';
	mDict['u'] = 'j';
	mDict['q'] = 'z';

	gets(text);

	for(int i=1; i <=T; i++){
		//cin >> text;
		gets(text);
		cout << "Case #" <<i<<": ";
		
		for( int j=0; j < strlen(text); j++){
			if( 'a' <= text[j] && text[j] <= 'z')
				cout << mDict[ text[j] ];
			else
				cout << text[j];
		}
		cout << std::endl;
	}
}