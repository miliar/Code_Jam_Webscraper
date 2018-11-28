#include <iostream>
#include <map>
#include <stdio.h>
using namespace std;

map<char,char> m_data;

int main()
{
	m_data['a'] = 'y';
	m_data['b'] = 'h';
	m_data['c'] = 'e';
	m_data['d'] = 's';
	m_data['e'] = 'o';
	m_data['f'] = 'c';
	m_data['g'] = 'v';
	m_data['h'] = 'x';
	m_data['i'] = 'd';
	m_data['j'] = 'u';
	m_data['k'] = 'i';
	m_data['l'] = 'g';
	m_data['m'] = 'l';
	m_data['n'] = 'b';
	m_data['o'] = 'k';
	m_data['p'] = 'r';
	m_data['q'] = 'z';
	m_data['r'] = 't';
	m_data['s'] = 'n';
	m_data['t'] = 'w';
	m_data['u'] = 'j';
	m_data['v'] = 'p';
	m_data['w'] = 'f';
	m_data['x'] = 'm';
	m_data['y'] = 'a';
	m_data['z'] = 'q';

	int t, i;
	char tmp;
	scanf("%d", &t);
	getchar();
	for(i = 1; i <= t; i++)
	{
		printf("Case #%d: ", i);
		while(scanf("%c",&tmp) && tmp != '\n')
		{
			if(tmp == ' ');
			else tmp = m_data[tmp];
			printf("%c", tmp);
		}
		printf("\n");
	}
}
