#include<stdio.h>
#include<iostream>
#include<map>
#include<string>
using namespace std;
int main()
{
	int t;
	map<char,char> mymap;
	mymap.insert(make_pair('y','a'));
	mymap.insert(make_pair('e','o'));
	mymap.insert(make_pair('q','z'));
	mymap.insert(make_pair('j','u'));
	mymap.insert(make_pair('p','r'));
	mymap.insert(make_pair('m','l'));
	mymap.insert(make_pair('y','a'));
	mymap.insert(make_pair('s','n'));
	mymap.insert(make_pair('l','g'));
	mymap.insert(make_pair('j','u'));
	mymap.insert(make_pair('c','e'));
	mymap.insert(make_pair('k','i'));
	mymap.insert(make_pair('d','s'));
	mymap.insert(make_pair('x','m'));
	mymap.insert(make_pair('v','p'));
	mymap.insert(make_pair('n','b'));
	mymap.insert(make_pair('r','t'));
	mymap.insert(make_pair('i','d'));
	mymap.insert(make_pair('b','h'));
	mymap.insert(make_pair('t','w'));
	mymap.insert(make_pair('a','y'));
	mymap.insert(make_pair('h','x'));
	mymap.insert(make_pair('w','f'));
	mymap.insert(make_pair('m','l'));
	mymap.insert(make_pair('o','k'));
	mymap.insert(make_pair('g','v'));
	mymap.insert(make_pair('j','u'));
	mymap.insert(make_pair('u','j'));
	mymap.insert(make_pair('f','c'));
	mymap.insert(make_pair('z','q'));
	scanf("%d ",&t);
	char c;
	int i=0;
	cout << "Case #" << i+1<<": ";
	while(i < t)
	{
		scanf("%c",&c);
		if(c == '\n')
		{
			cout << endl;
			i++;
			if(i+1 <= t)
				cout << "Case #" << i+1<<": ";
		}
		else if(c != ' ')
			cout << mymap.find(c)->second;
		else
			cout << c;
	}
	return 0;
}
