// A1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <windows.h>
#include <map>
#include <vector>
using namespace std;
void SplitWord( string str,vector< string >&strVct );
int Serct( map<int,int>& NumMap );

int main(int argc, char* argv[])
{
	int TCase = 0;
  //  vector<int> NUmVct;
	map<int,int>NumMap;
    vector<string>ResVct;
	int NNUm = 0,i = 0,j= 0;
	FILE*stream = fopen( "A-large.in","r" );
	if( stream )
	{
		char line[100];
		
		while( NULL != fgets( line,100,stream ) )
		{
			string str = line;
			if( TCase == 0 )
			{
				TCase = atoi( str.c_str() );
				continue;
			}
			if( NNUm == 0)
			{
				NNUm = atoi( str.c_str() );
				continue;
			}
			vector<string>TmpVct;
            SplitWord( str, TmpVct );
	//	    NUmVct.push_back( atoi( TmpVct[1].c_str()) );
			NumMap[atoi( TmpVct[0].c_str())] = atoi( TmpVct[1].c_str());
		
			i++;
			if( i == NNUm )
			{
				j++;
				NNUm = 0;
				i = 0;
				int Re = Serct( NumMap );
				NumMap.clear();
				char Tmp[512];
				sprintf( Tmp, "Case #%d: %d", j,Re );
				ResVct.push_back( Tmp );
			}
			
		}
		fclose( stream );
	}
	
	 HANDLE hFile = CreateFile( "AL.out",GENERIC_WRITE|GENERIC_READ,FILE_SHARE_READ|FILE_SHARE_WRITE,NULL,CREATE_ALWAYS,
		FILE_ATTRIBUTE_NORMAL,NULL );
	if( INVALID_HANDLE_VALUE != hFile )
	{
		for( i = 0; i < ResVct.size(); i++ )
		{
			DWORD nFileSize = ResVct[i].size();
			WriteFile( hFile,ResVct[i].c_str(),nFileSize,&nFileSize,NULL );
			WriteFile( hFile,"\r\n",2,&nFileSize,NULL );
		}
		CloseHandle( hFile );
	}
	return 0;
}

void SplitWord( string str,vector< string >&strVct )
{
	strVct.clear();
	if( !str.size() ) return;

	str += " ";
	size_t nBegin = 0,nEnd = -1;
	nEnd = str.find( " " );
	while( -1 != nEnd )
	{
		string strSub = str.substr( nBegin, nEnd - nBegin );
		strVct.push_back( strSub );
		nBegin = nEnd+1;
		nEnd = str.find( " ",nBegin+1 );
	}
	return;
}

int Serct(map<int,int>& NumMap )
{
	int Result = 0;
    vector<int>NumVct;
	map<int,int>::iterator iMap = NumMap.begin();
	while( iMap != NumMap.end() )
	{
		NumVct.push_back( iMap->second );
		iMap++;
	}
    int i, j ;
	int nSize = NumVct.size();
	for( i = 0; i < nSize; i++ )
	{
		for( j = i+1; j < nSize; j++ )
		{
			if( NumVct[j] < NumVct[i] )
			{
				Result++;
			}
		}
	}
	return Result;
}