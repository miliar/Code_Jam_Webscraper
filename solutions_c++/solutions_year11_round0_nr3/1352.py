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

const int MAXN = 500000  ;
const int mod = 1000000007 ;
int n;

void readin()
{
  cin >> n ;
}

void work()
{
  int minx = 0x7fffffff ;
  int sum = 0 ;
  int sum_xor = 0 ;
  int x ;
  myfor( i, 1, n ) {
    cin >> x ;
    sum += x ;
    sum_xor ^= x ;
    checkmin( minx, x );
  }

  if( sum_xor == 0 ) cout << sum - minx << endl;
  else cout << "NO" <<endl;
    

}

int main()
{
	SetFile( "         C-large         " ) ;

	int test ; cin>>test ; readln(cin);
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
