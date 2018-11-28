#include <myheading.h>

void SetFile( string s )
{
	string::size_type p = s.find('.') ;
	if( p!=string::npos ) s = s.substr( 0, p ) ;
	string sin  = s+".in" ;  freopen( sin. c_str() , "r" , stdin  );
	string sout = s+".out";  freopen( sout.c_str() , "w" , stdout );
}

#define myfor(i,c,d) for( int i=(c); i<=(d); ++i )

const int MAXN = 50000  ;
const int mod = 1000000007 ;


int n , k ; 
int a ;

char s[ MAXN+100 ] ;

void readin()
{
	scanf("%d",&k) ;
	scanf("%s",s) ;

	n = (int)( strlen( s ) );	
}

int process( int *a )
{
	static char t[ MAXN+100 ] ;

	int c = 0 , d = k-1 ;
	while( c!=n )
	{
		myfor( i, 1, k ) 
			t[c+i-1] = s[ c+a[i]-1 ] ;

		c += k , d+=k ;
	}

	int re = 1 ;
	myfor( i, 1, n-1 )
		if( t[i]!=t[i-1] ) ++ re;

	return re; 
}

void work()
{
	int ans = n+1 ;
	
	static int a[ 100 ] ;
	myfor( i, 1, k ) a[i] = i ;

	do
	{
		int t = process( a ) ;
		if( t<ans ) ans = t ;

	}
	while( next_permutation( a+1, a+k+1) ) ;

	cout<<ans<<endl;
}

int main()
{
	SetFile( "D-small-attempt0.in" ) ;
	
	int test ; cin>>test ; readln();
	myfor( i, 1, test )
	{ 
		cout<<"Case #"<<i<<": ";
		cerr<<"Running on Case #_"<<i<<endl ;

		readin() ;
		work() ;
		//cout<<ans<<endl;

	}

	if( !seekeof( cin ) ) cout<<("wrong")<<endl;

	fclose( stdin ); fclose( stdout );
	return 0;
}
