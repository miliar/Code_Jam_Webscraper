#include<iostream>
#include<stdio.h>
#include<string>
using namespace std;

int main()
{
	int diff='A'-'a';
	int t;
	cin>>t;
	string s[t+1];
	for(int i=0;i<t+1;i++)
		getline(cin, s[i], '\n');	
	for(int i=1;i<t+1;i++)
	{
		for(int j=0;j<s[i].length();j++)
		{
			switch(s[i][j])
			{
				case 'a':
					s[i][j]='Y';
					break;
				case 'b':
					s[i][j]='H';
					break;
				case 'c':
					s[i][j]='E';
					break;
				case 'd':
					s[i][j]='S';
					break;
				case 'e':
					s[i][j]='O';
					break;
				case 'f':
					s[i][j]='C';
					break;
				case 'g':
					s[i][j]='V';
					break;
				case 'h':
					s[i][j]='X';
					break;
				case 'i':
					s[i][j]='D';
					break;
				case 'j':
					s[i][j]='U';
					break;
				case 'k':
					s[i][j]='I';
					break;
				case 'l':
					s[i][j]='G';
					break;
				case 'm':
					s[i][j]='L';
					break;
				case 'n':
					s[i][j]='B';
					break;
				case 'o':
					s[i][j]='K';
					break;
				case 'p':
					s[i][j]='R';
					break;
				case 'q':
					s[i][j]='Z';
					break;
				case 'r':
					s[i][j]='T';
					break;
				case 's':
					s[i][j]='N';
					break;
				case 't':
					s[i][j]='W';
					break;
				case 'u':
					s[i][j]='J';
					break;
				case 'v':
					s[i][j]='P';
					break;
				case 'w':
					s[i][j]='F';
					break;
				case 'x':
					s[i][j]='M';
					break;
				case 'y':
					s[i][j]='A';
					break;
				case 'z':
					s[i][j]='Q';
					break;
				case ' ':
					s[i][j]=' '+diff;
					break;
				default:
					break;
			}
		}
		for(int j=0;j<s[i].length();j++)
			s[i][j]-=diff;
		cout<<"Case #"<<i<<": "<<s[i]<<endl;
	}
	
}		
