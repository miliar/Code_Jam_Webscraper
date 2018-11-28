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

const int MAXN = 5010 ;
const int MAXLEN = 15 ;
const int mod = 1000000007 ;

int len, n ;

string dic[ MAXN+1 ] ;

void read_dic()
{
	myfor( i, 1, n ) cin>>dic[i] ;
}

bool match( string pat, string word )
{
	static bool ok[ MAXLEN+1 ][ 'z'+1 ] ;

	memset( ok, false, sizeof(ok) ) ;

	int k = 0 ;
	bool in_par = false ;
	myforv( i, pat )
	{
		if( pat[i]=='(' ) { in_par = true ; continue ; }
		if( pat[i]==')' ) { in_par = false ; ++k; continue ; }

		ok[k][ (int)pat[i] ] = true ;

		if( !in_par ) ++k ;		
	}

	myforv( i, word )
		if( ! ok[i][ word[i] ] ) return false ;

	return true ;
}

void work()
{
	string s ;
	cin>>s ;

	int cnt = 0 ;
	myfor( i, 1, n )
		if( match( s, dic[i] ) ) ++cnt ;

	cout<<cnt<<endl;
}

int main()
{
	SetFile( "        A-large         " ) ;

	int test ; cin>>len>>n>>test ; readln();
	cerr<<"n_test = "<<test<<endl;

	read_dic() ;

	myfor( _u, 1, test )
	{ 
		cout<<"Case #"<<_u<<": ";
		cerr<<"Running on Case #_"<<_u<<endl ;

		work() ;
		//cout<<ans<<endl;

	}

	if( !seekeof( cin ) ) cout<<("wrong")<<endl;

	fclose( stdin ); fclose( stdout );
	return 0;
}
