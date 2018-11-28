#include <iostream>
#include <fstream>

using namespace std;

const char patt[] = "welcome to code jam";

#define DATA_INPUT "C-small.in"
#define DATA_OUTPUT "C-small.out"

long coutStrInStr( char *str, const char *pat)
{
	int t = 0;
	long count = 0;
	if ( pat[1] == '\0')
	{
		while ( str[t] != '\0')
		{
			if ( str[t] == pat[0]) 
				count++;
			t++;
		}
	}
	else
	{
		while ( str[t] != '\0')
		{
			if ( str[t] == pat[0]) 
				count += coutStrInStr (str + t + 1, pat + 1);
			t++;
		}		
	}
	return count;
}

int main ()
{
	int N;
	fstream fin, fout;
	fin.open ( DATA_INPUT, fstream::in);
	fout.open ( DATA_OUTPUT, fstream::out);
	fin >> N;
	char buf[501];
	fin.getline(buf,1);
	for ( int i = 0; i < N; i++)
	{
		fin.getline(buf, 501);
		long count = coutStrInStr( buf, patt);
		fout << "Case #" << i + 1 << ": ";
		fout.width(4);
		fout.fill('0');
		fout << count % 1000 << endl;
	}
	fout.close ( );
	fin.close ( );
}