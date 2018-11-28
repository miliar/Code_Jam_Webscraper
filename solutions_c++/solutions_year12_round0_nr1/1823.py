#include <vector>
#include <string>
#include <map>
#include <stdio.h>
using namespace std;

string getLine()
{
	string ret = "";
	while(true){
		char ch = getchar();
		if(ch == -1 || ch == '\n') break;
		if(ch == '\r') continue;
		ret += ch;
	}
	return ret;
}

map<char,char> alp;

int main()
{
	alp[' '] = ' ';
	alp['y'] = 'a';
	alp['n'] = 'b';
	alp['f'] = 'c';
	alp['i'] = 'd';
	alp['c'] = 'e';
	alp['w'] = 'f';
	alp['l'] = 'g';
	alp['b'] = 'h';
	alp['k'] = 'i';
	alp['u'] = 'j';
	alp['o'] = 'k';
	alp['m'] = 'l';
	alp['x'] = 'm';
	alp['s'] = 'n';
	alp['e'] = 'o';
	alp['v'] = 'p';
	alp['z'] = 'q';
	alp['p'] = 'r';
	alp['d'] = 's';
	alp['r'] = 't';
	alp['j'] = 'u';
	alp['g'] = 'v';
	alp['t'] = 'w';
	alp['h'] = 'x';
	alp['a'] = 'y';
	alp['q'] = 'z';

	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int n = stoi(getLine());
	for(int i=0;i<n;++i){
		string origin = getLine();
		string next;
		for(int i=0;i<origin.size();++i){
			next += alp[origin[i]];
		}
		printf("Case #%d: %s\n",i+1, next.c_str());
	}
	return 0;
}