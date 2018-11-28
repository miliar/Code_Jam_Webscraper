#include <iostream>
#include <fstream>
#include <string>
#include<cmath>
using namespace std;
string decode(string s)
{
	string ans="";
	for(int i=0;i<s.length();i++)
	{
		switch(s[i])
		{
		case ' ':{ans+=' ';break;}
		case 'a':{ans+='y';break;}
		case 'b':{ans+='h';break;}
		case 'c':{ans+='e';break;}
		case 'd':{ans+='s';break;}
		case 'e':{ans+='o';break;}
		case 'f':{ans+='c';break;}
		case 'g':{ans+='v';break;}
		case 'h':{ans+='x';break;}
		case 'i':{ans+='d';break;}
		case 'j':{ans+='u';break;}
		case 'k':{ans+='i';break;}
		case 'l':{ans+='g';break;}
		case 'm':{ans+='l';break;}
		case 'n':{ans+='b';break;}
		case 'o':{ans+='k';break;}
		case 'p':{ans+='r';break;}
		case 'q':{ans+='z';break;}
		case 'r':{ans+='t';break;}
		case 's':{ans+='n';break;}
		case 't':{ans+='w';break;}
		case 'u':{ans+='j';break;}
		case 'v':{ans+='p';break;}
		case 'w':{ans+='f';break;}
		case 'x':{ans+='m';break;}
		case 'y':{ans+='a';break;}
		case 'z':{ans+='q';break;}
		}
	
	}
	return ans;

}
int main()
{
	string s;
	ifstream in;
	ofstream out;
	in.open("file.txt");
	out.open("out.txt");
	int n;
	cin>>n;
	for(int i=0;i<n;i++)
	{
		getline(in,s);
		cout<<"Case #"<<i+1<<": "<<decode(s)<<'\n';
		out<<"Case #"<<i+1<<": "<<decode(s)<<'\n';
	}
return 0;
}