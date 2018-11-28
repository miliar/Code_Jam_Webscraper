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

const int MAXN = 3000  ;
const int mod = 1000000007 ;

struct Tpoint { int x, y ; int bird ; };

Tpoint a[ MAXN+1 ] ;
int n, m;

int cnt_good ;

void readin()
{
	cnt_good = 0 ;

	cin>>n ;
	myfor( i, 1, n )
	{
		cin>>a[i].x>>a[i].y ;
		string s ;
		cin>>s;
		if( s=="BIRD" ) a[i].bird = 1 ;
		else if( s=="NOT" ) { a[i].bird = 0 ; cin>>s; }
		else cout<<"WRong !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"<<endl;

		if( a[i].bird == 1 ) ++ cnt_good ;
	}
}

int minx , maxx ;
int miny , maxy ;

bool checkgood( Tpoint cur )
{
	if( cur.x >= minx && cur.x <=maxx && cur.y>=miny && cur.y<=maxy ) return true;
	else return false ;
}

bool checkbad( Tpoint cur )
{
	int tminx = minx , tmaxx = maxx ;
	int tminy = miny , tmaxy = maxy ;

	checkmin( minx, cur.x ) ; checkmax( maxx, cur.x );
	checkmin( miny, cur.y ) ; checkmax( maxy, cur.y );

	int i;
	for( i=1; i<=n; ++i )
	{
		if( a[i].bird != 1 && checkgood( a[i] ) ) break;
		if( a[i].bird == 1 && ! checkgood( a[i] ) ) break ;
	}

	minx = tminx , maxx = tmaxx ;
	miny = tminy , maxy = tmaxy ;

	if( i<=n ) return true ;
	else return false;
}

void work()
{
	//if( cnt_good == 0 ) { special(); return; }

	minx = miny = 999999999 ;
	maxx = maxy = -1 ;
	myfor( i, 1, n )
		if( a[i].bird==1 )
		{
			checkmin( minx, a[i].x ) ; checkmax( maxx, a[i].x );
			checkmin( miny, a[i].y ) ; checkmax( maxy, a[i].y ) ;
		}

	Tpoint cur ;

	cin>>m ;
	myfor( i, 1, m )
	{
		cin>>cur.x>>cur.y ;

		if( checkgood( cur ) ) 
		{
			cur.bird = 1 ;
			//a[ ++n ] = cur ;
			cout<<"BIRD"<<endl;
		}
		else if( checkbad(cur) ) 
		{
			cur.bird = 0 ;
			//a[ ++n ] = cur ;
			cout<<"NOT BIRD"<<endl;
		}
		else
		{
			cur.bird = -1 ;
			//a[ ++n ] = cur ;
			cout<<"UNKNOWN"<<endl;
		}
	}
}




int main()
{
	SetFile( "    A-large.in     " ) ;

	int test ; cin>>test ; readln();
	cerr<<"n_test = "<<test<<endl;

	myfor( _u, 1, test )
	{ 
		cout<<"Case #"<<_u<<": ";
		cerr<<"Running on Case #_"<<_u<<endl ;

		readin() ;
		cout<<endl;
		work() ;
		//cout<<ans<<endl;

	}

	if( !seekeof( cin ) ) cout<<("wrong")<<endl;

	fclose( stdin ); fclose( stdout );
	return 0;
}
