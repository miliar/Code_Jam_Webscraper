#include <iostream>
#include<fstream>
#include<cstdlib>
#include<string>
using namespace std;

char mapping(char c);

void main()
{
	int N,j=0;
	string G,S;
	ifstream input;
	ofstream output;
	input.open("A-small-attempt2.in");
	output.open("A.out");
	if (input.is_open())
	{
		getline(input,G);
		N=atoi(G.c_str());
		while(j<N)
		{
			j++;
			output<<"Case #"<<j<<": ";
			getline(input,G);
			for(int i=0;i<G.length();i++)
				output<<mapping(G[i]);		
			output<<"\n";
		}
		output.close();
		input.close();
	}
}
char mapping(char c)
{
	char f='a';
	switch(c)
	{
		case ' ':
		f=' ';
		break;
		case 'a':
		f= 'y';
		break;
		case 'b':
		f= 'h';
		break;
		case 'c':
		f= 'e';
		break;
		case 'd':
		f= 's';
		break;
		case 'e':
		f= 'o';
		break;
		case 'f':
		f= 'c';
		break;
		case 'g':
		f= 'v';
		break;
		case 'h':
		f= 'x';	
		break;
		case 'i':
		f= 'd';
		break;
		case 'j':
		f= 'u';
		break;
		case 'k':
		f= 'i';
		break;
		case 'l':
		f= 'g';
		break;
		case 'm':
		f= 'l';
		break;
		case 'n':
		f= 'b';
		break;
		case 'o':
		f= 'k';
		break;
		case 'p':
		f= 'r';
		break;
		case 'q':
		f= 'z';
		break;
		case 'r':
		f= 't';
		break;
		case 's':
		f= 'n';
		break;
		case 't':
		f= 'w';
		break;
		case 'u':
		f= 'j';
		break;
		case 'v':
		f= 'p';
		break;
		case 'w':
		f= 'f';
		break;
		case 'x':
		f= 'm';
		break;
		case 'y':
		f= 'a';
		break;
		case 'z':
		f= 'q';
		break;
	}
	return f;
}

