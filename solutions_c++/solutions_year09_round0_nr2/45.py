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

const int MAXN = 100 ;

int a[ MAXN+1 ][ MAXN+1 ] ;
int m, n ;

void readin()
{
	cin>>m>>n ;
	myfor( i, 1, m )
		myfor( j, 1, n ) cin>>a[i][j] ;
}

int f[ MAXN+1 ][ MAXN+1 ] ;
int cnt ;

int dfs( int x, int y )
{
	if( f[x][y] >= 0 ) return f[x][y] ;

	int tx, ty, min = a[x][y] ;

	if( x>1 && a[x-1][y] < min ) tx = x-1 , ty = y , min = a[x-1][y] ;
	if( y>1 && a[x][y-1] < min ) tx = x , ty = y-1 , min = a[x][y-1] ;
	if( y<n && a[x][y+1] < min ) tx = x , ty = y+1 , min = a[x][y+1] ;
	if( x<m && a[x+1][y] < min ) tx = x+1 , ty = y , min = a[x+1][y] ;

	if( min < a[x][y] ) return f[x][y] = dfs( tx, ty ) ;
	else
	{
		++cnt ;
		return f[x][y] = cnt ;
	}
}


void work()
{
	memset( f, 255, sizeof(f) );
	cnt = 0 ;

	myfor( i, 1, m )
		myfor( j, 1, n )
			if( f[i][j] == -1 ) dfs( i, j ) ;
}

void outans()
{
	myfor( i, 1, m )
	{
		myfor( j, 1, n )
		{
			cout<<(char)( 'a' + f[i][j]-1 );
			if( j!=n ) cout<<' ';
		}
		cout<<endl;
	}			
}

int main()
{
	SetFile( "       B-large        " ) ;

	int test ; cin>>test ; readln();
	cerr<<"n_test = "<<test<<endl;

	myfor( _u, 1, test )
	{ 
		cout<<"Case #"<<_u<<":\n";
		cerr<<"Running on Case #_"<<_u<<endl ;

		readin() ;
		work() ;
		outans() ;

	}

	if( !seekeof( cin ) ) cout<<("wrong")<<endl;

	fclose( stdin ); fclose( stdout );
	return 0;
}
