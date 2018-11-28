#include<iostream>
#include<fstream>
#include<string.h>
using namespace std;

main()
{
	int i,j,c,t;
	char ch;
	ifstream fin("tongue-input.txt");
	ofstream fout("tongue-output.txt");
	fin>>t;
	string g[t];
	getline(fin,g[0]);
	for(i=0;i<t;i++)
	{
		getline(fin,g[i]);
		fout<<"Case #"<<i+1<<": ";
		for(j=0;j<g[i].length();j++)
		{
			ch = g[i][j];
			if(ch >= 'A' && ch <= 'Z')
			{
				ch += 32;
				c = 1;
			}
			else
				c = 0;
			switch(ch)
			{
				case 'a':
					g[i][j] = 'y';
					break;
				case 'b':
					g[i][j] = 'h';
					break;
				case 'c':
					g[i][j] = 'e';
					break;
				case 'd':
					g[i][j] = 's';
					break;
				case 'e':
					g[i][j] = 'o';
					break;
				case 'f':
					g[i][j] = 'c';
					break;
				case 'g':
					g[i][j] = 'v';
					break;
				case 'h':
					g[i][j] = 'x';
					break;
				case 'i':
					g[i][j] = 'd';
					break;
				case 'j':
					g[i][j] = 'u';
					break;
				case 'k':
					g[i][j] = 'i';
					break;
				case 'l':
					g[i][j] = 'g';
					break;
				case 'm':
					g[i][j] = 'l';
					break;
				case 'n':
					g[i][j] = 'b';
					break;
				case 'o':
					g[i][j] = 'k';
					break;
				case 'p':
					g[i][j] = 'r';
					break;
				case 'q':
					g[i][j] = 'z';
					break;
				case 'r':
					g[i][j] = 't';
					break;
				case 's':
					g[i][j] = 'n';
					break;
				case 't':
					g[i][j] = 'w';
					break;
				case 'u':
					g[i][j] = 'j';
					break;
				case 'v':
					g[i][j] = 'p';
					break;
				case 'w':
					g[i][j] = 'f';
					break;
				case 'x':
					g[i][j] = 'm';
					break;
				case 'y':
					g[i][j] = 'a';
					break;
				case 'z':
					g[i][j] = 'q';
					break;
			}
			if(c)
				g[i][j] -= 32;
		}
		fout<<g[i]<<endl;
	}
	fin.close();
	fout.close();
}
