// codejam1.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include "stdafx.h"

#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>

#include <string>
#include <vector>
#include <map>

typedef const char* LPCSTR;

//////////////////////////////////////////////////////////////////////////

template < int STRING_BUFFER_SIZE = 8192 >
class TFormatAnsiString													  {
public:
	typedef std::string string;

	inline TFormatAnsiString( LPCSTR format, ... )
	{
		char	buffer_[STRING_BUFFER_SIZE] = { 0, };
		size_t buffer_size = sizeof(buffer_) / sizeof(buffer_[0]);
		va_list args;
		va_start( args, format );
		vsnprintf_s( buffer_, buffer_size, _TRUNCATE, format, args );
		va_end( args );
		format_ = buffer_;
	}
	inline TFormatAnsiString( LPCSTR format, va_list args )
	{
		char	buffer_[STRING_BUFFER_SIZE] = { 0, };
		size_t buffer_size = sizeof(buffer_) / sizeof(buffer_[0]);
		vsnprintf_s( buffer_, buffer_size, _TRUNCATE, format, args );
		format_ = buffer_;
	}

	inline operator string () const
	{
		return format_;
	}

	inline LPCSTR Get() const
	{
		return format_.c_str();
	}

protected:
	string	format_;
};

typedef TFormatAnsiString<8192>	FormatAnsiString;

//#ifdef _UNICODE
//typedef FormatWideString		FormatString;
//#else
typedef FormatAnsiString		FormatString;
//#endif


//////////////////////////////////////////////////////////////////////////

class solver
{
public:
	solver( LPCSTR input_file = 0, LPCSTR output_file = 0 )
	{
		if ( input_file )
			in_ = ::fopen( input_file, "r" );
		else 
			in_ = stdin;
		if ( output_file )
			out_ = ::fopen( output_file, "w" );
		else
			out_ = stdout;

		if ( !in_ )
		{
			::fprintf( stderr, "input file open failed: [%s]\n", input_file );
			::exit(1);
		}
		if ( !out_ )
		{
			::fprintf( stderr, "output file open failed: [%s]\n", output_file );
			::exit(1);
		}
	}
	~solver()
	{
		::fclose( in_ );
		::fclose( out_ );
	}

public:
	bool read_line( char* dst, int size )
	{
		::fgets( dst, size, in_ );
		if ( ::feof( in_ ) )
			return false;
		return true;
	}
	void write( const std::string& msg )
	{ return write( msg.c_str() ); }
	void write( const char* src )
	{
		::fprintf( out_, src );
	}
	void error( const std::string& msg )
	{ return error( msg.c_str() ); }
	void error( const char* msg )
	{
		::fprintf( stderr, msg );
		::exit(1);
	}

protected:
	FILE*	in_;
	FILE*	out_;
};

//////////////////////////////////////////////////////////////////////////
class saveing_the_universe : public solver
{
public:
	saveing_the_universe( LPCSTR input_file = 0, LPCSTR output_file = 0 )
		: solver(input_file,output_file)
	{
	}

	bool solve_one_case( int case_no )
	{
		char buf[512] = { 0, };

		if ( !read_line( buf, sizeof(buf) ) )
			error( FormatString( "S value read failed.\n" ) );
		int S = ::atoi( buf ); // search engine count

		typedef std::map< std::string, int > se_list_t;
		se_list_t search_engine_master_list;
		for ( size_t i = 0; i < S; ++i )
		{
			if ( !read_line( buf, sizeof(buf) ) )
				error( FormatString( "search engine name read failed.\n" ) );
			search_engine_master_list.insert( std::make_pair(buf,0) );
		}
		
		if ( !read_line( buf, sizeof(buf) ) )
			error( FormatString( "Q value read failed.\n" ) );
		int Q = ::atoi( buf ); // query count

		int switching_count = 0;

		se_list_t s = search_engine_master_list;
		for ( size_t j = 0; j < Q; ++j )
		{

			if ( !read_line( buf, sizeof(buf) ) )
				error( FormatString( "query read failed.\n" ) );
		
			se_list_t::iterator i = s.find( buf );
			if ( i != s.end() )
			{
				s.erase( i );
				if ( s.empty() )
				{
					// 새 검색에서도 금방 나온놈을 빼야함.
					++switching_count;
					s = search_engine_master_list;

					i = s.find( buf );
					if ( i == s.end() )
						error( FormatString( "query read failed.\n" ) );
					s.erase( i );
				}
			}
		}

		write( FormatString( "Case #%d: %d\n", case_no, switching_count ) );
		return true;
	}

	bool solve()
	{
		char buf[512] = { 0, };

		if ( !read_line( buf, sizeof(buf) ) )
		{
			error( FormatString( "N value read failed.\n" ) );
			return false;
		}
		int N = ::atoi( buf );

		if ( N <= 0 )
			error( FormatString( "case count should be greater than ZERO\n" ) );

		for ( size_t i = 0; i < N; ++i )
			solve_one_case(i+1);
		return true;
	}
};

int _tmain(int argc, _TCHAR* argv[])
{
//	saveing_the_universe solver( "in", 0 );
	saveing_the_universe solver( "A-large.in", "A-large.out" );
	solver.solve();
	return 0;
}

