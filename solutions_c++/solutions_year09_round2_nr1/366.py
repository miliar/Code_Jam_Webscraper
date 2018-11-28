// CodeJam.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//

#include <tchar.h>

#include <iomanip>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>

#include <memory>

#include <vector>
#include <list>
#include <set>
#include <map>

#include <algorithm>
#include <numeric>

#include <cmath>
#include <limits>

using namespace std;


// -------------------------------------------------------------------------

#if 0
//#if 1

#include <windows.h>

class DebugStreambuf : public std::streambuf 
{
public:
	DebugStreambuf(void)
	{
		m_buf[0] = '\0' ;
		m_buf[1] = '\0' ;
	}

	virtual int_type overflow( int_type i_char = EOF )
	{
		if( i_char != EOF )
		{
			m_buf[0] = (char)i_char;
			OutputDebugString( m_buf );
		}
		return i_char;
	}

private:
	static const size_t BUFFER_SIZE = 2;
	char m_buf[BUFFER_SIZE];
};

class DebugStream : public std::ostream
{
public:
	DebugStream(void) : std::ostream( &m_buf )
	{}

private:
	DebugStreambuf m_buf;
};

DebugStream dout;

#endif

// -------------------------------------------------------------------------




template<typename To, typename From>
To lexical_cast(const From& i_from)
{
	To result;
	std::stringstream ss;

	ss << i_from;
	ss >> result;

	return result;
}


template<typename T> inline T (min)( const T& a , const T& b )                           { return a < b ? a : b ;                                                          }
template<typename T> inline T (min)( const T& a , const T& b , const T& c )              { return (math_lib::min)( (math_lib::min)( a , b ) , c ) ;                        }
template<typename T> inline T (min)( const T& a , const T& b , const T& c , const T& d ) { return (math_lib::min)( (math_lib::min)( a , b ) , (math_lib::min)( c , d ) ) ; }
template<typename T> inline T (max)( const T& a , const T& b )                           { return a > b ? a : b ;                                                          }
template<typename T> inline T (max)( const T& a , const T& b , const T& c )              { return (math_lib::max)( (math_lib::max)( a , b ) , c ) ;                        }
template<typename T> inline T (max)( const T& a , const T& b , const T& c , const T& d ) { return (math_lib::max)( (math_lib::max)( a , b ) , (math_lib::max)( c , d ) ) ; }

template<typename T> inline T clamp( const T& i_min , const T& i_value , const T& i_max ) 
{
#ifdef _DEBUG
	assert( i_min <= i_max );
#endif

	return (math_lib::min)( (math_lib::max)( i_min , i_value ) , i_max );
}


template<typename T> inline T pow2( const T& v ) { return v * v ;             }
template<typename T> inline T pow3( const T& v ) { return v * v * v ;         }
template<typename T> inline T pow4( const T& v ) { return pow2( v * v ) ;     }
template<typename T> inline T pow5( const T& v ) { return pow2( v * v ) * v ; }
template<typename T> inline T pow6( const T& v ) { return pow3( v * v ) ;     }
template<typename T> inline T pow7( const T& v ) { return pow3( v * v ) * v ; }
template<typename T> inline T pow8( const T& v ) { return pow4( v * v ) ;     }


template<typename T> inline T gcd( T a , T b )
{
	if( b > a ) (std::swap)( a , b );
	while( ( a = a % b ) != 0 ) (std::swap)( b , a );
	return b;
}

template<typename T> inline T lcm( const T& a , const T& b )
{
	return a * b / gcd( a , b );
}


#define foreach( TYPE_ , CONTAINER_ , ITERATOR_ ) for( TYPE_::iterator ITERATOR_ = (CONTAINER_).begin() ; ITERATOR_ != (CONTAINER_).end() ; ++ITERATOR_ )
#define c_foreach( TYPE_ , CONTAINER_ , ITERATOR_ ) for( TYPE_::const_iterator ITERATOR_ = (CONTAINER_).begin() ; ITERATOR_ != (CONTAINER_).end() ; ++ITERATOR_ )




// ------------------------------------------------------------------------

void end_prog(void)
{
	cout << "end" << endl;
	getchar();
}

class node
{
public:
	string feature;
	double  weight;

	auto_ptr<node> n0;
	auto_ptr<node> n1;

	bool is_term;
};


void make_node( node& nd , istream& is )
{
	nd.is_term = false;

	vector<string> sary;
	{
		char c = 0;
		while( c != '(' )
		{
			is >> c;
		}

		bool in_w = false;
		for(;;)
		{
			is.read( &c , 1 );
			if     ( c == ' '  ) in_w = false;
			else if( c == '\n' ) in_w = false;
			else
			{
				if( !in_w )
				{
					if( sary.size() == 2 ) break;
					sary.push_back("");
				}

				sary.back().push_back( c );
				in_w = true;
			}

			if( is.peek() == ')' ) break;
			if( is.peek() == '(' ) break;
		}
	}

	nd.is_term = ( sary.size() == 1 );

	nd.weight = lexical_cast<double>( sary[0] );

	if( !nd.is_term )
	{
		nd.feature = sary[1];
		nd.n0.reset( new node() );
		nd.n1.reset( new node() );
		make_node( *nd.n0.get() , is );
		make_node( *nd.n1.get() , is );
	}

	{
		char c = 0;
		while( c != ')' ) is >> c;
	}
}

void core()
{
	ifstream ifs("in.txt");
	ofstream ofs("out.txt");

	int T;
	ifs >> T;

	if( ifs.peek() == '\n' )
	{
		char c;
		ifs.read( &c , 1 );
	}

	for( int i = 0 ; i < T ; ++i )
	{
		ofs << "Case #" << (i+1) << ":" << endl;

		node root;

		make_node( root , ifs );

		int N;
		ifs >> N;

		for( int i = 0 ; i < N ; ++i )
		{
			string anim;
			int params;
			ifs >> anim;
			ifs >> params;

			set<string> strs;
			for( int j = 0 ; j < params ; ++j )
			{
				string s;
				ifs >> s;
				strs.insert(s);
			}

			node* n = &root;

			double tw = n->weight;
			while( !n->is_term )
			{
				if( strs.find( n->feature ) != strs.end() )
					n = n->n0.get();
				else
					n = n->n1.get();

				tw *= n->weight;
			}

			ofs << fixed << setprecision(7) << tw << endl;
		}
	}

	int ii = 2+34;
}

int _tmain(int argc, _TCHAR* argv[])
{
	core();

	//end_prog();

	return 0;
}

