#include <iostream>
#include <fstream>
#include <list>
#include <string>
#include <map>

using namespace std;

int getSwitchCount( list<string>& listEngines, list<string>& listQueries )
{
	bool bSkip = false;
	int cnt, switch_len = 0, max_len = 0;
	list<string>::iterator itrE = listEngines.begin();
	list<string>::iterator itrQ;
	while( itrE != listEngines.end() )
	{
		switch_len = 0;
		itrQ = listQueries.begin();
		bool bFoundMatch = false;
		while( itrQ != listQueries.end() )
		{
			++ switch_len;
			if( *itrQ == *itrE )
			{
				bFoundMatch = true;	
				if( switch_len > max_len )
				{
					max_len = switch_len;
				}
				break;
			}
			++ itrQ;
		}
		if( !bFoundMatch )
		{
			bSkip = true;
			break;
		}
		
		++ itrE;
	}
	
	if( bSkip )
		cnt = listQueries.size();
	else
		cnt = max_len;
	
	while( cnt > 1 )
	{
		listQueries.pop_front();
		-- cnt;
	}
	
	if( listQueries.size() > 1 )
	{
		return getSwitchCount(listEngines, listQueries) + 1;
	}
	else
	{
		if( bSkip )
			return 0;
		else
			return listQueries.size();
	}
}

int main (int argc, const char * argv[]) {
	int nCnt = 0, nSubCnt = 0, nCaseCnt = 0;
	int nEngineCnt = 0, nQueryCnt = 0;
	
	list<string> listEngines, listQueries;
	char buf[101];
	
	ifstream ifs( argv[1] );
	//ifstream ifs( "./input2.txt" );
	if( !ifs.is_open() )
		return -1;
	
	ofstream ofs( "./output.txt" );
	
	ifs.getline( buf, sizeof(buf) );
	nCaseCnt = atoi( buf );
	
	while( nCnt < nCaseCnt )
	{
		listEngines.clear();
		listQueries.clear();
		
		ifs.getline( buf, sizeof(buf) );
		nEngineCnt = atoi( buf );
		nSubCnt = 0;
		while( nSubCnt < nEngineCnt )
		{
			ifs.getline( buf, sizeof(buf) );
			listEngines.push_back( (string)buf );
			++ nSubCnt;
		}
		
		ifs.getline( buf, sizeof(buf) );
		nQueryCnt = atoi( buf );
		nSubCnt = 0;
		string lastQuery, curQuery;
		while( nSubCnt < nQueryCnt )
		{
			ifs.getline( buf, sizeof(buf) );
			listQueries.push_back( (string)buf );
			++ nSubCnt;
		}
		
		ofs << "Case #" << nCnt + 1 << ":" << " " << getSwitchCount(listEngines, listQueries) << endl;
		
		++ nCnt;
	}
	
	ifs.close();
	ofs.close();
	
    return 0;
}
