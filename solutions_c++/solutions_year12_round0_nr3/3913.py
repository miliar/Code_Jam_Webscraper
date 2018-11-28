#include <iostream>
#include <fstream>

using namespace std;

fstream fin;
fstream fout;

class recycler
{
public:
	void check( int numA, int numB, int casenum );
	int shift( char *sznum );
};

int recycler::shift( char *sznum )
{
	int len = strlen(sznum);
	char sftnum = sznum[0];
	memcpy(sznum, sznum+1, len-1);
	memcpy(sznum+(len-1), &sftnum, 1);

	return atoi(sznum);
}

void recycler::check( int numA, int numB, int casenum )
{
	int n = numA;
	int m = 0;

	char szm[256] = {0, };


	int count = 0;

	// add
	while ( n < numB )
	{
		itoa( n, szm, 10 );

		// shift
		while(1)
		{
			m = this->shift( szm );
			if ( n == m ) break;
			if ( n < m && m <= numB )
				count++;
		}
		n++;
	}

	//Case #1: 0
	fout << "Case #" << casenum+1 << ": "<< count << endl;

}

int main()
{
	recycler r;
	char buf[128] = {0, };

	fin.open("C-large.in", ios_base::in);
	fout.open("a.out", ios_base::out);

	fin.getline( buf, 128 );

	int size = atoi(buf);
	int numA = 0;
	int numB = 0;

	for( int i=0; i<size; i++)
	{
		fin >> buf;
		numA = atoi(buf);
		fin >> buf;
		numB = atoi(buf);

		r.check( numA, numB, i );
	}
	
	//r.check( "1", "9" );
	//r.check( "10", "40" );
	//r.check( "100", "500" );
	//r.check( "1111", "2222" );

	return 0;
}