// CodeJam.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//

#include <tchar.h>

#include <iostream>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <string>

#include <memory>

#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>

#include <algorithm>
#include <numeric>

#include <cmath>
#include <limits>

#include <cassert>

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




template<typename T>
class matrix
{
public:
	matrix(void);
	matrix(size_t num_x, size_t num_y);
	matrix(size_t num_x, size_t num_y, const T& initial_value);
	matrix(const matrix<T>& m);

	T* v(void);
	const T* v(void) const;

	T& at(size_t idx_v);
	const T& at(size_t idx_v) const;
	T& operator()(size_t idx_x, size_t idx_y);
	const T& operator()(size_t idx_x, size_t idx_y) const;
	T& operator[](size_t idx_v);
	const T& operator[](size_t idx_v) const;

	T& at(size_t idx_x, size_t idx_y);
	const T& at(size_t idx_x, size_t idx_y) const;
	T& operator()(size_t idx_v);
	const T& operator()(size_t idx_v) const;

	void resize(size_t num_x, size_t num_y);
	void resize(size_t num_x, size_t num_y, const T& initial_value);

	void clear(void);

	size_t size(void) const;
	size_t size_x(void) const;
	size_t size_y(void) const;

	bool empty(void) const;

	void set(const matrix<T>& m);
	matrix<T>& operator=(const matrix<T>& m);

	bool equals(const matrix<T>& m);
	bool operator==(const matrix<T>& m);
	bool operator!=(const matrix<T>& m);

	typedef typename std::vector<T>::iterator               iterator;
	typedef typename std::vector<T>::const_iterator         const_iterator;
	typedef typename std::vector<T>::reverse_iterator       reverse_iterator;
	typedef typename std::vector<T>::const_reverse_iterator const_reverse_iterator;
	iterator               begin  (void);
	iterator               end    (void);
	reverse_iterator       rbegin (void);
	reverse_iterator       rend   (void);
	const_iterator         begin  (void) const;
	const_iterator         end    (void) const;
	const_reverse_iterator rbegin (void) const;
	const_reverse_iterator rend   (void) const;

protected:
	size_t m_size_x;
	size_t m_size_y;
	std::vector<T> buf;
};


// implement

template<typename T> inline
matrix<T>::matrix(void)
	: m_size_x( 0 )
	, m_size_y( 0 )
{}

template<typename T> inline
matrix<T>::matrix(size_t num_x, size_t num_y)
	: m_size_x( num_x )
	, m_size_y( num_y )
{
	buf.resize( m_size_x * m_size_y );
}

template<typename T> inline
matrix<T>::matrix(size_t num_x, size_t num_y, const T& initial_value)
	: m_size_x( num_x )
	, m_size_y( num_y )
{
	buf.resize( m_size_x * m_size_y );
	std::fill( buf.begin() , buf.end() , initial_value );
}

template<typename T> inline
matrix<T>::matrix(const matrix<T>& m)
{
	buf = m.buf;
	m_size_x = m.size_x();
	m_size_y = m.size_y();
}


template<typename T> inline
T* matrix<T>::v()
{
	if( buf.empty() ) return NULL    ;
	else              return &buf[0] ;
}
template<typename T> inline
const T* matrix<T>::v() const
{
	if( buf.empty() ) return NULL    ;
	else              return &buf[0] ;
}


template<typename T> inline
T& matrix<T>::at(size_t idx_v)
{
	return buf[idx_v];
}
template<typename T> inline
const T& matrix<T>::at(size_t idx_v) const
{
	return buf[idx_v];
}
template<typename T> inline
T& matrix<T>::operator()(size_t idx_v)
{
	return at(idx_v);
}
template<typename T> inline
const T& matrix<T>::operator()(size_t idx_v) const
{
	return at(idx_v);
}
template<typename T> inline
T& matrix<T>::operator[](size_t idx_v)
{
	return at( idx_v );
}
template<typename T> inline
const T& matrix<T>::operator[](size_t idx_v) const
{
	return at( idx_v );
}


template<typename T> inline
T& matrix<T>::at(size_t idx_x, size_t idx_y)
{
#ifdef _DEBUG
	// Matrix subscript out of range
	assert( idx_x < m_size_x && idx_y < m_size_y );
#endif
	return buf[ idx_x + m_size_x * idx_y ];
}
template<typename T> inline
const T& matrix<T>::at(size_t idx_x, size_t idx_y) const
{
#ifdef _DEBUG
	// Matrix subscript out of range
	assert( idx_x < m_size_x && idx_y < m_size_y );
#endif
	return buf[ idx_x + m_size_x * idx_y ];
}
template<typename T> inline
T& matrix<T>::operator()(size_t idx_x,size_t idx_y)
{
	return at( idx_x , idx_y );
}
template<typename T> inline
const T& matrix<T>::operator()(size_t idx_x, size_t idx_y) const
{
	return at( idx_x , idx_y );
}


