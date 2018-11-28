// g2010_C.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <windows.h>
#include <vector>
#include <string>
#include <iostream>
using namespace std;
int GetMoney( int nR, int nK,int nN, int* Array );
void SplitString( string strS,vector<string>& RVct );
int main(int argc, char* argv[])
{
	int Tnum = 0;
	vector<string>RVct;
	int i = 0;

	FILE *stream = fopen( "C-small.in","r" );
	if( stream )
	{
		char line[500];
	    fgets( line,500,stream );
		Tnum = atoi( line );
	    
		int nR,nK,nN;
		int *Array = NULL;
        while( NULL != fgets( line,500,stream ) )
		{
			i++;
			string strLine( line );
			vector<string>TmpVct;
			SplitString( strLine,TmpVct );
			if( i%2 == 1 && TmpVct.size() == 3 )
			{
				nR = atoi( TmpVct[0].c_str() );
				nK = atoi( TmpVct[1].c_str() );
				nN = atoi( TmpVct[2].c_str() );
			}
			if( i%2 == 0 )
			{
				size_t nSize = TmpVct.size();
				Array = new int[nSize];
				for( int k = 0; k < nSize; k++ )
				{
					Array[k] = atoi( TmpVct[k].c_str() );
				}
				int vRet = GetMoney( nR,nK, nN,Array );
				delete Array;
				Array = NULL;
				
				char ss[100];
				sprintf( ss,"Case #%d: %d",i/2,vRet);
				string str(ss);
				RVct.push_back( str );
			}
	
		}
		fclose( stream );
	}
		 HANDLE hFile = CreateFile( "C.out",GENERIC_WRITE|GENERIC_READ,FILE_SHARE_READ|FILE_SHARE_WRITE,NULL,CREATE_ALWAYS,
		FILE_ATTRIBUTE_NORMAL,NULL );
	if( INVALID_HANDLE_VALUE != hFile )
	{
		for( i = 0; i < RVct.size(); i++ )
		{
			DWORD nFileSize = RVct[i].size();
			WriteFile( hFile,RVct[i].c_str(),nFileSize,&nFileSize,NULL );
			WriteFile( hFile,"\r\n",2,&nFileSize,NULL );
		}
		CloseHandle( hFile );
	}
//	printf("Hello World!\n");
	return 0;
}


int GetMoney( int nR, int nK,int nN, int* Array )
{
	int Total = 0;
	int nCount = 0;
	int Cur = nCount;
	int PeopleSum = 0;
	int i = 0;
	
	for( i = 0; i < nN; i++ )
	{
		PeopleSum += Array[i];
	}

	if( PeopleSum <= nK )
	{
		Total = nR*PeopleSum;
		return Total;
	}
	
	
	for( i = 0; i < nR; i++ )
	{
		int TmpSum = 0;
		while( TmpSum + Array[Cur] <= nK )
		{
			TmpSum +=  Array[Cur];
			nCount++;
			Cur = nCount%nN;	
		}
		Total += TmpSum;
	}
	return Total;
}

void SplitString( string strS,vector<string>& RVct )
{
	strS += " ";
	size_t nBegin = 0, nEnd = strS.find( " ");
    while( -1 != nEnd )
	{
		string strT = strS.substr( nBegin, nEnd - nBegin );
		RVct.push_back( strT );
        nBegin = nEnd+1;
		nEnd = strS.find( " ",nBegin );
	}
	return;
}