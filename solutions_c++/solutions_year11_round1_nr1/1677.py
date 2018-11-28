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

using namespace std;

namespace {
#if 0
	const char INPUT_FILENAME[32]	= "test_A.txt";
	const char OUTPUT_FILENAME[32]	= "result_testA.txt";
#else
	const char INPUT_FILENAME[32]	= "A-small-attempt3.in";
	const char OUTPUT_FILENAME[32]	= "result_smallA.txt";
#endif
}	// anonymous namespace


class CWork
{
	struct SInput
	{
		int n;
		int pd;
		int pg;
	};
public:	
	//------------------------------
	void exec()
	{
		m_testNum = 0;
		load();
		ofstream stream( OUTPUT_FILENAME );
		for( int i=0; i<m_testNum; ++i )
		{
			execImpl(i, stream);
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
			getline( s, str );
			sscanf_s( str.c_str(), "%d %d %d", &input.n, &input.pd, &input.pg );
			m_input.push_back( input );
		}
	}
	bool total( int d, int win, int pg)
	{
#if 0
		int totalD = d;
		while(1)
		{
			for( int totalW=win; totalW<totalD; ++totalW )
			{
				int rate = (int)((float)totalW/(float)totalD * 100.0f);
				if( rate == pg ) {
					return	true;
				}
				else if( rate > pg ) {
					break;
				}
			}
			totalD++;
		}
		return	false;

#else
		if( pg == 100 && d != win ) {
			return	false;
		}
		else if( pg == 0 && win > 0 ) {
			return	false;
		}
		/*enum
		{
			STATE_NONE,
			STATE_BIG,
			STATE_SMALL,
		};*/
		int totalD = d;
		/*int prevRate = (int)((float)win/(float)totalD * 100.0f);
		if( prevRate == pg ) {
			return	true;
		}*/

		while(1)
		{
			int totalW = pg * totalD / 100;
			if( (totalD - d) >= (totalW -win)
				&& totalW >= win
				)
			{
				int rate = (int)((float)totalW/(float)totalD * 100.0f);
				if( rate == pg ) {
					return	true;
				}
				// ñ⁄ïWÇ…ëŒÇµÇƒè¨Ç≥Ç¢
				/*if( rate < pg )
				{
					if( rate < prevRate ) {
						return	false;
					}
				}
				// big
				else
				{
					if( rate > prevRate ) {
						return	false;
					}
				}*/
				//prevRate = rate;
				/*for( int totalW=win; totalW<totalD; ++totalW )
				{
					int rate = (int)((float)totalW/(float)totalD * 100.0f);
					if( rate == pg ) {
						return	true;
					}
					else if( rate > pg ) {
						break;
					}
				}*/
			}
			totalD++;
		};
		return	false;
#endif
	}

	//------------------------------
	void execImpl(int index, ofstream& stream)
	{
		//cout << index << endl;
		const SInput& input = m_input[index];
		for( int d=1; d<=input.n; ++d )
		{
			int win = input.pd * d / 100;
			int rate = (int)((float)win/(float)d * 100.0f);
			if( rate == input.pd )
			{
				if( total( d, win, input.pg ) )
				{
					cout << "Case #" << (index+1) << ": Possible" << endl;						
					stream << "Case #" << (index+1) << ": Possible" << endl;						
					return;
				}
			}
		}
		cout << "Case #" << (index+1) << ": Broken" << endl;
		stream << "Case #" << (index+1) << ": Broken" << endl;
	}

	int m_testNum;
	vector<SInput> m_input;
};

int main(int argc, char *argv[])
{
	CWork work;
	work.exec();

	getchar();
}
