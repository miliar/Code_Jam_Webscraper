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
	const char INPUT_FILENAME[32]	= "A-small-attempt1.in";
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
		string m_str;
	};

	char g_transform[30] = "yhesocvxduiglbkrztnwjpfmaq";
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
			input.m_str = str;
			m_input.push_back( input );
		}
	}

	//------------------------------
	void execImpl(int index, ostream& stream)
	{
		const string& input = m_input[index].m_str;
		string output = input;
		for( int i=0; i<input.size(); ++i )
		{
			if( input[i] == ' ' ) {
				continue;
			}
			char c = g_transform[ input[i] - 'a' ];
			output[i] = c;
		}
		stream << "Case #" << (index+1) << ": " << output;
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
