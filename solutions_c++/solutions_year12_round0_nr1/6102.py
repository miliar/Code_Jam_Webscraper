#include<iostream>
#include<string>
#include<map>
#include <limits>
#include<math.h>
using namespace std;
int main()
{
	map<char,char> g;
	int t,no=1;
	char ch;
	string str;
	cin>>t;
	//build a-z map
	g.insert(pair<char,char>(' ',' '));
	g.insert(pair<char,char>('a','y'));
	g.insert(pair<char,char>('b','h'));
	g.insert(pair<char,char>('c','e'));
	g.insert(pair<char,char>('d','s'));
	g.insert(pair<char,char>('e','o'));
	g.insert(pair<char,char>('f','c'));
	g.insert(pair<char,char>('g','v'));
	g.insert(pair<char,char>('h','x'));
	g.insert(pair<char,char>('i','d'));
	g.insert(pair<char,char>('j','u'));
	g.insert(pair<char,char>('k','i'));
	g.insert(pair<char,char>('l','g'));
	g.insert(pair<char,char>('m','l'));
	g.insert(pair<char,char>('n','b'));
	g.insert(pair<char,char>('o','k'));
	g.insert(pair<char,char>('p','r'));
	g.insert(pair<char,char>('q','z'));
	g.insert(pair<char,char>('r','t'));
	g.insert(pair<char,char>('s','n'));
	g.insert(pair<char,char>('t','w'));
	g.insert(pair<char,char>('u','j'));
	g.insert(pair<char,char>('v','p'));
	g.insert(pair<char,char>('w','f'));
	g.insert(pair<char,char>('x','m'));
	g.insert(pair<char,char>('y','a'));
	g.insert(pair<char,char>('z','q'));
	map<char,char> ::iterator p;
	cin.ignore();
	while(t--)
	{	
		getline(cin,str);
		char *s = new char[str.size() + 1];
		std::copy(str.begin(), str.end(), s);
		s[str.size()] = '\0'; 
		//cout<<"\nString value :"<<s<<endl; 
		for(int i=0;i<str.size();++i)
		{
			ch=s[i];
			p=g.find(ch);
			if(p!=g.end())
			s[i]= p->second;
		}
		cout<<"\nCase #"<<no<<": "<<s;
		++no;
		delete[] s;
		
	}
	//system("pause");
	return 0;
}