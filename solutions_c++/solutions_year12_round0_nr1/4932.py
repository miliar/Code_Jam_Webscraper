#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<sstream>
#include<istream>
#include<fstream>
using namespace std;

map<char,char> ar;
void init()
{
	ar['y'] = 'a';
	ar['n'] = 'b';
	ar['f'] = 'c';
	ar['i'] = 'd';
	ar['c'] = 'e';
	ar['w'] = 'f';
	ar['l'] = 'g';
	ar['b'] = 'h';
	ar['k'] = 'i';
	ar['u'] = 'j';
	ar['o'] = 'k';
	ar['m'] = 'l';
	ar['x'] = 'm';
	ar['s'] = 'n';
	ar['e'] = 'o';
	ar['v'] = 'p';
	ar['z'] = 'q';
	ar['p'] = 'r';
	ar['d'] = 's';
	ar['r'] = 't';
	ar['j'] = 'u';
	ar['g'] = 'v';
	ar['t'] = 'w';
	ar['h'] = 'x';
	ar['a'] = 'y';
	ar['q'] = 'z';
}

int main()
{
	init();
	int t;
	ifstream fs ( "A-small-attempt1.in" , ifstream::in );
	ofstream os;
	os.open("A-small-attempt1.out");
	string text;
	stringstream ss;
	getline(fs,text);
	ss << text;
	ss >> t;
	for(int i=0;i<t;++i)
	{
		string translated="";
		cin.clear();
		getline(fs,text);
		for(int j=0;j<text.length();++j)
		{
			if(text[j] == ' ')
				translated+=text[j];
			else
				translated+=ar[text[j]];
		}
	
		os << "Case #" << i+1 << ": " << translated << endl;
	}
	return 0;
}