#include <stdint.h>
#include <cmath>
#include <ctime>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <numeric>

using namespace std;

class CLang
{
public:
	CLang()	{}

	void exec()
	{
		load();
		ofstream stream( "result.txt" );
		for( int i=0; i<m_testNum; ++i )
		{
			test(i, stream);
		}
	}

	int getValue( const vector<int>& buf )
	{
		int value = 0;
		for( vector<int>::const_iterator ite=buf.begin(); ite!= buf.end(); ++ite  )
		{
			if( *ite == 0 ) {
				continue;
			}
			value ^= *ite;
		}
		return	value;
	}

	void func( int index )
	{
		for( int i=index; i<m_size; ++i )
		{
			int v = m_buf1[i];
			m_buf1[i] = 0;
			m_buf2[i] = v;
			int v1 = getValue( m_buf1 );
			int v2 = getValue( m_buf2 );
			if( v1 == v2 )
			{
				int sum = 0;
				for( int i=0; i<m_size; ++i ) {
					sum += m_buf1[i];
				}
				//accumulate( m_buf1[0], m_buf2[m_size], 0 );
				if( m_result < sum ) {
					m_result = sum;
				}
			}
			func( i+1);
			m_buf1[i] = v;
			m_buf2[i] = 0;
		}
	}

	void test( int index, ofstream& stream )
	{
		m_result = 0;

		m_size = m_input[index].size();
		m_buf1 = m_input[index];
		m_buf2.clear();
		for( int i=0; i<m_size; ++i ) {
			m_buf2.push_back(0);
		}
		func(0);

		// output
		cout << "Case #" << (index+1) << ": ";
		stream << "Case #" << (index+1) << ": ";
		if( m_result == 0 )
		{
			cout << "NO";
			stream << "NO";
		}
		else
		{
			cout << m_result;
			stream << m_result;
		}
		cout << endl;
		stream << endl;
	}
	void load()
	{		
		ifstream s( "C-small-attempt0.in" );
		//ifstream s( "C-test.in" );
		string str;
		getline( s, str );
		m_testNum = atoi( str.c_str() );
		for( int i=0; i<m_testNum; ++i )
		{
			vector<int> list;
			getline( s, str );	// num
			getline( s, str );
			while(1)
			{
				int pos = str.find( " " );
				if( pos == string::npos )
				{
					list.push_back( atoi( str.c_str() ) );
					break;
				}
				string c = "";
				for( int i=0; i<pos; ++i ) {
					c.push_back( str[i] );
				}
				list.push_back( atoi( c.c_str() ) );
				str.erase( 0, pos +1 );
			}
			m_input.push_back( list );
		}
	}

private:
	int m_testNum;
	vector< vector<int> > m_input;
	int m_result;
	int m_size;

	vector<int> m_buf1;
	vector<int> m_buf2;
};

int main(int argc, char *argv[])
{
	CLang lang;
	lang.exec();
	
	getchar();
}
