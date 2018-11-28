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

const int MAXN = 50;
const int MAXM = 50;

char s[MAXM+10][MAXN+10];
int m, n;

void readin()
{
  cin >> m >> n ;
  myfor (i, 1, m) {
    cin >> (s[i]+1) ;
    cerr << (s[i]+1) << endl;
  }
}

int update() {
  bool found = false;
  int i, j;
  for (i=1; i<=m; ++i) {
    for (j=1; j<=n; ++j)
      if (s[i][j] == '#') {
        found = true;
        break;
      }
    if (found) break;
  }

  if (!found) return 0;

  //cerr << "found at " << i << ' ' << j << endl;
  
  if (i+1 > m || j+1 > n) return -1;

  assert(s[i][j] == '#');
  if (s[i+1][j] == '#' && s[i][j+1] == '#' && s[i+1][j+1] == '#') {
    s[i][j] = '/';
    s[i+1][j+1] = '/';
    s[i][j+1] = '\\';
    s[i+1][j] = '\\';
    //cerr << "ok " << i << ' ' << j << endl;
    return 1;
  }
  else {
    return -1;
  }

}

  

void work()
{
  int flag;

  do {
    flag = update();
  } while (flag == 1);

  cout << endl;
  
  if (flag == 0) {
    myfor (i, 1, m) cout << (s[i]+1) << endl;
  } else {
    assert(flag == -1);
    cout << "Impossible" << endl;
  }
}

int main()
{
	SetFile( "         A-large   " ) ;

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
