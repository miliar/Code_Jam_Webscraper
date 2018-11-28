#include<iostream>
#include<fstream>
#include<string>
using namespace std;

ifstream fin;
ofstream fout;

int main()
{
	int T, X = 0 , i;
	
	fin.open("A_small.in");
	fout.open("a_small.out");
	
	fin >> T;
	string s;
	getline( fin , s );
	while(T--)
	{
		getline( fin , s );
		fout << "Case #" << ++X << ": ";
		for( i = 0 ; i < (int)s.size() ; ++i )
		{
			if( s[i] == ' ' )
				fout << ' ';
			else if( s[i] == 'y' )
				fout << 'a';
			else if( s[i] == 'n' )
				fout << 'b';
			else if( s[i] == 'f' )
				fout << 'c';
			else if( s[i] == 'i' )
				fout << 'd';
			else if( s[i] == 'c' )
				fout << 'e';
			else if( s[i] == 'w' )
				fout << 'f';
			else if( s[i] == 'l' )
				fout << 'g';
			else if( s[i] == 'b' )
				fout << 'h';
			else if( s[i] == 'k' )
				fout << 'i';
			else if( s[i] == 'u' )
				fout << 'j';
			else if( s[i] == 'o' )
				fout << 'k';
			else if( s[i] == 'm' )
				fout << 'l';
			else if( s[i] == 'x' )
				fout << 'm';
			else if( s[i] == 's' )
				fout << 'n';
			else if( s[i] == 'e' )
				fout << 'o';
			else if( s[i] == 'v' )
				fout << 'p';
			else if( s[i] == 'z' )
				fout << 'q';
			else if( s[i] == 'p' )
				fout << 'r';
			else if( s[i] == 'd' )
				fout << 's';
			else if( s[i] == 'r' )
				fout << 't';
			else if( s[i] == 'j' )
				fout << 'u';
			else if( s[i] == 'g' )
				fout << 'v';
			else if( s[i] == 't' )
				fout << 'w';
			else if( s[i] == 'h' )
				fout << 'x';
			else if( s[i] == 'a' )
				fout << 'y';
			else //if( s[i] == 'q' )
				fout << 'z';
		}
		fout << endl;
	}
	return 0;
} 

