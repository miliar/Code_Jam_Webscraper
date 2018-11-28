/*
ID: mitstud1
PROG: beads
LANG: C++
*/

#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<map>
using namespace std;

char conv(char ch)
{
	switch(ch)
	{
	case 'a':
		return 'y';
	case 'b':
		return 'h';
	case 'c':
		return 'e';
	case 'd':
		return 's';
	case 'e':
		return 'o';
	case 'f':
		return 'c';
	case 'g':
		return 'v';
	case 'h':
		return 'x';
	case 'i':
		return 'd';
	case 'j':
		return 'u';
	case 'k':
		return 'i';
	case 'l':
		return 'g';
	case 'm':
		return 'l';
	case 'n':
		return 'b';
	case 'o':
		return 'k';
	case 'p':
		return 'r';
	case 'q':
		return 'z';
	case 'r':
		return 't';
	case 's':
		return 'n';
	case 't':
		return 'w';
	case 'u':
		return 'j';
	case 'v':
		return 'p';
	case 'w':
		return 'f';
	case 'x':
		return 'm';
	case 'y':
		return 'a';
	case 'z':
		return 'q';
	default:
		return ' ';
	}
}

int main()
{
	ifstream in ("test.in");
	ofstream out ("test.out");
	int n;
	in>>n;
	for(int i=0; i<n; i++)
	{
		int n, s, p;
		int a[100];
		in>>n>>s>>p;
		for(int j=0; j<n; j++)
			in>>a[j];
		int least, sleast, ans=0;
		least = 3*p-2; sleast = 3*p-4;
		if(least<0) least = 0; if(sleast<0) sleast = 0; 
		for(int j=0; j<n; j++)
		{
			if(a[j]>=p)
			{
				if(a[j] >= least)
					ans ++;
				else if(a[j] >= sleast && s>0)
				{
					ans++;
					s--;
				}
			}
		}
		out<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	//fout<<out<<endl;
	
}