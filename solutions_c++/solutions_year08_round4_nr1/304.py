#include <myheading.h>

void SetFile( string s )
{
	string::size_type p = s.find('.') ;
	if( p!=string::npos ) s = s.substr( 0, p ) ;
	string sin  = s+".in" ;  freopen( sin. c_str() , "r" , stdin  );
	string sout = s+".out";  freopen( sout.c_str() , "w" , stdout );
}

#define myfor(i,c,d) for( int i=(c); i<=(d); ++i )

const int MAXN = 10000  ;
const int mod = 1000000007 ;


int n , aim ; 

int type[ MAXN+1 ] ;
int change[ MAXN+1 ] ;

void readin()
{
	cin>>n>>aim ;
	
	int i ;
	for( i=1; i<=(n-1)/2; ++i )
		cin>>type[i]>>change[i] ;

	for( ; i<=n; ++i )
		cin>>type[i] ;
}

int f[ MAXN+1 ][2] ;

int dp( int p, int aim )
{
	int &re = f[p][aim] ;
	if( re!=-1 ) return re ;

	if( p+p > n )
	{
		if( type[p]==aim ) return re = 0 ;
		else return re = 20000 ;
	}

	re = 20000 ;

	int tmp, tmp1, tmp2 ;
	int curtype , base ;

	curtype = type[p] ;

	if( curtype==1 )
	{
		if( aim==1 )
		{
			tmp = dp( p+p , 1 ) + dp( p+p+1, 1 ) ;
			if( tmp < re ) re = tmp ;
		}
		else
		{
			tmp1 = dp( p+p , 0 ) ;
			tmp2 = dp( p+p+1 , 0 ) ;
			if( tmp1 < re ) re = tmp1 ;
			if( tmp2 < re ) re = tmp2 ;
		}
	}
	else if( curtype == 0 )
	{
		if( aim==0 )
		{
			tmp = dp( p+p , 0 ) + dp( p+p+1, 0 ) ;
			if( tmp < re ) re = tmp ;
		}
		else
		{
			tmp1 = dp( p+p , 1 ) ;
			tmp2 = dp( p+p+1 , 1 ) ;
			if( tmp1 < re ) re = tmp1 ;
			if( tmp2 < re ) re = tmp2 ;
		}
	}

	if( change[p]==0 ) return re ;

	curtype = 1 - type[p] ;

	if( curtype==1 )
	{
		if( aim==1 )
		{
			tmp = dp( p+p , 1 ) + dp( p+p+1, 1 ) ;
			if( tmp+1 < re ) re = tmp+1 ;
		}
		else
		{
			tmp1 = dp( p+p , 0 ) ;
			tmp2 = dp( p+p+1 , 0 ) ;
			if( tmp1+1 < re ) re = tmp1+1 ;
			if( tmp2+1 < re ) re = tmp2+1 ;
		}
	}
	else if( curtype == 0 )
	{
		if( aim==0 )
		{
			tmp = dp( p+p , 0 ) + dp( p+p+1, 0 ) ;
			if( tmp+1 < re ) re = tmp+1 ;
		}
		else
		{
			tmp1 = dp( p+p , 1 ) ;
			tmp2 = dp( p+p+1 , 1 ) ;
			if( tmp1+1 < re ) re = tmp1+1 ;
			if( tmp2+1 < re ) re = tmp2+1 ;
		}
	}

	return re ;
}




void work()
{
	memset( f, 255, sizeof(f) );

	int re = dp( 1, aim ) ;
	if( re > n ) 
		cout<<"IMPOSSIBLE"<<endl;
	else 
		cout<<re<<endl;	
}

int main()
{
	SetFile( "A-large.in" ) ;
	
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
