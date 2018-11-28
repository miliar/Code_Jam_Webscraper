#include <iostream>
#include <cstdlib>
#include <cmath>
#include <string>
using namespace std;


int main(int argc, char ** argv)
{
	int T;
	cin>>T;
	string* S = new string[T];
	string* O = new string[T];
	string dummy;
	getline(cin,dummy);
	for(int i=0;i<T;i++)
	{
		getline(cin,S[i]);
	}
	string input;
	int len;
	for(int i=0;i<T;i++)
	{
		input = S[i];
		len = input.length();
		string output;
		for(int j=0;j<len;j++)
		{
			if(input[j] == ' ')
			{
				output.push_back(' ');
			}
			if(input[j] == 'y')
			{
				output.push_back('a');
			}
			if(input[j] == 'n')
			{
				output.push_back('b');
			}
			if(input[j] == 'f')
			{
				output.push_back('c');
			}
			if(input[j] == 'i')
			{
				output.push_back('d');
			}
			if(input[j] == 'c')
			{
				output.push_back('e');
			}
			if(input[j] == 'w')
			{
				output.push_back('f');
			}
			if(input[j] == 'l')
			{
				output.push_back('g');
			}
			if(input[j] == 'b')
			{
				output.push_back('h');
			}
			if(input[j] == 'k')
			{
				output.push_back('i');
			}
			if(input[j] == 'u')
			{
				output.push_back('j');
			}
			if(input[j] == 'o')
			{
				output.push_back('k');
			}
			if(input[j] == 'm')
			{
				output.push_back('l');
			}
			if(input[j] == 'x')
			{
				output.push_back('m');
			}
			if(input[j] == 's')
			{
				output.push_back('n');
			}
			if(input[j] == 'e')
			{
				output.push_back('o');
			}
			if(input[j] == 'v')
			{
				output.push_back('p');
			}
			if(input[j] == 'z')
			{
				output.push_back('q');
			}
			if(input[j] == 'p')
			{
				output.push_back('r');
			}
			if(input[j] == 'd')
			{
				output.push_back('s');
			}
			if(input[j] == 'r')
			{
				output.push_back('t');
			}
			if(input[j] == 'j')
			{
				output.push_back('u');
			}
			if(input[j] == 'g')
			{
				output.push_back('v');
			}
			if(input[j] == 't')
			{
				output.push_back('w');
			}
			if(input[j] == 'h')
			{
				output.push_back('x');
			}
			if(input[j] == 'a')
			{
				output.push_back('y');
			}
			if(input[j] == 'q')
			{
				output.push_back('z');
			}
		}
		O[i] = output;
	}
	for(int i=0;i<T;i++)
	{
		cout<<"Case #"<<i+1<<": "<<O[i]<<endl;
	}
	return 0;
}

