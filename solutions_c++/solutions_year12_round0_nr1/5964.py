#include <cstdio>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <limits>
using namespace std;

string input,output;
map<char,char>mymap;
map<char,char>:: iterator it;

void pre()
{
	mymap.insert(pair<char,char>('a','y')); mymap.insert(pair<char,char>('j','u')); mymap.insert(pair<char,char>('s','n'));
	mymap.insert(pair<char,char>('b','h')); mymap.insert(pair<char,char>('k','i')); mymap.insert(pair<char,char>('t','w'));
	mymap.insert(pair<char,char>('c','e')); mymap.insert(pair<char,char>('l','g')); mymap.insert(pair<char,char>('u','j'));
	mymap.insert(pair<char,char>('d','s')); mymap.insert(pair<char,char>('m','l')); mymap.insert(pair<char,char>('v','p'));
	mymap.insert(pair<char,char>('e','o')); mymap.insert(pair<char,char>('n','b')); mymap.insert(pair<char,char>('w','f'));
	mymap.insert(pair<char,char>('f','c')); mymap.insert(pair<char,char>('o','k')); mymap.insert(pair<char,char>('x','m'));
	mymap.insert(pair<char,char>('g','v')); mymap.insert(pair<char,char>('p','r')); mymap.insert(pair<char,char>('y','a'));
	mymap.insert(pair<char,char>('h','x')); mymap.insert(pair<char,char>('q','z')); mymap.insert(pair<char,char>('z','q'));
	mymap.insert(pair<char,char>('i','d')); mymap.insert(pair<char,char>('r','t')); mymap.insert(pair<char,char>(' ',' '));
}

int main()
{
	ifstream in("/home/pranay/Desktop/in.txt");
	ofstream out("/home/pranay/Desktop/out.txt");
	
	int i,t,cases;
	pre();
	//char dump;
	in>>t;
	in.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	for(cases=1;cases<=t;cases++)
	{
		output="";
		getline(in,input);
		int len = input.length();
		for(i=0;i<len;i++)
		{
			output+=mymap[input[i]];
		}
		out<<"Case #"<<cases<<": "<<output<<endl;
		
	}
	return 0;
	
}
