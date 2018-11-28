#include <iostream>
#include <cstdio>
#include <map>
#include <string>

using namespace std;

int t;
map <char,char> M;
string S,G;
char s[200];
int main()
{
	freopen("file.in","r",stdin);
	freopen("file.out","w",stdout);
	M['a'] = 'y'; M['b'] = 'h'; M['c'] = 'e'; M['d'] = 's'; M['e'] = 'o';
	M['f'] = 'c'; M['g'] = 'v'; M['h'] = 'x'; M['i'] = 'd'; M['j'] = 'u'; 
	M['k'] = 'i'; M['l'] = 'g'; M['m'] = 'l'; M['n'] = 'b'; M['o'] = 'k';
	M['p'] = 'r'; M['q'] = 'z'; M['r'] = 't'; M['s'] = 'n';	M['t'] = 'w';
	M['u'] = 'j'; M['v'] = 'p'; M['w'] = 'f'; M['x'] = 'm'; M['y'] = 'a'; 
	M['z'] = 'q'; M[' '] = ' ';
	scanf("%d\n",&t);
	for(int k=1;k<=t;k++)
	{
		gets(s);
		G = string(s);
		S = "";
		for(int i=0;i<G.length();i++)
			S += M[G[i]];
		cout<<"Case #"<<k<<": "<<S<<endl;
	}
	return 0;
}