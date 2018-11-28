#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <fstream>
#include <set>
#include <map>
using namespace std;

#define mysize(X) ((int)X.size())
#define myfor(i,c,d) for( int i=(c); i<=(d); ++i )
#define myforv(i,V) for( int i=0; i<mysize(V); ++i )
template<class T>void checkmin( T&a, const T&b ){if(b<a)a=b;}

bool seekeof()
{
	int t;  while( (t=cin.peek())!=EOF && t<=' ' ) cin.get();
	return t==EOF ;
}

ifstream fin ;
ofstream fout ;

map< string, int > no ;
int n ;
int ans ;


void readin()
{
	no.clear();

	string s, buf ;

	cin>>n; getline( cin, buf );
	myfor( i, 1, n )
	{
		getline( cin, s );
		no[s] = i ;
	}
}

void work()
{
	static  int f [ 1000+1 ][ 100+1 ] ;
	memset( f[0], 0, sizeof(f[0]) ) ;

	string s , buf ;
	int n_query ; cin >> n_query; getline( cin, buf );

	myfor( i, 1, n_query )
	{
		getline( cin, s );
		if( no[s]==0 ) cout<<"wrong"<<endl;

		myfor( j, 1, n )
		{
			f[i][j] = 9999999 ;
			if( no[s] == j ) continue;

			myfor( k, 1, n )
				checkmin( f[i][j] , f[i-1][k] + (int)(j!=k) );
		}
	}//for i

	ans = 99999 ;
	myfor( j, 1, n )
		checkmin( ans, f[n_query][j] ) ;
}

int main()
{
	freopen( "A-large.in", "r", stdin );
	freopen( "A-large.out", "w", stdout );
	//freopen( "in.txt", "r", stdin );
	//freopen( "out.txt", "w", stdout );

	int test ; cin>>test ;

	myfor( i, 1, test )
	{
		cout<<"Case #"<<i<<": ";

		readin();
		work();

		cout<< ans <<endl;
	}

	if( !seekeof() ) cout<<("wrong")<<endl;
	
	fclose( stdin ); fclose( stdout );
	return 0;
}