#include <iostream>
#include <string>
#include <map>
#include <sstream>

using namespace std;

int stringToInt(string s)
{
		int x;
		istringstream is(s);
		is>>x;
		
		return x;
}

int main()
{
	map<char,char> mapa;
	
	mapa['a']='y';
	mapa['b']='h';
	mapa['c']='e';
	mapa['d']='s';
	mapa['e']='o';
	mapa['f']='c';
	mapa['g']='v';
	mapa['h']='x';
	mapa['i']='d';
	mapa['j']='u';
	mapa['k']='i';
	mapa['l']='g';
	mapa['m']='l';
	mapa['n']='b';
	mapa['o']='k';
	mapa['p']='r';
	mapa['q']='z';
	mapa['r']='t';
	mapa['s']='n';
	mapa['t']='w';
	mapa['u']='j';
	mapa['v']='p';
	mapa['w']='f';
	mapa['x']='m';
	mapa['y']='a';
	mapa['z']='q';
	
	int t;
	string buffer;
	
	getline(cin,buffer);
	t=stringToInt(buffer);
	
	for(int i=1; i<=t; i++)
	{
			getline(cin,buffer);
			cout<<"Case #"<<i<<": ";
			
			for(int j=0; j<(int)buffer.length(); j++)
			{
				if(buffer[j]==' ') cout<<' ';
				else cout<<mapa[buffer[j]];
			}
			cout<<endl;
	}
	return 0;
}
