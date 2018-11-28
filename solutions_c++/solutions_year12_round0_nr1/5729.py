#include<iostream>
#include<string>
#include<fstream>
#include<cstdio>
using namespace std;
string replace(char x);
int main(int argc,char*argv[])
{
	freopen("inin.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int n;cin>>n;
	string s,r;
	getline(cin,s,'\n');
	for(int i=0;i<n;i++)
	{	
		r="";
		getline(cin,s,'\n');		
		//cout<<"string: "<<s<<"\n";
		//cout<<"string-length: "<<s.length()<<"\n";
		for(int j=0;j<s.length();j++)
		{
			//cout<<s[j]<<"\n";
			if(s[j]==' '){r = r + " ";}
			else	{r = r + replace(s[j]);}
			
		}
		cout<<"Case #"<<i<<": "<<r<<"\n";
	}
}
string replace(char x)
{
	//cout<<"Replace char called for '"<<x<<"'\n";
	switch (x)
	{
		case 'y':
			return "a";break;
		case 'n':
			return "b";break;
		case 'f':
			return "c";break;
		case 'i':
			return "d";break;
		case 'c':
			return "e";break;
		case 'w':
			return "f";break;
		case 'l':
			return "g";break;
		case 'b':
			return "h";break;
		case 'k':
			return "i";break;
		case 'u':
			return "j";break;
		case 'o':
			return "k";break;
		case 'm':
			return "l";break;
		case 'x':
			return "m";break;
		case 's':
			return "n";break;
		case 'e':
			return "o";break;
		case 'v':
			return "p";break;
		case 'z':
			return "q";break;
		case 'p':
			return "r";break;
		case 'd':
			return "s";break;
		case 'r':
			return "t";break;
		case 'j':
			return "u";break;
		case 'g':
			return "v";break;
		case 't':
			return "w";break;
		case 'h':
			return "x";break;
		case 'a':
			return "y";break;
		case 'q':
			return "z";break;
	}
}