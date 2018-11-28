#include <iostream>
#include <map>
#include <string>
#include <fstream>
using namespace std;
int main()
{
	char charMap[128];
	charMap['a'] = 'y';
	charMap['b'] = 'h';
	charMap['c'] = 'e';
	charMap['d'] = 's';
	charMap['e'] = 'o';
	charMap['f'] = 'c';
	charMap['g'] = 'v';
	charMap['h'] = 'x';
	charMap['i'] = 'd';
	charMap['j'] = 'u';
	charMap['k'] = 'i';
	charMap['l'] = 'g';
	charMap['m'] = 'l';
	charMap['n'] = 'b';
	charMap['o'] = 'k';
	charMap['p'] = 'r';
	charMap['q'] = 'z';
	charMap['r'] = 't';
	charMap['s'] = 'n';
	charMap['t'] = 'w';
	charMap['u'] = 'j';
	charMap['v'] = 'p';
	charMap['w'] = 'f';
	charMap['x'] = 'm';
	charMap['y'] = 'a';
	charMap['z'] = 'q';
	charMap[' '] = ' ';
	int T;
	ifstream in("input.txt");
	ofstream out("output.txt");
	in>>T;
	int i,j;
	
	for(i=0;i<=T;i++)
	{

		string cur;
		string ret;
		getline(in,cur);
		if(i==0)
			continue;
		out<<"Case #"<<i<<": ";
		int n = cur.size();
		
		for(j=0;j<n;j++)
		{
			//const char* ch = cur.substr(j,1).c_str();
			char c = charMap[cur[j]];
			out<<charMap[cur[j]];
		}
		if(i!=0)
			out<<endl;
	}
	return 0;
}

