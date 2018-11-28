#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <conio.h>
using namespace std;

int main() {
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	int K,c=1;
	char ch;
	string s;
	getline(cin, s);
	sscanf(s.c_str(), "%d", &K);
	cout<<"Case #1: ";
		while((ch=getchar())!=EOF)
		{
			if(ch==' ')
				cout<<" ";
			else if((ch=='\n')&&(c<K))
			{
				cout<<"\n";
				cout<<"Case #"<<c+1<<": ";
				c++;
			}
			else
				switch(ch) {
				case 'a':
					cout<<"y";
					break;
				case 'b':
					cout<<"h";
					break;
				case 'c':
					cout<<"e";
					break;
				case 'd':
					cout<<"s";
					break;
				case 'e':
					cout<<"o";
					break;
				case 'f':
					cout<<"c";
					break;
				case 'g':
					cout<<"v";
					break;
				case 'h':
					cout<<"x";
					break;
				case 'i':
					cout<<"d";
					break;
				case 'j':
					cout<<"u";
					break;
				case 'k':
					cout<<"i";
					break;
				case 'l':
					cout<<"g";
					break;
				case 'm':
					cout<<"l";
					break;
				case 'n':
					cout<<"b";
					break;
				case 'o':
					cout<<"k";
					break;
				case 'p':
					cout<<"r";
					break;
				case 'q':
					cout<<"z";
					break;
				case 'r':
					cout<<"t";
					break;
				case 's':
					cout<<"n";
					break;
				case 't':
					cout<<"w";
					break;
				case 'u':
					cout<<"j";
					break;
				case 'v':
					cout<<"p";
					break;
				case 'w':
					cout<<"f";
					break;
				case 'x':
					cout<<"m";
					break;
				case 'y':
					cout<<"a";
					break;
				case 'z':
					cout<<"q";
					break;
			}
		}
}