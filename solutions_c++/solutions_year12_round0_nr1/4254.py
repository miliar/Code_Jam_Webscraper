#include <iostream>
#include <string>
#include <climits>
#include <map>
using namespace std;
int main (int argc, char **argv)
{
	map<char,char> mymap ;
	mymap['a']= 'y';
	mymap['b']= 'h';
	mymap['c']= 'e';
	mymap['d']= 's';
	mymap['e']= 'o';
	mymap['f']= 'c';
	mymap['g']= 'v';
	mymap['h']= 'x';
	mymap['i']= 'd';
	mymap['j']= 'u';
	mymap['k']= 'i';
	mymap['l']= 'g';
	mymap['m']= 'l';
	mymap['n']= 'b';
	mymap['o']= 'k';
	mymap['p']= 'r';
	mymap['q']= 'z';
	mymap['r']= 't';
	mymap['s']= 'n';
	mymap['t']= 'w';
	mymap['u']= 'j';
	mymap['v']= 'p';
	mymap['w']= 'f';
	mymap['x']= 'm';
	mymap['y']= 'a';
	mymap['z']= 'q';
	mymap[' ']= ' ';
	int num;
	cin>>num;
	cin.clear(); 
	cin.ignore(INT_MAX,'\n'); 
	string str;
	for (int i=0;i<num;i++)
	{
		cout<<"Case #"<<i + 1<<": ";
		//cin>>str;
		getline (cin,str);
		string::iterator beg = str.begin();
		string::iterator end = str.end();
		for (;beg != end; ++beg)
		{
			cout<<mymap[*beg];
		} 
		cout<<endl;
	}
	return 0;
}

