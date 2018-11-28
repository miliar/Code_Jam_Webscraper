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

const int Infinity = 1000000000 ;
const int MaxV = 6500 + 2  ;
const int MaxA = 1056000 ;

typedef long Tcapacity ;

struct Tnetflow;

struct Tnetflow
{
	struct Tarc
	{
		Tcapacity flow, capa;
		int from, to;
		int next; // the index of the next arc connected to from
	} arc[ MaxA+1 ];

	int V, A;
	int source, sink;
	Tcapacity totflow, delta;

	int  first[ MaxV+1 ]; // first[i] is the first arc of node i
	int  last [ MaxV+1 ]; // point to the arc in the last augmenting path
	bool used [ MaxV+1 ];

	void initialize( int n, int s, int t );
	void clearFlow();
	void addarc( int from, int to, Tcapacity c );
	Tcapacity solve();
	bool CQFdfs( int no, Tcapacity receive );
	int  opp( int ArcNo );

};

Tcapacity min( Tcapacity a, Tcapacity b ) { return a<b ? a : b ; }

void Tnetflow :: initialize( int n, int s, int t )
{	
	source=s, sink=t, V=n, A=0;
	memset( first, 0, sizeof(first[0])*V );
}

void Tnetflow :: clearFlow()
{	for( int i=1; i<=A; i++ ) arc[i].flow=0;   }

void Tnetflow :: addarc( int v1, int v2, Tcapacity c )
{
#define cur arc[A]
	A++, cur.from=v1, cur.to=v2, cur.capa=c, cur.flow=0;
	cur.next=first[v1], first[v1]=A;

	A++, cur.from=v2, cur.to=v1, cur.capa=0, cur.flow=0;
	cur.next=first[v2], first[v2]=A;
#undef cur
}

inline int Tnetflow :: opp( int no )
{	return no + ( no&1 ? 1:-1 ) ;	}

bool Tnetflow :: CQFdfs( int u, Tcapacity receive )
{
	if( u==sink ) { delta=receive; return 1; }

	used[ u ] = 1;  int ptr=last[u];
#define cur arc[ptr]
	do
	{	if( !used[ cur.to ] && cur.flow<cur.capa )
		if( CQFdfs( cur.to, min(receive,cur.capa-cur.flow) ) )
		{
			cur.flow += delta ,	arc[ opp(ptr) ].flow = -cur.flow;
			last[ u ] = ptr;
			return 1;
		}
		ptr=cur.next;  if( ptr==0 ) ptr=first[u];
	} while( ptr!=last[u] );
#undef cur

	return 0;
}

Tcapacity Tnetflow :: solve()
{
	memcpy( last, first, sizeof(last[0])*V );

	totflow = delta = 0;
	do 
	{	totflow += delta;
	memset( used, 0, sizeof(used[0])*V );
	} while( delta<Infinity && CQFdfs( source, Infinity ) );

	return totflow;
} //solve()

Tnetflow net ;


int n ,m ; 
int can_place ;

const int zx[6] = { -1 , -1 , 0 , 0 , 1 , 1 } ;
const int zy[6] = { -1 ,  1 , -1, 1 , -1, 1 } ;

int getno( int x , int y )
{
	if( x<1 || x>m || y<1 || y>n ) return -1 ;

	int p = 1 , re = 0 ;
	while( p!=y && p<=n ) re += m , p += 2 ;

	if( p==y ) return re + x ;

	p = 2 ;
	while( p!=y && p<=n ) re += m , p+=2 ;
	if( p!=y ) cout<<"\n\n\nwrong!!!!"<<endl;

	return re + x ;
}

void readin()
{
	static char s[100][100];

	scanf("%d%d",&m,&n);
	cerr<<m<<' '<<n <<endl;
	myfor( i, 1, m ) scanf("%s", &(s[i][1]) ) ;

	net.initialize( m*n+2 , 0 , m*n+1 ) ;

	myfor( i, 1, m )
	myfor( j, 1, n ) if( (j&1)==1 && s[i][j]!='x' )
	{
		int x = getno( i, j ) ;

		myfor( k , 0 , 5 )
		{
			int y = getno( i+zx[k] , j+zy[k] ) ;
			if( y!=-1 && s[i+zx[k]][j+zy[k]]!='x' )
				net.addarc( x , y , 1 ) ;
		}
	}

	can_place = 0 ;
	myfor( i, 1, m )
	myfor( j, 1, n ) if( s[i][j]!='x' )
	{
		++can_place ;
		//cerr<<i<<' '<<j<<endl;
		int x = getno( i, j ) ;

		if( (j&1)==1 ) net.addarc( 0 , x , 1 ) ;
		else net.addarc( x , m*n+1 , 1 ) ;
	}
}

void work()
{
	int flow = net.solve() ;

	cout<< can_place - flow <<endl;	
}
int main()
{
	SetFile( "   C-large.in    " ) ;

	int test ; cin>>test ; readln();
	cerr<<"n_test = "<<test<<endl;

	myfor( _u, 1, test )
	{ 
		cout<<"Case #"<<_u<<": ";
		cerr<<"Running on Case #_"<<_u<<endl ;

		readin() ;
		cerr<<"ok"<<endl;
		work() ;
		//cout<<ans<<endl;

	}

	if( !seekeof( cin ) ) cout<<("wrong")<<endl;

	fclose( stdin ); fclose( stdout );
	return 0;
}
