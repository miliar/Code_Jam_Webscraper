#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>

using namespace std;

int t, na, nb;

#define Time pair<int, int>

//vector<Time> A;
//vector<Time> B;

int avaliable[ 2 ];

struct Point{
	Time t1, t2;
	bool station;
	Point( Time t1, Time t2, bool station )
	{
		this->t1 = t1;
		this->t2 = t2;
		this->station = station;
	}
	Point(){}
} ;
vector<Point> all;



bool operator < ( const Point & a, const Point & b )
{
	if( a.t1 != b.t1 )
		return a.t1 < b.t1;
	return a.t2 < b.t2;
}
struct Point1{
	Time t1, t2;
	bool station;
	Point1( Point & p )
	{
		this->t1 = p.t1;
		this->t2 = p.t2;
		this->station = p.station;
	}
	Point1(){}
} ;
multiset<Point1> wait;
bool operator < ( const Point1 & a, const Point1 & b )
{
	if( a.t2 != b.t2 )
		return a.t2 < b.t2;
	return a.t1 < b.t1;
}

int main()
{
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	int test;
	scanf( "%d", & test );
	int ind = 1;
	for( ; test; --test )
	{
		scanf( "%d%d%d", & t, & na, & nb );
		all.clear();
		for( int i = 0; i < na; ++i )
		{
			int a, b, c, d;
			scanf( "%d:%d %d:%d", & a, & b, & c, & d );
			//A.push_back( make_pair( a, b ) );
			all.push_back( Point( make_pair( a, b ), make_pair( c, d ), 0 ) );
		}
		for( int i = 0; i < nb; ++i )
		{
			int a, b, c, d;
			scanf( "%d:%d %d:%d", & a, & b, & c, & d );
			//B.push_back( make_pair( a, b ) );
			all.push_back( Point( make_pair( a, b ), make_pair( c, d ),  1 ) );
		}
		wait.clear();
		sort( all.begin(), all.end() );
		avaliable[ 0 ] = avaliable[ 1 ] = 0;
		int ans[ 2 ];
		ans[ 0 ] = ans[ 1 ] = 0;
		for( vector<Point> :: iterator i = all.begin();
			i != all.end(); ++i )
		{
			while( !wait.empty() )
			{
				multiset<Point1> :: iterator p = wait.begin();
				//Point1 p = wait.begin();
				if( p->t2 <= i->t1 )
				{
					avaliable[ p->station ]++;
					wait.erase( p );

				}else break;
			}
			if( avaliable[ i->station ] )
				--avaliable[ i->station ];
			else
				++ans[ i->station ];
			i->t2.second += t;
			if( i->t2.second >= 60 )
			{
				++i->t2.first;
				i->t2.second -= 60;
			}
			i->station = !i->station;
			wait.insert( Point1( *i ) );
		}
		printf( "Case #%d: %d %d\n", ind, ans[ 0 ], ans[ 1 ] );
		++ind;
		
	}
	return 0;
}