#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <fstream>
#include <set>
#include <map>
#include <queue>
using namespace std;

#define mysize(X) ((int)X.size())
#define myfor(i,c,d) for( int i=(c); i<=(d); ++i )
#define myforv(i,V) for( int i=0; i<mysize(V); ++i )
template<class T>void checkmin( T&a, const T&b ){if(b<a)a=b;}

bool seekeof()
{
	int t;  while( (t=cin.peek())!=EOF && t<=' ' ) cin.get();
	return t==EOF ;
}

ifstream fin ;
ofstream fout ;

struct node 
{
	node( double t , int c ) { time=t; code=c; }
	double time ;
	int code ; // -1: leave A   -2: leave B   1: arrive at A  2: arrive at B
};

bool operator < ( const node &a , const node &b )
{
	return a.time > b.time ;
}

priority_queue< node > que ;

int n , na, nb ;
int need_a, need_b ;
int delay ;


void readin()
{
	while( !que.empty() ) que.pop();

	cin>>delay ;
	cin>>na>>nb ;

	int h, minute ;
	myfor( i, 1, na )
	{
		scanf("%d:%d",&h,&minute);
		minute += h*60 ;
		que.push( node( minute+0.01, -1 ) ) ;

		scanf("%d:%d",&h,&minute);
		minute += h*60 ;
		que.push( node( minute+delay, 2 ) ) ;
	}

	myfor( i, 1, nb )
	{
		scanf("%d:%d",&h,&minute);
		minute += h*60 ;
		que.push( node( minute+0.01, -2 ) ) ;

		scanf("%d:%d",&h,&minute);
		minute += h*60 ;
		que.push( node( minute+delay, 1 ) ) ;
	}	
}

void work()
{
	int lefta , leftb ;
	int cnta , cntb ;

	lefta = leftb = cnta = cntb = 0 ;

	node e( 0, 0 ) ;
	while( !que.empty() )
	{
		e = que.top(); que.pop() ;
		if( e.code == 1 ) ++lefta ; else
		if( e.code == 2 ) ++leftb ; else
		if( e.code == -1 )
		{
			if( lefta > 0 ) -- lefta ;
			else ++cnta ;
		} else
		if( e.code == -2 )
		{
			if( leftb > 0 ) -- leftb ;
			else ++cntb ;
		}
	}

	cout<< cnta << ' ' << cntb <<endl;
}

int main()
{
	freopen( "B-large.in", "r", stdin );
	freopen( "B-large.out", "w", stdout );
	//freopen( "in.txt", "r", stdin );
	//freopen( "out.txt", "w", stdout );

	int test ; cin>>test ;

	myfor( i, 1, test )
	{
		cout<<"Case #"<<i<<": ";

		readin();
		work();
	}

	if( !seekeof() ) cout<<("wrong")<<endl;
	
	fclose( stdin ); fclose( stdout );
	return 0;
}