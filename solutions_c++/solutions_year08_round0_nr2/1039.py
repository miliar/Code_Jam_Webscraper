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
	virtual bool solve_one_case( int case_no ) = 0;
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
};

#ifndef FOR_EACH_CONT
#define FOR_EACH_CONT( cont_type, cont_instance, iterator_name )									\
	for ( cont_type::iterator iterator_name = cont_instance.begin(), itrEnd = cont_instance.end();	\
	iterator_name != itrEnd; ++iterator_name )
#endif//FOR_EACH_CONT
#ifndef FOR_EACH_CONST_CONT
#define FOR_EACH_CONST_CONT( cont_type, cont_instance, iterator_name )										\
	for ( cont_type::const_iterator iterator_name = cont_instance.begin(), itrEnd = cont_instance.end();	\
	iterator_name != itrEnd; ++iterator_name )
#endif//FOR_EACH_CONST_CONT

//////////////////////////////////////////////////////////////////////////
class train_timetable : public solver
{
public:
	train_timetable( LPCSTR input_file = 0, LPCSTR output_file = 0 )
		: solver(input_file,output_file)
	{
	}

	int train_time_to_integer( const char* time )
	{
		char time_string[512] = { 0, };
		::strcpy( time_string, time );
		std::string tt;
		const char* t = 0;
		t = ::strtok( time_string, ":" );
		tt = t;
		t = ::strtok( NULL, ":" );
		tt += t;
		return ::atoi( tt.c_str() );
	}

	int train_time_add( int time_a, int time_b )
	{
		int time_a_hour = time_a / 100;
		int time_a_min = time_a % 100;
		int time_b_hour = time_b / 100;
		int time_b_min = time_b % 100;
		
		int t = (time_a_hour + time_b_hour)*100;
		t += (time_a_min+time_b_min)%60;
		t += ((time_a_min+time_b_min)/60)*100;
		return t;
	}
	
	bool solve_one_case( int case_no )
	{
		char buf[512] = { 0, };

		if ( !read_line( buf, sizeof(buf) ) )
			error( FormatString( "T value read failed.\n" ) );
		int T = ::atoi( buf ); // turn around time

		if ( !read_line( buf, sizeof(buf) ) )
			error( FormatString( "NA,NB value read failed.\n" ) );

		const char* t = 0;
		t = ::strtok( buf, " " ); // NA
		int NA = ::atoi( t );
		t = ::strtok( NULL, " " ); // NB
		int NB = ::atoi( t );

		// 도착시간, 출발시간 // 일부러 도착 시간으로 정렬한다.
		typedef std::multimap< int, int > time_table_t;
		time_table_t	AB,		// A->B 출발시간이 앞(출발시간으로 소팅)
						AB_r;	// A->B 도착시간이 앞(도착시간으로 소팅)
		time_table_t	BA,		// B->A 출발시간이 앞(출발시간으로 소팅)
						BA_r;	// B->A 도착시간이 앞(도착시간으로 소팅)

		// read timetable
		for ( size_t i = 0; i < NA; ++i )
		{
			if ( !read_line( buf, sizeof(buf) ) )
				error( FormatString( "time_table AB read failed.\n" ) );
			std::string departure_time = ::strtok( buf, " " ); // departure time
			std::string arrival_time = ::strtok( NULL, " " ); // arrival time

			int d_t = train_time_to_integer( departure_time.c_str() );
			int a_t = train_time_to_integer( arrival_time.c_str() );

			AB.insert( std::make_pair( d_t, train_time_add( a_t, T )  ) ); // add turnaround time
			AB_r.insert( std::make_pair( train_time_add( a_t, T ), d_t ) ); // add turnaround time
		}

		for ( size_t i = 0; i < NB; ++i )
		{
			if ( !read_line( buf, sizeof(buf) ) )
				error( FormatString( "time_table BA read failed.\n" ) );
			std::string departure_time = ::strtok( buf, " " ); // departure time
			std::string arrival_time = ::strtok( NULL, " " ); // arrival time

			int d_t = train_time_to_integer( departure_time.c_str() );
			int a_t = train_time_to_integer( arrival_time.c_str() );

			BA.insert( std::make_pair( d_t, train_time_add( a_t, T )  ) ); // add turnaround time
			BA_r.insert( std::make_pair( train_time_add( a_t, T ), d_t ) ); // add turnaround time
		}

		time_table_t AB_o = AB;
		time_table_t BA_o = BA;

		NA = NB = 0;

		// process
		bool found = false;
		FOR_EACH_CONT( time_table_t, AB_r, itr_A ) // 도착시간순으로
		{
			FOR_EACH_CONT( time_table_t, BA, itr_B ) // 출발시간 순으로
			{
				// A->B 로 가는 녀석중에서, BA로 올 수 있는 녀석을 찾는다.
				if ( itr_A->first/*B에 도착시간*/ <= itr_B->first/*B에서 출발시간*/ )
				{
					// 적용된 녀석은 삭제 함.
					time_table_t::iterator i = BA_o.find( itr_B->first ); // 출발시간으로 찾아서 제거
					if ( i != BA_o.end() )
					{
						BA_o.erase( i );
						break; // 이놈은 찾았다. 다음 A->B 열차 시간표를 검색
					}
				}
			}
		}

		FOR_EACH_CONT( time_table_t, BA_r, itr_B )
		{
			FOR_EACH_CONT( time_table_t, AB, itr_A )
			{
				if ( itr_B->first/*A에 도착시간*/ <= itr_A->first/*A에서 출발시간*/ )
				{
					// 적용된 녀석은 삭제 함.
					time_table_t::iterator i = AB_o.find( itr_A->first ); // 출발시간으로 찾아서 제거
					if ( i != AB_o.end() )
					{
						AB_o.erase( i );
						break; // 이놈은 찾았다. 다음 A->B 열차 시간표를 검색
					}
				}
			}
		}

		NA = AB_o.size();
		NB = BA_o.size();
	
		write( FormatString( "Case #%d: %d %d\n", case_no, NA, NB ) );
		return true;
	}
};

int _tmain(int argc, _TCHAR* argv[])
{
//	saveing_the_universe solver( "in", 0 );
//	saveing_the_universe solver( "A-large.in", "A-large.out" );
	train_timetable solver( "B-large.in", "B-large.out" );
	solver.solve();
	return 0;
}

