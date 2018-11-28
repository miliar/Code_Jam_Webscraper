// codejam1.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include "stdafx.h"

#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#include <math.h>

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

const double PI = 3.141592f;

//////////////////////////////////////////////////////////////////////////
class fly_swatter : public solver
{
public:
	fly_swatter( LPCSTR input_file = 0, LPCSTR output_file = 0 )
		: solver(input_file,output_file)
	{
	}

	struct case_info
	{
		double R;
		double t;
		double r;
		double G;
		
		double white_area_grid_size;
		double inner_circle_r;
		double inner_circle_r_square;

		// 중간값.
		double f;
		double g;
	};

	bool solve_one_case( int case_no )
	{
		char buf[512] = { 0, };

		if ( !read_line( buf, sizeof(buf) ) )
			error( FormatString( "one line of case value read failed.\n" ) );

		case_info info;

		const char* tok = 0;
		tok = ::strtok( buf, " " );
		info.f = ::atof( tok );	// 파리 반지름
		tok = ::strtok( NULL, " " );
		info.R = ::atof( tok );	// 라켓 반지름
		tok = ::strtok( NULL, " " );
		info.t = ::atof( tok );	// 라켓 외부 링 넒이
		tok = ::strtok( NULL, " " );
		info.r = ::atof( tok );	// 라켓줄 반지름
		tok = ::strtok( NULL, " " );
		info.g = ::atof( tok );	// 라켓줄간의 거리

		double P = 1.0f;

		info.G = info.g - (info.f*2);		// 실제 파리의 크리를 적용한 라켓 줄간의 거리
											// 이렇게 두고 라켓의 공간만 구하면 됨.
		info.r += info.f;

		if ( info.G <= 0.0f )
			info.G = 0.0f;

		if ( info.G > 0.0f )
		{
			info.inner_circle_r = info.R - info.t;
			info.inner_circle_r_square = info.inner_circle_r*info.inner_circle_r;
			info.white_area_grid_size 
				= 2*info.r+info.g;

			// 전체 면적을 구함.
			double total_area = (PI * (info.R*info.R))/8;

			// 파리가 무사할수 있는 면적을 구함.
			// 8분의 1의 면적만 구하면 됨.
			// 1/4쪽의 빈공간은 ((R / ( 2r+g ))+1)개 by ((R / ( 2r+g ))+1)개의 하얀사각형수만큼 있고
			// 이것을 원의 1/4쪽 모양으로 커팅한 안쪽의 부분만 구하면됨
			
			// 이때 하얀 사각형의 그리드 갯수를 K라 놓자
			int K = ((info.inner_circle_r/(info.white_area_grid_size))+1);
			
			double total_white_area = 0.0f;
			for ( int i = 0; i < K; ++i )
			{
				for ( int j = 0; j <= i; ++j ) 
					// i 수만큼만 올라가면 됨. j==i인 곳은 넒이를 절반으로 계산해야함
				{
					double white_area = get_white_area( i, j, info );
					total_white_area += i==j?(white_area/2):white_area;
				}
			}

			// 파리가 무사할수 있는 면적에서 전체 면적으로 나눔.
			P = 1 - (total_white_area / total_area);
		}

		write( FormatString( "Case #%d: %0.06f\n", case_no, P ) );
		return true;
	}

	struct point
	{
		double x;
		double y;
	};

	bool is_inside_in_circle( const point& p, double circle_square )
	{
		if ( p.x*p.x+p.y+p.y < circle_square )
			return true;
		return false;
	}

	double calc_contact_point_with_circle( double x_or_y, double circle_square )
	{
		return circle_square - x_or_y*x_or_y;
	}

