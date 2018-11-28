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
		int A;
		int B;
		vector<string> sl;
		vector<float> prob;
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

			getline( s, str );
			split( input.sl, str, " " );
			for( int i=0; i<input.sl.size(); ++i ) {
				input.prob.push_back( boost::lexical_cast<float>( input.sl[i] ) );
			}
			m_input.push_back( input );
		}
	}

	//------------------------------
	void execImpl(int index, ostream& stream)
	{
		const SInput& input = m_input[index];

		// i:backspaceâüÇµÇΩâÒêî
		float result = -1.0f;
		int allbit = (1<<input.A) -1;
		for( int i=0; i<=input.A; ++i )
		{
			float sum = 0;			
			for( int k=0; k<=allbit; ++k )
			{
				int num = i * 2;
				float prob = 1.0f;
				for( int m=0; m<input.A; ++m )	// bitî‘çÜ
				//for( int m=input.A-1; m>=0; --m )
				{
					if( k & (1<<(input.A-m-1)) ) {
						prob *= 1.0f - input.prob[m];
					}
					else {
						prob *= input.prob[m];
					}
				}
				int mask = allbit - ((1<<i) -1);
				// Ç‹Çæä‘à·Ç¢óLÇË
				if( k & mask ) {
//cout << "ng:";
					num += (input.B - input.A) +1 + input.B +1;
				}
				// ä‘à·Ç¢Ç»Çµ
				else {
					num += (input.B - input.A) +1;
//cout << "ok:";
				}
				sum += num * prob;
//cout << "num=" << num << ", prob=" << prob << " = " << (num * prob) << " sum=" << sum << endl;
			}
			if( result < 0.0f || result > sum ) {
				result = sum;
			}
//cout << "sum=" << sum << endl << endl;
		}

		// enter
		{
			int num = 1+ input.B +1;
			if( result > num ) {
				result = num;
			}
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
