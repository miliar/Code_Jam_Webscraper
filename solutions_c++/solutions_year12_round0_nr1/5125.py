#include <iostream>
#include <fstream>
#include <string>
using namespace std;


string szinput = "../A-small-attempt1.in";
string szoutput = "../output.txt";
int main()
{
	ifstream in;
	in.open(szinput , ios::in);

	ofstream out;
	out.open(szoutput,ios::out);
	int T;

	in>>T;
	in.ignore(100,'\n');

	for(int i=0;i<T;i++)
	{
		string line;
		getline(in,line);

		int len = line.length();
		string res="";
		for(int j=0;j<len;j++)
		{
			if(line.c_str()[j]=='a')
				res.push_back('y');
			else if(line.c_str()[j]=='b')
				res.push_back('h');
			else if(line.c_str()[j]=='c')
				res.push_back('e');
			else if(line.c_str()[j]=='d')
				res.push_back('s');
			else if(line.c_str()[j]=='e')
				res.push_back('o');
			else if(line.c_str()[j]=='f')
				res.push_back('c');
			else if(line.c_str()[j]=='g')
				res.push_back('v');
			else if(line.c_str()[j]=='h')
				res.push_back('x');
			else if(line.c_str()[j]=='i')
				res.push_back('d');
			else if(line.c_str()[j]=='j')
				res.push_back('u');
			else if(line.c_str()[j]=='k')
				res.push_back('i');
			else if(line.c_str()[j]=='l')
				res.push_back('g');
			else if(line.c_str()[j]=='m')
				res.push_back('l');
			else if(line.c_str()[j]=='n')
				res.push_back('b');
			else if(line.c_str()[j]=='o')
				res.push_back('k');
			else if(line.c_str()[j]=='p')
				res.push_back('r');
			else if(line.c_str()[j]=='q')
				res.push_back('z');
			else if(line.c_str()[j]=='r')
				res.push_back('t');
			else if(line.c_str()[j]=='s')
				res.push_back('n');
			else if(line.c_str()[j]=='t')
				res.push_back('w');
			else if(line.c_str()[j]=='u')
				res.push_back('j');
			else if(line.c_str()[j]=='v')
				res.push_back('p');
			else if(line.c_str()[j]=='w')
				res.push_back('f');
			else if(line.c_str()[j]=='x')
				res.push_back('m');
			else if(line.c_str()[j]=='y')
				res.push_back('a');
			else if(line.c_str()[j]=='z')
				res.push_back('q');
			else if(line.c_str()[j]==' ')
				res.push_back(' ');
		}

		out<<"Case #"<<i+1<<": "<<res<<endl;
	}
	return 1;
}