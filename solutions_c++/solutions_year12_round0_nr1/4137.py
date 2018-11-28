#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<math.h>
#include<set>
#include<vector>
#include<string.h>
#include<string>
#include<map>
using namespace std;

int main()
{
#ifdef _DEBUG
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
#endif

	int n;
	cin >> n;

	map<char,char>m;

	m['a']  = 'y';
	m['b']  = 'h';
	m['c']  = 'e';
	m['d']  = 's';
	m['e']  = 'o';
	m['f']  = 'c';
	m['g']  = 'v';
	m['h']  = 'x';
	m['i']  = 'd';
	m['j']  = 'u';
	m['k']  = 'i';
	m['l']  = 'g';
	m['m']  = 'l';
	m['n']  = 'b';
	m['o']  = 'k';
	m['p']  = 'r';
	m['q']  = 'z';
	m['r']  = 't';
	m['s']  = 'n';
	m['t']  = 'w';
	m['u']  = 'j';
	m['v']  = 'p';
	m['w']  = 'f';
	m['x']  = 'm';
	m['y']  = 'a';
	m['z']  = 'q';

	char buff[256];

	cin.getline(buff,256);

	for (int i=0; i<n; i++)
	{
		cin.getline(buff,256);
		int l = strlen(buff);
		cout << "Case #" << i+1 << ": ";
		for (int i=0; i<l; i++)
			cout << ((buff[i] == ' ') ? ' ' : m[buff[i]]);
		cout << endl;
	}


	return 0;
}

// q <-> z