	double get_white_area( int i, int j, const case_info& info )
	{
		point area_left_bottom;		// 좌하단.
		area_left_bottom.x = (info.white_area_grid_size)*i + info.r;
		area_left_bottom.y = (info.white_area_grid_size)*j + info.r;

		{
			const point& pt = area_left_bottom;
			// 좌측하단의 점이 안쪽원 바깥에 있음 전체가 바깥이므로 계산할 필요없음.
			if ( !is_inside_in_circle( pt, info.inner_circle_r_square ) )
				return 0;
		}

		point area_right_top;		// 우상단. 얘가 원의 안에 있는지 체크 있으면 거의 바로 끝남.
		area_right_top.x = (info.white_area_grid_size)*i + info.r + info.G;
		area_right_top.y = (info.white_area_grid_size)*j + info.r + info.G;

		{
			const point& pt = area_right_top;
			// 우측상단 점이 안쪽 원의 안쪽에 있음 하얀 
			// 사각형이 모두 안쪽에 있다. 하얀사각형 면적을 그대로 리턴.
			if ( is_inside_in_circle( pt, info.inner_circle_r_square ) )
				return info.G*info.G;
		}


		// 전체원에서 동북방향 파이 모양의 원이므로,
		// 우하단이 밖에 있음 좌상단도 항상 바깥에 있음. 
		// 3가지 경우가 나옴.
		//
		// 1) 우측상단만 바깥에 있음
		// 2) 우측상단과 좌측상단과 우측하단이 동시에 바깥에 있음.
		// 3) 우측상단과 우측하단만 바깥에 있음.


		point area_left_top;		
		area_left_top.x = (info.white_area_grid_size)*i + info.r;
		area_left_top.y = (info.white_area_grid_size)*j + info.r + info.G;
		{
			const point& pt = area_left_top;
			// 좌측상단만 체크하면 2번 케이스를 바로 찾을수 있으므로 좌측상단부터 체크
			if ( !is_inside_in_circle( pt, info.inner_circle_r_square ) )
			{ // 2) 번케이스. 모두 바깥에 나가있음.

				// 원과 white_area의 두 접점을 구함.
				point pt1, pt2;
				pt1.x = area_left_bottom.x;
				pt1.y = calc_contact_point_with_circle( pt1.x, info.inner_circle_r_square );
				pt2.y = area_left_bottom.y;
				pt2.x = calc_contact_point_with_circle( pt2.y, info.inner_circle_r_square );

				// 계산해봐
				double pie_area = calc_pie_area( pt1, pt2, info );


				// 모두 바깥에 나가있는 경우는 사각형 계산이 없음.

				return pie_area;
			}
		}

		point area_right_bottom;
		area_right_bottom.x = (info.white_area_grid_size)*i + info.r + info.G;
		area_right_bottom.y = (info.white_area_grid_size)*j + info.r;
		{
			const point& pt = area_right_bottom;
			if ( is_inside_in_circle( pt, info.inner_circle_r_square ) )
			{ // 1) 번케이스 우측상단만 바깥에 나가있음.

				// 원과 white_area의 두 접점을 구함.
				point pt1, pt2;
				pt1.y = area_right_top.x;
				pt1.x = calc_contact_point_with_circle( pt1.y, info.inner_circle_r_square );
				pt2.x = area_right_top.x;
				pt2.y = calc_contact_point_with_circle( pt2.x, info.inner_circle_r_square );

				double pie_area = calc_pie_area( pt1, pt2, info );

				// 
				double lrect_area = 
					(info.G)*(pt1.x-area_left_top.x);

				double rrect_area =
					(pt2.y-area_right_bottom.y)*(pt2.x-pt1.x);

				return pie_area+lrect_area+rrect_area;
			}
		}

		{
			// 3)번 케이스
			// 원과 white_area의 두 접점을 구함.
			point pt1, pt2;
			pt1.y = area_right_top.y;
			pt1.x = calc_contact_point_with_circle( pt1.y, info.inner_circle_r_square );
			pt2.y = area_right_bottom.y;
			pt2.y = calc_contact_point_with_circle( pt2.y, info.inner_circle_r_square );

			double pie_area = calc_pie_area( pt1, pt2, info );

			double lrect_area = 
				(info.G)*(pt1.x-area_left_top.x);

			//double rrect_area =
			//	(pt2.y-area_right_bottom.y)*(pt2.x-pt1.x);

			return pie_area+lrect_area;
		}
	}

