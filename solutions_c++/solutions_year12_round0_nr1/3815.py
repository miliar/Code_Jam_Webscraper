#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <map>

using namespace std;

int main()
{
	map<char , char> m_map;
	
	m_map.insert(pair<char,char>('a','y'));
	m_map.insert(pair<char,char>('b','h'));
	m_map.insert(pair<char,char>('c','e'));
	m_map.insert(pair<char,char>('d','s'));
	m_map.insert(pair<char,char>('e','o'));
	m_map.insert(pair<char,char>('f','c'));
	m_map.insert(pair<char,char>('g','v'));
	m_map.insert(pair<char,char>('h','x'));
	m_map.insert(pair<char,char>('i','d'));
	m_map.insert(pair<char,char>('j','u'));
	m_map.insert(pair<char,char>('k','i'));
	m_map.insert(pair<char,char>('l','g'));
	m_map.insert(pair<char,char>('m','l'));
	m_map.insert(pair<char,char>('n','b'));
	m_map.insert(pair<char,char>('o','k'));
	m_map.insert(pair<char,char>('p','r'));
	m_map.insert(pair<char,char>('q','z'));
	m_map.insert(pair<char,char>('r','t'));
	m_map.insert(pair<char,char>('s','n'));
	m_map.insert(pair<char,char>('t','w'));
	m_map.insert(pair<char,char>('u','j'));
	m_map.insert(pair<char,char>('v','p'));
	m_map.insert(pair<char,char>('w','f'));
	m_map.insert(pair<char,char>('x','m'));
	m_map.insert(pair<char,char>('y','a'));
	m_map.insert(pair<char,char>('z','q'));
	m_map.insert(pair<char,char>(' ',' '));
	
	int n;
	string line;
	
	scanf("%d" , &n);
	getline(cin , line);	
	
	for (int i = 0; i < n; ++i)
	{
		getline(cin , line);	
		
		printf("Case #%d: " , i + 1);  
		
		for (int j = 0; j < line.length(); ++j)
		{
			printf("%c", m_map[line[j]]);
		}
		
		printf("\n");
	}
	
	return 0;
}