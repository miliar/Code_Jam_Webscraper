#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	ifstream in;
	in.open("A-small-attempt0.in");
	ofstream out;
	out.open("output.txt");

	unsigned int cases = 0;
	in>>cases;

	for (unsigned int _case=0; _case<cases; _case++)
	{
		char* str = new char[300];
		in.getline(str,300);

		if (strlen(str))
		{
			for (unsigned int i=0; i<strlen(str); i++)
			{
				char x=' ';
				
				switch(str[i])
				{
					case 'a': x='y'; break;
					case 'b': x='h'; break;
					case 'c': x='e'; break;
					case 'd': x='s'; break;
					case 'e': x='o'; break;
					case 'f': x='c'; break;
					case 'g': x='v'; break;
					case 'h': x='x'; break;
					case 'i': x='d'; break;
					case 'j': x='u'; break;
					case 'k': x='i'; break;
					case 'l': x='g'; break;
					case 'm': x='l'; break;
					case 'n': x='b'; break;
					case 'o': x='k'; break;
					case 'p': x='r'; break;
					case 'q': x='z'; break;
					case 'r': x='t'; break;
					case 's': x='n'; break;
					case 't': x='w'; break;
					case 'u': x='j'; break;
					case 'v': x='p'; break;
					case 'w': x='f'; break;
					case 'x': x='m'; break;
					case 'y': x='a'; break;
					case 'z': x='q'; break;

				}

				str[i]=x;
			}
			cout<<"Case #"<<_case+1<<": "<<str<<endl;
			out<<"Case #"<<_case+1<<": "<<str<<endl;
		}
		else _case--;
	}

	out.close();
	in.close();
}