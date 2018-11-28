// Krzysztof Czainski
// gcc version 4.3.1 (Gentoo 4.3.1 p1.0)
// using boost-1.35.0: www.boost.org

#include <iostream>
#include <map>
#include <queue>
#include <vector>
#include <deque>
#include <iterator>
#include <boost/tuple/tuple.hpp>
#include <boost/tuple/tuple_comparison.hpp>
#include <boost/assert.hpp>

void processLine( std::istream& is, std::ostream& os, unsigned case_no );

int main()
{
	unsigned n;
	std::cin >> n;
	for ( unsigned i = 0 ; i < n ; ++i )
		processLine( std::cin, std::cout, i+1 );
}

// departure, fromB, next_departure_ready
typedef boost::tuple<unsigned,bool,unsigned> Trip;

typedef std::priority_queue< Trip, std::vector<Trip>, std::greater<Trip> > Que;

typedef std::priority_queue< unsigned, std::vector<unsigned>, std::greater<unsigned> > TrainQue;

inline unsigned readTime( std::istream& is )
{
	unsigned h, m;
	char c;
	is >> h >> c >> m;
	BOOST_ASSERT( c == ':' );
	return h * 60 + m;
}

void processLine( std::istream& is, std::ostream& os, unsigned case_no )
{
	Que que;

	{
		unsigned t, n[2];
		is >> t >> n[0] >> n[1];
		
		for ( unsigned fromB = 0 ; fromB < 2 ; ++fromB )
		{
			bool fb = static_cast<bool>(fromB);
			for ( unsigned i = 0 ; i < n[fromB] ; ++i )
			{
				unsigned dep = readTime(is), nextDepReady = readTime(is) + t;
				que.push( Trip(dep,fb,nextDepReady) );
			}
		}
	}
	
	unsigned t[2] = {0,0};
	TrainQue q[2];
	while ( !que.empty() )
	{
		const Trip& trip = que.top();
		bool fb = trip.get<1>();
		
		if ( q[fb].empty() || q[fb].top() > trip.get<0>() )
			++t[fb];
		else
			q[fb].pop();
		
		q[!fb].push( trip.get<2>() );
		
		que.pop();
	}
	
	os << "Case #" << case_no << ": " << t[0] << " " << t[1] << "\n";
}
