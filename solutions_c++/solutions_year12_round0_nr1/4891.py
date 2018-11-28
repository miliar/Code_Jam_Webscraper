#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <string.h>
#include <conio.h>
#include <map>
#include <sstream>

using namespace std;



int main()
{
	int n=0;		//количество
	FILE* in = freopen("input.txt", "r", stdin);
	FILE* out = freopen("output.txt", "w", stdout);

	string g;
	cin>>n;
	getline(cin, g);

	for( int i=0; i<n; i++ )
	{
		getline(cin, g);
		cout<<"Case #"<<i+1<<": ";
		for( int j=0; j<g.size(); j++ )
		{
			switch (g[j])
			{
			case ' ':
				cout<<' ';
				break;
			case 'q':
				cout<<'z';
				break;
			case 'w':
				cout<<'f';
				break;
			case 'e':
				cout<<'o';
				break;
			case 'r':
				cout<<'t';
				break;
			case 't':
				cout<<'w';
				break;
			case 'y':
				cout<<'a';
				break;
			case 'u':
				cout<<'j';
				break;
			case 'i':
				cout<<'d';
				break;
			case 'o':
				cout<<'k';
				break;
			case 'p':
				cout<<'r';
				break;
			case 'l':
				cout<<'g';
				break;
			case 'k':
				cout<<'i';
				break;
			case 'j':
				cout<<'u';
				break;
			case 'h':
				cout<<'x';
				break;
			case 'g':
				cout<<'v';
				break;
			case 'f':
				cout<<'c';
				break;
			case 'd':
				cout<<'s';
				break;
			case 's':
				cout<<'n';
				break;
			case 'a':
				cout<<'y';
				break;
			case 'z':
				cout<<'q';
				break;
			case 'x':
				cout<<'m';
				break;
			case 'c':
				cout<<'e';
				break;
			case 'v':
				cout<<'p';
				break;
			case 'b':
				cout<<'h';
				break;
			case 'n':
				cout<<'b';
				break;
			case 'm':
				cout<<'l';
				break;
			}
		}
		cout<<endl;
	}

    return 0;
}