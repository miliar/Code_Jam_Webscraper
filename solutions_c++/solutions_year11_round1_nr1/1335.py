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

int N, a, b;

void readin()
{
  cin >> N >> a >> b;
}

bool special_check() {
  if( b != 100 && b != 0 ) return false;
  
  if( a == b ) cout << "Possible" << endl;
  else cout << "Broken" << endl;

  return true;
}

void work()
{
  if( special_check() ) return;

  int min_n = 100;
  while (a%2==0 && min_n%2==0) {
    a /= 2;
    min_n /= 2;
  }

  while (a%5==0 && min_n%5==0) {
    a /= 5;
    min_n /= 5;
  }

  if (min_n <= N) cout << "Possible" << endl;
  else cout << "Broken" << endl;

}

int main()
{
  SetFile( "  A-small-attempt1         " ) ;

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
