#include <iostream>
#include <string>
using namespace std ;

char trans[1100];

int main()
{
	trans['a'] = 'y' ;
	trans['b'] = 'h' ;
	trans['c'] = 'e' ;
	trans['d'] = 's' ;
	trans['e'] = 'o' ;
	trans['f'] = 'c' ;
	trans['g'] = 'v' ;
	trans['h'] = 'x' ;
	trans['i'] = 'd' ;
	trans['j'] = 'u' ;
	trans['k'] = 'i' ;
	trans['l'] = 'g' ;
	trans['m'] = 'l' ;
	trans['n'] = 'b' ;
	trans['o'] = 'k' ;
	trans['p'] = 'r' ;
	trans['q'] = 'z' ;
	trans['r'] = 't' ;
	trans['s'] = 'n' ;
	trans['t'] = 'w' ;
	trans['u'] = 'j' ;
	trans['v'] = 'p' ;
	trans['w'] = 'f' ;
	trans['x'] = 'm' ;
	trans['y'] = 'a' ;
	trans['z'] = 'q' ;
	trans[' '] = ' ' ;
	
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int cas ;
	cin >> cas ;
	string s ;
	scanf("\n");
	for(int i=1;i<=cas;i++)
	{
		cout << "Case #" << i << ": "  ;
		getline(cin,s);
		for(int j=0;j<s.size();j++)
		{
			cout << trans[int(s[j])] ;
		}
		cout << endl ;
	}	
}
