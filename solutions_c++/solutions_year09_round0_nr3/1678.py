#include <iostream>
#include <fstream>
#include <string.h>

using namespace std;

#define MAXN 100
#define MAXLINE 500

const char* inputname = "C-small-attempt0.in";
const char* outputname = "output.txt";
const char* target = "welcome to code jam";
const int targetLength = strlen( target );
unsigned long stringSize[ 19 ][ MAXLINE ];
char s[ MAXLINE + 1 ];
char result[ 5 ];

unsigned long getNumOfString()
{
	for( int i=0; i<targetLength; i++ )
		for( int j=0; j<MAXLINE; j++ ) stringSize[ i ] [ j ] = 0;
		
	int len = strlen( s );
	
	for( int i=0; i<len; i++ )
		if( s[i] == target[ targetLength-1 ] ) stringSize[ 0 ][i]=1;
	
	for( int i=1; i<targetLength; i++ )
	{
		for( int j=0; j<len; j++ )
		{
			if( s[j] == target[ targetLength-1-i ] )
				for( int k=j; k<len; k++ ) stringSize[ i ][ j ]+= stringSize[ i-1 ][ k ];
		}
	}
	
	unsigned long sum=0;
	for( int i=0; i<len; i++ )
		sum+=stringSize[ targetLength-1 ][ i ];
		
	return sum;
}

int parseInt( char* num )
{
	int len = strlen( num );
	int sum=0;
	for( int i=0; i<len; i++ )
		sum = 10*sum+( num[i]-'0' );
		
	return sum;
}

int pow( int x , int y )
{
	if( y==0 ) return 1;
	int mul=1;
	for( int i=0; i<y; i++ ) mul*=x;
	return mul;
}

char* toString( int n )
{
	for( int i=0; i<4; i++ )
	{
		result[ i ] = '0' + (int)( n/(int)pow( 10 , 3-i ) );
		n%=(int)pow( 10 , 3-i );
	}
}

void input()
{
	ifstream in;
	in.open( inputname , ios::in );
	
	in.getline( s , MAXLINE+1 , '\n' );
	int n=parseInt( s );
	
	if( n > MAXN ) {
		cerr << "Out of test" << endl;
		return;
	}

	ofstream fout( outputname , ios::out );
	
	cout << "Num Of test: " << n << endl;
	for( int i=0; i<n; i++ )
	{
		in.getline( s , MAXLINE+1 , '\n' );
		int res = getNumOfString()%10000;
		toString( res );
		fout << "Case #" << i+1 << ": " << result << endl;
	}

}


int main()
{
	input();
	system("pause");
	return 0;
}
