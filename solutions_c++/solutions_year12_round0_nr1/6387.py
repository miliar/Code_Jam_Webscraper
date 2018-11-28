#include <iostream>
#include <string>
#include <fstream>
using namespace std;


void main()
{
	ofstream out("output");
	ifstream in("A-small-attempt1.in");
	int n,i,j;
	char s[50][255];
	in>>n;
	for(i=0;i<=n;i++)
	{
		in.getline(s[i],255);
	//	in>>s[i];
	}
	for(i=1;i<=n;i++)
	{
		j=0;
		while(s[i][j]!=NULL)
		{
			switch(s[i][j])
			{
				case 'a':{s[i][j]='y'; break;}
				case 'b':{s[i][j]='h'; break;}
				case 'c':{s[i][j]='e'; break;}
				case 'd':{s[i][j]='s'; break;}
				case 'e':{s[i][j]='o'; break;}
				case 'f':{s[i][j]='c'; break;}
			    case 'g':{s[i][j]='v'; break;}
				case 'h':{s[i][j]='x'; break;}
				case 'i':{s[i][j]='d'; break;}
     			case 'j':{s[i][j]='u'; break;}
				case 'k':{s[i][j]='i'; break;}
				case 'l':{s[i][j]='g'; break;}
				case 'm':{s[i][j]='l'; break;}
				case 'n':{s[i][j]='b'; break;}
				case 'o':{s[i][j]='k'; break;}
				case 'p':{s[i][j]='r'; break;}
				case 'q':{s[i][j]='z'; break;}
				case 'r':{s[i][j]='t'; break;}
				case 's':{s[i][j]='n'; break;}
				case 't':{s[i][j]='w'; break;}
				case 'u':{s[i][j]='j'; break;}
				case 'v':{s[i][j]='p'; break;}
				case 'w':{s[i][j]='f'; break;}
			    case 'x':{s[i][j]='m'; break;}
	   		    case 'y':{s[i][j]='a'; break;}
				case 'z':{s[i][j]='q'; break;}

			}
			j++;
		}
		out<<"Case #"<<i<<": "<<s[i]<<endl;
	}
}