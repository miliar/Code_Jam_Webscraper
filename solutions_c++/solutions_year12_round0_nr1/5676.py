#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

string transforming(string input)
{
	string output="";
	for (int i=0;i<input.size();i++)
	{
		switch(input[i])
		{
			case ' ':
			{
				output+=' ';
				break;
			}
			case 'e':
			{
				output+='o';
				break;
			}
			case 'j':
			{
				output+='u';
				break;
			}
			case 'p':
			{
				output+='r';
				break;
			}
			case 'm':
			{
				output+='l';
				break;
			}
			case 'y':
			{
				output+='a';
				break;
			}
			case 's':
			{
				output+='n';
				break;
			}
			case 'l':
			{
				output+='g';
				break;
			}
			case 'c':
			{
				output+='e';
				break;
			}

			case 'k':
			{
				output+='i';
				break;
			}
			case 'd':
			{
				output+='s';
				break;
			}
			case 'x':
			{
				output+='m';
				break;
			}
			case 'v':
			{
				output+='p';
				break;
			}
			case 'n':
			{
				output+='b';
				break;
			}
			case 'r':
			{
				output+='t';
				break;
			}
			case 'i':
			{
				output+='d';
				break;
			}
			case 'b':
			{
				output+='h';
				break;
			}
			case 't':
			{
				output+='w';
				break;
			}
			case 'h':
			{
				output+='x';
				break;
			}
			case 'w':
			{
				output+='f';
				break;
			}
			case 'f':
			{
				output+='c';
				break;
			}
			case 'o':
			{
				output+='k';
				break;
			}
			case 'a':
			{
				output+='y';
				break;
			}
			case 'g':
			{
				output+='v';
				break;
			}
			case 'u':
			{
				output+='j';
				break;
			}
			case 'z':
			{
				output+='q';
				break;
			}

			case 'q':
			{
				output+='z';
				break;
			}
		}
	}
	return output;
}
int main()
{
	ifstream inp("CON",ios::in);
	ofstream out("otv.out");
	int n;
	cin >> n;
	string s;
	string ansver;
	for(int i=0;i<n;i++)
	{
		string s;
		getline(inp,s);
		ansver=transforming(s);
		out<<"Case #"<<i+1<<": "<<ansver<<endl;
	}
return 0;
}