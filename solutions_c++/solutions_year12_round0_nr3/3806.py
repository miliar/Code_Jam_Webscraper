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
#	if 0
	const char INPUT_FILENAME[32]	= "C-small-attempt0.in";
	const char OUTPUT_FILENAME[32]	= "C-small_result.txt";
#	else
	const char INPUT_FILENAME[32]	= "C-large.in";
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
		int A;
		int B;
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
			sscanf_s( str.c_str(), "%d %d", &input.A, &input.B );
			m_input.push_back( input );
		}
	}

	//------------------------------
	void execImpl(int index, ostream& stream)
	{
		const SInput& input = m_input[index];
		int a = input.A;
		int b = input.B;
		string sa = boost::lexical_cast<string>( a );
		int l = sa.length();
		int result = 0;
		if( sa.size() == 1 ) {
			result = 0;
		}
		else
		{
			set<string> ss;
			for( int digit=1; digit<l; ++digit )
			{
				for( int no=a; no<=b; ++no )
				{
					string sn = boost::lexical_cast<string>( no );
					string str = sn.substr(digit, l-digit) + sn.substr(0,digit);
					if( str[0] == '0' ) {
						continue;
					}
					int no2 = boost::lexical_cast<int>( str );
					if( no2 > b
						|| no2 < no
						) {
						continue;
					}
					if( sn == str ) {
						continue;
					}
					ss.insert( sn + " " + str );
				}
			}
			result = ss.size();
		}

		stream << "Case #" << (index+1) << ": " << result;
		stream << endl;
	}

	//------------------------------
	int m_testNum;
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
