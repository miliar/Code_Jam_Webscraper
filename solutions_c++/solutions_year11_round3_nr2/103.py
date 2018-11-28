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

typedef long long int64;

int64 finish_time;
int n;
int L;
deque<int64> a;
vector<int64> lens;

void readin()
{
  int C;
  cin >> L >> finish_time >> n >> C;
  cerr << " C=" << C << endl;
  
  lens.clear();
  myfor (i, 1, C) {
    int64 t; cin >> t;
    lens.push_back(t);
  }
  assert( lens.size() == C );
  assert( seekeoln(cin) );

  a.clear();
  myfor (i, 0, n-1) {
    a.push_back( lens[ i%C ] );
  }
}

int64 curtime;

void stage1()
{
  while (!a.empty() && curtime < finish_time) {
    int64 len = a.front();
    int64 left_time = finish_time - curtime;
    
    if (len*2 <= left_time) {
      curtime += len*2;
      a.pop_front();
    } else {
      assert( left_time % 2 == 0 );

      curtime += left_time;
      len -= left_time / 2;
      a.pop_front();
      a.push_front(len);
    }
  }
}

void stage2() {
  if (a.empty()) return;

  sort(a.begin(), a.end(), greater<int64>());

  int to_build = L;
  myforv (i, a) {
    if (to_build > 0) {
      curtime += a[i];
      --to_build;
    } else {
      curtime += a[i]*2;
    }
  }
}

void work()
{
  curtime = 0;
  stage1();
  stage2();
  cout << curtime << endl;
}

int main()
{
	SetFile( "  B-large         " ) ;

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
