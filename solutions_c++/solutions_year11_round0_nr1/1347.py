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

struct Tnode
{
  char c;
  int x;
};
vector<Tnode> tasks;

deque<int> a1, a2;

int n; 

void readin()
{
  a1.clear();
  a2.clear();
  tasks.clear();
  
  cin >> n;
  myfor( i, 1, n ) {
    string s;
    int x;
    cin >> s >> x;
    Tnode v = { s[0], x };
    tasks.push_back( v );
    if( s=="O" ) a1.push_back(x);
    else if( s=="B") a2.push_back(x);
    else assert(false);
  }
}

void work()
{
  int ans = 0 ;
  int cur1 = 1, cur2 = 1;

  myforv( i, tasks ) {
    if( tasks[i].c == 'O' ) {
      assert( !a1.empty() && a1.front()==tasks[i].x );
      int t = myabs( tasks[i].x - cur1 ) + 1 ;
      ans += t ;
      cur1 = a1.front();
      a1.pop_front();
      
      if( !a2.empty() ) {
	int step2go = myabs( a2.front() - cur2 );
	step2go = max( 0, step2go - t );
	cur2 = a2.front() + step2go;
      }
    }
    else {
      assert( !a2.empty() && a2.front()==tasks[i].x );
      int t = myabs( tasks[i].x - cur2 ) + 1 ;
      cur2 = a2.front();
      ans += t ;
      a2.pop_front();

      if( !a1.empty() ) {
	int step2go = myabs( a1.front() - cur1 );
	step2go = max( 0, step2go - t );
	cur1 = a1.front() + step2go;
      }
    } //else

    //cout<< "*" << ans <<endl;
  } //for i

  assert( a1.empty() && a2.empty() );
  
  cout << ans << endl;
}

int main()
{
	SetFile( "       A-large.in         " ) ;

	int test ; cin>>test ; readln(cin);
	cerr<<"#test = "<<test<<endl;

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