	double calc_pie_area( const point& pt1, const point& pt2, const case_info& info )
	{
		// 파이 부분의 넒이.
		/*
		double abs_pt1_plus_pt2 = 
			::sqrt( pt1.x*pt1.x + pt1.y*pt1.y ) + ::sqrt( pt2.x*pt2.x + pt2.y*pt2.y );
		double inner_product_pt1_pt2 =
			((pt1.x * pt2.x) + (pt1.y * pt2.y ));
		double acos_pt1_pt2 = ::acos( inner_product_pt1_pt2 / abs_pt1_plus_pt2 );
		*/
		double half_PI = ::atan( 1.0f );

		double radian_pt1_pt2 = ::atan( pt1.y/pt1.x ) - ::atan( pt2.y/pt1.x );
		double pie_area = info.inner_circle_r_square * radian_pt1_pt2;
		
		// 이부분에서 삼각형2개를 빼면된다.
		double t = (pt1.x - pt1.x*pt2.y/pt1.x);
		pie_area -=
			(pt1.y-pt2.y)*t/2; // 위쪽 삼각형
		pie_area -=
			(pt2.x - (pt1.x-t))*pt2.y/2;
		return pie_area;
	}
};

//////////////////////////////////////////////////////////////////////////
//class hexagon_game
//{
//	hexagon_game( LPCSTR input_file = 0, LPCSTR output_file = 0 )
//		: solver(input_file,output_file)
//	{
//	}
//
//	const char* tokenize( char* buf, const char* delim )
//	{
//		const char* t = ::strtok( buf, delim );
//		//if ( !t )
//		//	error( FormatString( "failed to read token.\n" ) );
//		return t;
//	}
//
//	bool solve_one_case( int case_no )
//	{
//		char pos_buf[512] = { 0, };
//		if ( !read_line( pos_buf, sizeof(pos_buf) ) )
//			error( FormatString( "one line of position read failed.\n" ) );
//		char value_buf[512] = { 0, };
//		if ( !read_line( value_buf, sizeof(value_buf) ) )
//			error( FormatString( "one line of value read failed.\n" ) );
//
//		typedef int value_t;
//		typedef int position_t;
//		typedef std::multimap< value_t, position_t > game_board_t;
//		game_board_t initial_board;
//
//		position_t	c_p;
//		value_t		c_v;
//		const char* t = 0;
//
//		std::vector< position_t > pos_list;
//		std::vector< value_t > value_list;
//
//		// read position list
//		t = tokenize( pos_buf, " " );
//		pos_list.push_back( ::atoi( t ) );
//		while ( t = tokenize( NULL, " " ) )
//			pos_list.push_back( ::atoi( t ) );
//
//		// read value list
//		t = tokenize( value_buf, " " );
//		value_list.push_back( ::atoi( t ) );
//		while ( t = tokenize( NULL, " " ) )
//			value_list.push_back( ::atoi( t ) );
//
//		if ( pos_list.size() != value_list.size() )
//			error( FormatString( "one line of value read failed.\n" ) );
//		if ( pos_list.empty() || value_list.empty() )
//			error( FormatString( "one line of value read failed.\n" ) );
//
//		// make game_board
//		for ( size_t i = 0; i < pos_list.size(); ++i )
//		{
//			initial_board.insert( 
//				std::make_pair( value_list[i], pos_list[i] ) );
//		}
//
//
//		// now process
//		
//};


int _tmain(int argc, _TCHAR* argv[])
{
//	saveing_the_universe solver( "A-large.in", "A-large.out" );
//	train_timetable solver( "B-large.in", "B-large.out" );
	fly_swatter solver( "C-in", 0 );
//	hexagon_game solver( "C-in", 0 );
	solver.solve();
	return 0;
}

// 만 13세 이상
// 구글과 구글관련 회사의 직원이 아니어야함
// 구글과 구글관련 회사의 직원과 가족관계나 같이 살거나 하면 안됨
// 미안마, 쿠바, 이란, 북한, 퀘벡 수단, 시리아 사람은 안됨
// 상위 500등은 해당 국가의 구글 사무실에서 3라운드를 진행
// 그리고 마지막 상위 100명은 구글 캘리포니아 마운틴뷰 본사로 초청됨. (구글이 돈 대준다함)
