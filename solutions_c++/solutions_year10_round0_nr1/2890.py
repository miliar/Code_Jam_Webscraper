// g2010_A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <windows.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <iostream>
using namespace std;


long GetN( int k );

int main(int argc, char* argv[])
{
	int Tnum = 0;
	long * Array = NULL;
	int i = 0,j = 0,k = 0;
	vector< string > VctResult;
	//read file
	FILE *stream = fopen( "A-large.in","r" );
	if( stream )
	{
		char line[500];
	    fgets( line,500,stream );
		Tnum = atoi( line );
		Array = new long[2*Tnum];
		memset( Array,0,2*Tnum );

        while( NULL != fgets( line,500,stream ) )
		{
			string strLine( line );
			size_t nPos = strLine.find( " " );
            Array[i] = atol( strLine.substr( 0,nPos ).c_str() );
			i++;
			Array[i] = atol( strLine.substr( nPos+1,strLine.size()-nPos-1 ).c_str() );
			i++;
		}
		
		fclose( stream );
	}

	for( i = 0 ; i < 2*Tnum; i+=2 )
	{
		long n = Array[i];
		long m = Array[i+1];
		long k = GetN( n );
		m = m%k;
		if( m == k-1 )
		{	
			char sTmp[ 20 ];
			sprintf( sTmp, "Case #%d: %s",i/2+1,"ON" );
			VctResult.push_back( sTmp );
		}
		else
		{
			char sTmp[ 20 ];
			sprintf( sTmp, "Case #%d: %s",i/2+1,"OFF" );
			VctResult.push_back( sTmp );
		}
	}
	 HANDLE hFile = CreateFile( "A.out",GENERIC_WRITE|GENERIC_READ,FILE_SHARE_READ|FILE_SHARE_WRITE,NULL,CREATE_ALWAYS,
		FILE_ATTRIBUTE_NORMAL,NULL );
	if( INVALID_HANDLE_VALUE != hFile )
	{
		for( i = 0; i < VctResult.size(); i++ )
		{
			DWORD nFileSize = VctResult[i].size();
			WriteFile( hFile,VctResult[i].c_str(),nFileSize,&nFileSize,NULL );
			WriteFile( hFile,"\r\n",2,&nFileSize,NULL );
		}
		CloseHandle( hFile );
	}
//	printf("Hello World!\n");
	return 0;
}

long GetN( int k )
{
	long Result = 2;
	for( int i = 1; i < k; i++ )
	{
        Result *= 2;
	}
	return Result;
}