template<typename T> inline
void matrix<T>::resize(size_t num_x, size_t num_y)
{
	m_size_x = num_x ;
	m_size_y = num_y ;
	buf.resize( m_size_x * m_size_y );
}
template<typename T> inline
void matrix<T>::resize(size_t num_x, size_t num_y, const T& initial_value)
{
	m_size_x = num_x ;
	m_size_y = num_y ;
	buf.resize( m_size_x * m_size_y );
	std::fill( buf.begin() , buf.end() , initial_value );
}


template<typename T> inline
void matrix<T>::clear(void)
{
	m_size_x = 0;
	m_size_y = 0;
	buf.clear();
}


template<typename T> inline
size_t matrix<T>::size(void) const
{
	return buf.size();
}
template<typename T> inline
size_t matrix<T>::size_x(void) const
{
	return m_size_x;
}
template<typename T> inline
size_t matrix<T>::size_y(void) const
{
	return m_size_y;
}

template<typename T> inline
bool matrix<T>::empty(void) const
{
	return buf.empty();
}


template<typename T> inline
void matrix<T>::set(const matrix<T>& m)
{
	buf = m.buf;
	m_size_x = m.size_x() ;   m_size_y = m.size_y() ;
}
template<typename T> inline
matrix<T>& matrix<T>::operator=(const matrix<T>& m)
{
	set( m ) ;
	return (*this);
}


template<typename T> inline
bool matrix<T>::equals(const matrix<T>& m)
{
	if( m_size_x != m.m_size_x || m_size_y != m.m_size_y ) return false;
	for(size_t i=0;i<m.size();i++) if( (*this)(i) != m(i) ) return false;
	return true;
}
template<typename T> inline
bool matrix<T>::operator==(const matrix<T>& m)
{
	return equals( m );
}
template<typename T> inline
bool matrix<T>::operator!=(const matrix<T>& m)
{
	return !equals( m );
}


template<typename T> inline
typename matrix<T>::iterator matrix<T>::begin(void)
{
	return buf.begin();
}
template<typename T> inline
typename matrix<T>::iterator matrix<T>::end(void)
{
	return buf.end();
}
template<typename T> inline
typename matrix<T>::reverse_iterator matrix<T>::rbegin(void)
{
	return buf.rbegin();
}
template<typename T> inline
typename matrix<T>::reverse_iterator matrix<T>::rend(void)
{
	return buf.rend();
}
template<typename T> inline
typename matrix<T>::const_iterator matrix<T>::begin(void) const
{
	return buf.begin();
}
template<typename T> inline
typename matrix<T>::const_iterator matrix<T>::end(void) const
{
	return buf.end();
}
template<typename T> inline
typename matrix<T>::const_reverse_iterator matrix<T>::rbegin(void) const
{
	return buf.rbegin();
}
template<typename T> inline
typename matrix<T>::const_reverse_iterator matrix<T>::rend(void) const
{
	return buf.rend();
}



// ------------------------------------------------------------------------

void end_prog(void)
{
	cout << "end" << endl;
	getchar();
}

void f( istream& ifs , ostream& ofs , int cnt )
{
	int s;
	ifs >> s;
	vector<int> max_l(s);

	for( int i = 0 ; i < s ; ++i )
	{
		for( int j = 0 ; j < s ; ++j )
		{
			char c;
			ifs >> c;
			if( c == '1' ) max_l[i] = j;
		}
	}

	int num_swap = 0;
	for(;;)
	{
		bool moved = false;
		for( int i = 0 ; i < s-1 ; ++i )
		{
			if( max_l[i] <= i ) continue;

			int jj;
			for( int j = i+1 ; j < s ; ++j )
			{
				if( max_l[j] <= i )
				{
					jj = j;
					break;
				}
			}

			moved = true;

			for( int j = jj ; j > i ; j-- )
			{
				swap( max_l[j] , max_l[j-1] );
				num_swap++;
			}
			break;
		}
		if( !moved )break;
	}

	ofs << "Case #" << cnt << ": " << num_swap << std::endl; 

	int ww = 2+2;
}

void core()
{
	ifstream ifs("in.txt");
	ofstream ofs("out.txt");

	int T;
	ifs >> T;

	for( int i = 0 ; i < T ; ++i )
	{
		f( ifs , ofs , i+1 );
		//f( ifs , cout , i+1 );
	}

	int ii = 2+34;
}

int _tmain(int argc, _TCHAR* argv[])
{
	core();

	//end_prog();

	return 0;
}

