#include<iostream>
#include<fstream>
#include<sstream>
#include<cstdlib>
using namespace std;
int main()
{
string line;
int counter=1;
ifstream f("A-small-attempt1.in");
getline(f,line);
int a=atoi(line.c_str());
//cout<<a<<endl;
cout<<"Case #"<<counter++<<": ";
while(!f.eof())
{
char c;
f.get(c);
if(c=='a')
	cout<<"y";
else if(c=='b')
	cout<<"h";
else if(c=='c')
	cout<<"e";
else if(c=='d')
	cout<<"s";
else if(c=='e')
	cout<<"o";
else if(c=='f')
	cout<<"c";
else if(c=='g')
	cout<<"v";
else if(c=='h')
	cout<<"x";
else if(c=='i')
	cout<<"d";
else if(c=='j')
	cout<<"u";
else if(c=='k')
	cout<<"i";
else if(c=='l')
	cout<<"g";
else if(c=='m')
	cout<<"l";
else if(c=='n')
	cout<<"b";
else if(c=='o')
	cout<<"k";
else if(c=='p')
	cout<<"r";
else if(c=='q')
	cout<<"z";
else if(c=='r')
	cout<<"t";
else if(c=='s')
	cout<<"n";
else if(c=='t')
	cout<<"w";
else if(c=='u')
	cout<<"j";
else if(c=='v')
	cout<<"p";
else if(c=='w')
	cout<<"f";
else if(c=='x')
	cout<<"m";
else if(c=='y')
	cout<<"a";
else if(c=='z')
	cout<<"q";
else if(c=='\n')
{
	if(counter>a)
	exit(0);
	cout<<"\nCase #"<<counter++<<": ";
}
else
	cout<<" ";
}
return 0;
}

