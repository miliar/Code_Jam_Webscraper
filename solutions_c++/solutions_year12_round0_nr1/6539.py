#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main()
{
	string G;
	
	ifstream in;
	ofstream out;
	
	int Cases;
	
	in.open("Init.txt");
	out.open("Out.txt");

	getline(in, G);

	Cases=atoi(G.c_str());

	for (int i=0; i<Cases; i++)
	{
		fflush(stdin);
		getline(in, G);

		for (int j=0; j<G.length(); j++)
		{

			switch (G[j])
			{
				case 'a':
				{
					G[j]='y';
					break;
				}
				case 'b':
				{
					G[j]='h';
					break;
				}
				case 'c':
				{
					G[j]='e';
					break;
				}
				case 'd':
				{
					G[j]='s';
					break;
				}
				case 'e':
				{
					G[j]='o';
					break;
				}
				case 'f':
				{
					G[j]='c';
					break;
				}
				case 'g':
				{
					G[j]='v';
					break;
				}
				case 'h':
				{
					G[j]='x';
					break;
				}
				case 'i':
				{
					G[j]='d';
					break;
				}
				case 'j':
				{
					G[j]='u';
					break;
				}
				case 'k':
				{
					G[j]='i';
					break;
				}
				case 'l':
				{
					G[j]='g';
					break;
				}
				case 'm':
				{
					G[j]='l';
					break;
				}
				case 'n':
				{
					G[j]='b';
					break;
				}
				case 'o':
				{
					G[j]='k';
					break;
				}
				case 'p':
				{
					G[j]='r';
					break;
				}
				case 'q':
				{
					G[j]='z';
					break;
				}
				case 'r':
				{
					G[j]='t';
					break;
				}
				case 's':
				{
					G[j]='n';
					break;
				}
				case 't':
				{
					G[j]='w';
					break;
				}
				case 'u':
				{
					G[j]='j';
					break;
				}
				case 'v':
				{
					G[j]='p';
					break;
				}
				case 'w':
				{
					G[j]='f';
					break;
				}
				case 'x':
				{
					G[j]='m';
					break;
				}
				case 'y':
				{
					G[j]='a';
					break;
				}
				case 'z':
				{
					G[j]='q';
					break;
				}
			}
			
			
		}
		out<<"Case #"<<i+1<<": "<<G<<endl;
	}
	
	in.close();
	out.close();

	return 0;
}