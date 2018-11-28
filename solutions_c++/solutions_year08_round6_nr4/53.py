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

const int MAXN = 50 ;
const int mod = 1000000007 ;

struct Tpoint { int x, y ; int bird ; };

int n, m;

int tu1[MAXN+1][MAXN+1] ;
int tu2[MAXN+1][MAXN+1] ;
int tu3[MAXN+1][MAXN+1] ;

int no[ MAXN+1 ];

void readin()
{
	memset( tu1, 0, sizeof(tu1) );

	cin>>n ;
	myfor( i, 1, n-1 )
	{
		int x, y ;
		cin>>x>>y ;
		tu1[x][y] = tu1[y][x] = 1 ;
	}


	memset( tu2, 0, sizeof(tu2) );

	cin>>m ;
	myfor( i, 1, m-1 )
	{
		int x, y ;
		cin>>x>>y ;
		tu2[x][y] = tu2[y][x] = 1 ;
	}	
}

bool check()
{
	//memset( tu3, 0, sizeof(tu3[0])*(m+1) ) ;

	myfor( i, 1, m )
	myfor( j, i, m )
	{
		if( tu2[i][j] != tu1[ no[i] ][ no[j] ] ) return false ;
	}

	return true ;
}

bool used[ MAXN+1 ]  ;

bool dfs( int k )
{
	if( k>m )
	{
		return check() ;
	}

	myfor( i, 1, n ) if( !used[i] )
	{
		no[k] = i; used[i] = true ;
		if( dfs( k+1 ) ) return true ;
		used[i] = false ;
	}

	return false; 
}

void work()
{
	//if( cnt_good == 0 ) { special(); return; }

	memset( used, 0, sizeof(used) ) ;
	if( dfs( 1 ) ) cout<<"YES"<<endl;
	else cout<<"NO"<<endl;	
}




int main()
{
	SetFile( "   D-small-attempt1.in   " ) ;
	//SetFile( "   data   " ) ;

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
