#include "myheading.h"

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


////////////////////////////////////////////////////////////////////

const int mod = 1000000007 ;

const int MAXN = 1010  ;

struct Tcycle
{	int m;  int c[ MAXN+1 ] , l[ MAXN+1 ] ;  };



double g[ MAXN+1 ];
double s[ MAXN+1 ];
int    a[ MAXN+1 ];
Tcycle cycle ;
int    n;

double ans;

// convert permutation to cycle
// 要保证a[1..n]是n的一个排列 
void p_to_c( const int *a, Tcycle &b  )
{
	static bool ok[ MAXN+1 ];
	memset( ok, 1, sizeof(ok[0])*(n+1) );
	
	int i, top, p;
	for( b.l[ b.m=0 ]=0, top=0, i=1; i<=n; ++i ) if( ok[i] )
	{
		for( p=i; ok[p]; p=a[p] ) b.c[ ++top ] = p , ok[p]=0 ;
		b.l[ ++b.m ] = top ;
	}
	for( i=b.m; i>1; --i ) b.l[i] -= b.l[i-1] ;
}


void readin()
{
  cin >> n;
  myfor( i, 1, n ) cin >> a[i];
  p_to_c( a, cycle );
}

void init()
{
  g[0] = g[1] = 0;
  s[0] = s[1] = 0;
  myfor( i, 2, MAXN ) {
    g[i] = ( 2.0 * s[i-1] + (i-1) ) / (double)(i-1) ;
    s[i] = s[i-1] + g[i] ;
  }
}

void work()
{
  double ans = 0 ;
  myfor( i, 1, cycle.m ) {
    if( cycle.l[i] > 1 ) ans += 1.0 + g[ cycle.l[i] ];
  }

  printf("%.9lf\n", ans);
}

int main()
{
	SetFile( "       D-large         " ) ;

	int test ; cin>>test ; readln(cin);
	cerr<<"n_test = "<<test<<endl;

	myfor( _u, 1, test )
	{ 
		cout<<"Case #"<<_u<<": ";
		cerr<<"Running on Case #_"<<_u<<endl ;

		readin() ;
		init() ;
		work() ;
		//cout<<ans<<endl;

	}

	if( !seekeof( cin ) ) cout<<("wrong")<<endl;

	fclose( stdin ); fclose( stdout );
	return 0;
}
