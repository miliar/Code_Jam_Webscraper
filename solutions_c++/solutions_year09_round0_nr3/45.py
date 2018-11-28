#include <myheading.h>

void SetFile( string s )
{
	while( s.size()>0 && s[0]<=' ' ) s.erase( 0, 1 ) ;
	while( s.size()>0 && s[s.size()-1]<=' ' ) s.erase( s.size()-1 ) ;
	string::size_type p = s.find('.') ;
	if( p!=string::npos ) s = s.substr( 0, p ) ;
	string sin  = s+".in" ;  freopen( sin. c_str() , "r" , stdin  );
	string sout = s+".out";  freopen( sout.c_str() , "w" , stdout );
}

#define myfor(i,c,d) for( int i=(c); i<=(d); ++i )

const string pat = " welcome to code jam";

char s[1000] ;
int len ;

void readin()
{
	len = 0 ;
	char ch ;
	while( ( ch = getchar() ) != '\n' )
	{
		s[ ++len ] = ch ;
	}
}

const int MAXN = 500 ;
int f[ MAXN+1 ][ 19+1 ] ;

void work()
{
	assert( mysize(pat) == 20 ) ;

	memset( f, 0, sizeof(f) ) ;

	myfor( i, 1, 19 ) f[0][0] = 1 ;

	myfor( i, 1, len )
	{
		f[i][0] = 1 ;
		myfor( k, 1, 19 )
		{
			f[i][k] = f[i-1][k] ;
			if( s[i] == pat[k] ) f[i][k] += f[i-1][k-1] ;
			f[i][k] %= 10000 ;
		}
	}

	printf( "%04d\n", f[len][19]%10000 ) ;
}

int main()
{
	SetFile( "      C-large       " ) ;

	int test ; cin>>test ; readln();
	cerr<<"n_test = "<<test<<endl;

	myfor( _u, 1, test )
	{ 
		cout<<"Case #"<<_u<<": ";
		cerr<<"Running on Case #_"<<_u<<endl ;

		readin() ;
		work() ;
		//cout<<ans<<endl;

	}

	if( !seekeof( cin ) ) cout<<("wrong")<<endl;

	fclose( stdin ); fclose( stdout );
	return 0;
}
