#include <cstdlib>
#include <iostream>
#include <map>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
	map<char, char> tl;
	tl['a']='y';
	tl['b']='h';
	tl['c']='e';
	tl['d']='s';
	tl['e']='o';
	tl['f']='c';
	tl['g']='v';
	tl['h']='x';
	tl['i']='d';
	tl['j']='u';
	tl['k']='i';
	tl['l']='g';
	tl['m']='l';
	tl['n']='b';
	tl['o']='k';
	tl['p']='r';
	tl['q']='z';
	tl['r']='t';
	tl['s']='n';
	tl['t']='w';
	tl['u']='j';
	tl['v']='p';
	tl['w']='f';
	tl['x']='m';
	tl['y']='a';
	tl['z']='q';
	tl[' ']=' ';
	int n;
	cin >> n;
		string s;
		getline(cin,s);
	for(int i=0;i<n;++i)
	{
		string s;
		getline(cin,s);
		for(int j=0;j<s.size();++j)
			s[j] = tl[s[j]];
		cout << "Case #" << i+1 << ": " << s << "\n";
	}
    return EXIT_SUCCESS;
}
