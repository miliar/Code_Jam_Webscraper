#include<fstream>
#include<string>
#include<algorithm>
#include<map>
#include<vector>
#include<iomanip>

using namespace std;


int main()
{
	ifstream cin("in.txt");
	ofstream cout("out.txt");
	int t;
	cin>>t;
	string s;
	getline(cin, s);
	for(int tt=0; tt<t; tt++)
	{
		getline(cin, s);
		map<char, char> m;
		m[' '] = ' ';
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
		for(int i=0; i<s.length(); i++)
			s[i] = m[s[i]];
		cout<<"Case #"<<tt+1<<": "<<s<<endl;
	}
	return 0;
}