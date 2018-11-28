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

const int maxN = 108;
int f[ maxN + 1 ][ maxN + 1 ];
int h, w, r;
const int PRIME = 10007;
void readin()
{
    int u, v;
    memset(f, 0, sizeof(f));
	scanf("%d%d%d",&h, &w, &r) ;
	myfor( i, 1, r )
    {
       scanf("%d%d", &u, &v);
       f[u][v] = -1;
    }
}


void work()
{
    f[1][1] = 1;
    myfor( i, 2, h )
       myfor( j, 2 ,w )
          if( f[i][j] != -1 ) f[i][j] = ( f[i-2][j-1] + f[i-1][j-2] )%PRIME;
          else f[i][j] = 0;
    cout << f[h][w] << endl;
}

int main()
{
	SetFile( "   D-small-attempt0.in   " ) ;

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
