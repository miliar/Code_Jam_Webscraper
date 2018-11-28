#include <stdint.h>
#include <cmath>
#include <ctime>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <algorithm>
#include <map>
#include <set>
#include <boost/lexical_cast.hpp>

using namespace std;

//#define TEST

namespace {


#if defined(TEST)
	const char INPUT_FILENAME[32]	= "C-test.in";
	const char OUTPUT_FILENAME[32]	= "C-result.txt";
#else
#	if 1
	const char INPUT_FILENAME[32]	= "C-small-attempt1.in";
	const char OUTPUT_FILENAME[32]	= "C-small_result.txt";
#	else
	const char INPUT_FILENAME[32]	= "C-large-practice.in";
	const char OUTPUT_FILENAME[32]	= "C-large_result.txt";
#	endif
#endif
	
	//------------------------------
	// split
	void split( vector<string>& list, string& str, const string& delim )
	{
		int cutAt;
		while( (cutAt = str.find_first_of(delim)) != str.npos )
		{
			if(cutAt > 0)
			{
				list.push_back(str.substr(0, cutAt));
			}
			str = str.substr(cutAt + 1);
		}
		if(str.length() > 0)
		{
			list.push_back(str);
		}
	}

	//------------------------------
	struct SInput
	{
		int N;
		int M;
		struct SPair
		{
			int64_t num;
			int type;
		};
		vector<SPair> ap;
		vector<SPair> bp;

	};
}	// anonymous namespace


class CWork
{
public:	
	//------------------------------
	void exec()
	{
		m_testNum = 0;
		load();
		ofstream stream( OUTPUT_FILENAME );
		for( int i=0; i<m_testNum; ++i )
		{
#if defined(TEST)
			execImpl(i, cout);
#else
			execImpl(i, stream);
#endif
		}
	}
	
private:
	//------------------------------
	void load()
	{
		ifstream s( INPUT_FILENAME );
		string str;
		getline( s, str );
		sscanf_s( str.c_str(), "%d", &m_testNum );

		for( int loop=0; loop<m_testNum; ++loop )
		{
			getline( s, str );
			SInput input;
			vector<string> sl;
			sscanf_s( str.c_str(), "%d %d", &input.N, &input.M );

			getline( s, str );
			split( sl, str, " " );
			for( int i=0; i<input.N; ++i ) 
			{
				SInput::SPair pair;
				pair.num = boost::lexical_cast<int64_t>( sl[i*2] );
				pair.type = boost::lexical_cast<int64_t>( sl[i*2+1] );
				input.ap.push_back( pair );
			}

			getline( s, str );
			sl.clear();
			split( sl, str, " " );
			for( int i=0; i<input.M; ++i ) 
			{
				SInput::SPair pair;
				pair.num = boost::lexical_cast<int64_t>( sl[i*2] );
				pair.type = boost::lexical_cast<int64_t>( sl[i*2+1] );
				input.bp.push_back( pair );
			}
			m_input.push_back( input );
		}
	}

	void solve( int64_t result, vector<SInput::SPair>& ap, vector<SInput::SPair>& bp, int a, int b )
	{
		if( a >= m_case.ap.size() || b >= m_case.bp.size() ) {
			if( m_result < result ) {
				m_result = result;
			}
			return;
		}

		if( ap[a].type == bp[b].type )
		{
			int64_t sub_a = m_case.ap[a].num - ap[a].num;
			int64_t sub_b = m_case.bp[b].num - bp[b].num;
			int64_t sub = min( sub_a, sub_b );
			result += sub;
			ap[a].num += sub;
			if( ap[a].num >= m_case.ap[a].num ) {
				a++;
			}
			bp[b].num += sub;
			if( bp[b].num >= m_case.bp[b].num ) {
				b++;
			}
			solve( result, ap, bp, a, b );
		}
		else
		{			
			// a‚ðŽÌ‚Ä‚é
			{
				int64_t num_a = ap[a].num;
				int64_t num_b = bp[b].num;

				solve( result, ap, bp, a+1, b );
				// Œ³‚É–ß‚·
				ap[a].num = num_a;
				bp[b].num = num_b;
				for( int i=a+1; i<ap.size(); ++i ) {
					ap[i].num = 0;
				}
				for( int i=b+1; i<bp.size(); ++i ) {
					bp[i].num = 0;
				}
			}

			// b‚ðŽÌ‚Ä‚é
			{
				int64_t num_a = ap[a].num;
				int64_t num_b = bp[b].num;
				solve( result, ap, bp, a, b+1 );
				// Œ³‚É–ß‚·
				ap[a].num = num_a;
				bp[b].num = num_b;
				for( int i=a+1; i<ap.size(); ++i ) {
					ap[i].num = 0;
				}
				for( int i=b+1; i<bp.size(); ++i ) {
					bp[i].num = 0;
				}
			}
		}
	}

	//------------------------------
	void execImpl(int index, ostream& stream)
	{
		const SInput& input = m_input[index];
		m_case = input;
		m_result = 0;
		vector<SInput::SPair> ap = input.ap;
		vector<SInput::SPair> bp = input.bp;
		for( int i=0; i<ap.size(); ++i ) {
			ap[i].num = 0;
		}
		for( int i=0; i<bp.size(); ++i ) {
			bp[i].num = 0;
		}

		solve( 0, ap, bp, 0, 0 );

		stream << "Case #" << (index+1) << ": " << m_result;
		stream << endl;
	}

	//------------------------------
	int m_testNum;
	int64_t m_result;
	SInput m_case;
	vector<SInput> m_input;
};

int main(int argc, char *argv[])
{
	clock_t start,end;
	start = clock();

	CWork work;
	work.exec();
	
	end = clock();
	printf( "time=%fsec\n", (double)(end-start)/CLOCKS_PER_SEC);
	getchar();
}
