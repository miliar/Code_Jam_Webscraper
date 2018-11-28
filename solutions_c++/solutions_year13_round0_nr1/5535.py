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

using namespace std;

//#define TEST

namespace {


#if defined(TEST)
	const char INPUT_FILENAME[32]	= "A-test.in";
	const char OUTPUT_FILENAME[32]	= "A-result.txt";
#else
#	if 1
	const char INPUT_FILENAME[32]	= "A-small-attempt0.in";
	const char OUTPUT_FILENAME[32]	= "A-small_result.txt";
#	else
	const char INPUT_FILENAME[32]	= "A-large-practice.in";
	const char OUTPUT_FILENAME[32]	= "A-large_result.txt";
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
		string m_str[4];
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
			SInput input;
			for( int i=0; i<4; ++i)
			{
				//getline( s, str );
				getline( s, input.m_str[i] );
			}
			getline( s, str );

			m_input.push_back( input );
		}
	}

	enum RESULT
	{
		NONE,
		WIN_X,
		WIN_O,
	};
	int getResult(const string& str)
	{
		enum STATE
		{
			NONE,
			X,
			O,
		};
		// ‰¡
		STATE state = STATE::NONE;
		for( int i=0; i<4; ++i)
		{
			char c = str[i];
			if( c == '.' ) {
				m_notComp = true;
				state = STATE::NONE;
				break;
			}
			else if( c == 'T') {
				continue;
			}
			else if(c=='X') {
				if(state == STATE::O) {
					state = STATE::NONE;
					break;
				}
				state = STATE::X;
			}
			else {
				if( state == STATE::X) {
					state = STATE::NONE;
					break;
				}
				state = STATE::O;
			}			
			
		}
		if( state == STATE::O) {
				return	RESULT::WIN_O;
			}
		else if( state == STATE::X) {
			return	RESULT::WIN_X;
		}
		return	RESULT::NONE;
	}

	//------------------------------
	void execImpl(int index, ostream& stream)
	{
		const SInput& input = m_input[index];
		m_notComp = false;
		// ‰¡
		int result = RESULT::NONE;
		for( int i=0; i<4; ++i)
		{
			result = getResult(input.m_str[i]);
			if( result != RESULT::NONE)
				break;
		}
		// c
		if( result == RESULT::NONE)
		{
			for( int i=0; i<4; ++i)
			{
				string str = "";
				for( int j=0; j<4; ++j )
				{
					str += input.m_str[j][i];
				}
				result = getResult(str);
				if( result != RESULT::NONE)
					break;
			}
		}
		// ŽÎ‚ß
		if( result == RESULT::NONE)
		{
			string str = "";
			str = "";
			str += input.m_str[0][0];
			str += input.m_str[1][1];
			str += input.m_str[2][2];
			str += input.m_str[3][3];
			result = getResult(str);
			if( result == RESULT::NONE)
			{
				str = "";
				str += input.m_str[3][0];
				str += input.m_str[2][1];
				str += input.m_str[1][2];
				str += input.m_str[0][3];
				result = getResult(str);
			}			
		}
		
		stream << "Case #" << (index+1) << ": ";
		if( result == RESULT::WIN_X )
			stream << "X won";
		else if(result == RESULT::WIN_O)
			stream << "O won";
		else if(m_notComp)
			stream << "Game has not completed";
		else
			stream << "Draw";
		
		stream << endl;
	}

	//------------------------------
	int m_testNum;
	bool m_notComp;
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
