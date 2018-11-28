#include <stdint.h>
#include <cmath>
#include <ctime>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class CLang
{
private:	
	struct SInput
	{
		bool m_o;
		int m_step;
	};
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

private:
	vector<CLang::SInput>::const_iterator getNextIte( vector<CLang::SInput>::const_iterator ite, const vector<CLang::SInput>& inputList, bool o )
	{
		while(1) 
		{
			++ite;
			if( ite == inputList.end() ){
				return	ite;
			}
			if( ite->m_o == o ) {
				return	ite;
			}
		}
	}

	void test( int index, ofstream& stream )
	{
		const vector<SInput>& inputList = m_input[index];
		
		// 最初の命令を検索
		vector<SInput>::const_iterator iteO = inputList.begin();
		vector<SInput>::const_iterator iteB = inputList.begin();
		if( !iteO->m_o ) {
			iteO = getNextIte( iteO, inputList, true );
		}
		if( iteB->m_o ) {
			iteB = getNextIte( iteB, inputList, false );
		}
				
		int count = 0;
		int posO = 1;
		int posB = 1;
		bool pushO = false;	// ボタン押したフラグ
		bool pushB = false;
		//bool firstO = (iteO == inputList.end() );	// Oが最初の命令実行済み
		while(1)
		{
			if( iteO == inputList.end() 
				&& iteB == inputList.end() 
				)
			{
				break;
			}
			// Orange
			if( iteO != inputList.end() )
			{
				if( iteO->m_step == posO )
				{
					if( iteB == inputList.end()
						|| iteO < iteB
						)
					{
						pushO = true;
					}
				}
				else {
					if( posO < iteO->m_step ) {
						posO++;
					}
					else {
						posO--;
					}
				}
			}
			// Blue
			if( iteB != inputList.end() )
			{
				if( iteB->m_step == posB )
				{
					if( iteO == inputList.end()
						|| iteB < iteO
						)
					{
						pushB = true;
					}
				}
				else {
					if( posB < iteB->m_step ) {
						posB++;
					}
					else {
						posB--;
					}
				}
			}
			if( pushO )
			{
				iteO = getNextIte( iteO, inputList, true );
				pushO = false;
			}
			else if( pushB )				
			{
				iteB = getNextIte( iteB, inputList, false );
				pushB =false;
			}

			count++;
		}


		//cout << "Case #" << (index+1) << ": " << count << endl;
		stream << "Case #" << (index+1) << ": " << count << endl;
	}
	void load()
	{
		//ifstream s( "A-test.in" );
		ifstream s( "A-large.in" );
		string str;
		getline( s, str );
		sscanf_s( str.c_str(), "%d", &m_testNum );

		for( int i=0; i<m_testNum; ++i )
		{
			vector<SInput> inputList;
			char str2[1024] = "";
			getline( s, str );
			int pos = str.find( " " );
			string strNum = "";
			for( int i=0; i<pos; ++i ) {
				strNum.push_back( str[i] );
			}
			int num = atoi( strNum.c_str() );
			str.erase( 0, pos+1 );
			for( int j=0; j<num; ++j )
			{
				SInput input;
				char c = str[0];
				str.erase( 0, 2 );
				input.m_o = ( c == 'O' );
				pos = str.find( " " );
				strNum = "";
				if( pos == string::npos )
				{
					strNum = str;
				}
				for( int i=0; i<pos; ++i ) {
					strNum.push_back( str[i] );
				}
				input.m_step = atoi( strNum.c_str() );
				str.erase( 0, pos+1 );
				inputList.push_back( input );
			}
			m_input.push_back( inputList );
		}
	}

private:
	int m_testNum;
	vector< vector<SInput> > m_input;
};

int main(int argc, char *argv[])
{
	CLang lang;
	lang.exec();
	
	//getchar();
}
