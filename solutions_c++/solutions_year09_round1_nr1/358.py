#include <stdio.h>
#include <assert.h>
#include <iostream>
#include <vector>
#include <map>
#include <string>

using namespace std;

#define MAX_BASE 10

typedef map<int,char> HistoryRec;
typedef HistoryRec::iterator HisRecIt;

HistoryRec fCase[MAX_BASE+1], sCase[MAX_BASE+1];

void ChangeToBase( int num, int base, vector<int> &ret )
{
	ret.clear();
	while( num )
	{
		ret.push_back( num%base );
		num /= base;
	}
}

bool IsNumberHappy( int num, int base )
{
	vector<int> tran;
	HistoryRec selfRec;
	HisRecIt it;
	int i;
	int n = num;
	while( true )
	{
		if( n==1 || sCase[base].find(n)!=sCase[base].end() )
		{
			sCase[base].insert( selfRec.begin(),selfRec.end() );
			return true;
		}
		if( fCase[base].find(n)!=fCase[base].end() || selfRec.find(n)!=selfRec.end() )
		{
			fCase[base].insert( selfRec.begin(),selfRec.end() );
			return false;
		}
		selfRec.insert( make_pair(n,' ') );
		ChangeToBase( n, base, tran );
		for( i=n=0;i<(int)tran.size();i++ )
			n += tran[i]*tran[i];
	}
	assert( 0 );
	return true;
}

int GetSmallestHappy( vector<int> bases )
{
	int i,j,k;
	int ret = 2;
	for( i=0; i<(int)bases.size(); i++ )
	{
		printf( "%d\n", i );
		for( j=ret; ; j ++ )
		{
			if( !IsNumberHappy(j,bases[i]) )
				continue;
			for( k=0;k<i;k++ )
			{
				if( !IsNumberHappy(j,bases[k]) )
					break;
			}
			if( k<i )
				continue;
			break;
		}
		if( j>ret )
			ret = j;
	}
	return ret;
}

#define BufLen 1024
void MultiBase()
{
	FILE *fin, *fout;
	fin = fopen( "in.txt", "r" );
	fout = fopen( "out.txt", "w" );
	assert( fin && fout );

	int tLen, tint;
	char buf[BufLen], *pbuf;
	vector<int> iBuf;
	fgets( buf, BufLen, fin );
	sscanf( buf, "%d", &tLen );
	for( int i=0; i<tLen; i++ )
	{
		fgets( buf, BufLen, fin );
		pbuf = buf;
		iBuf.clear();
		while( true )
		{
			while( *pbuf==' ' )
				pbuf ++;
			if( *pbuf==0 || *pbuf=='\n' || *pbuf=='\r' )
				break;
			if( sscanf( pbuf, "%d", &tint )==0 )
				break;
			iBuf.push_back( tint );
			while( *pbuf>='0' && *pbuf<='9' )
				pbuf ++;
		}
		printf( "-----------%d\n", i );
		fprintf( fout, "Case #%d: %d\n", i+1, GetSmallestHappy(iBuf) );
	}
	fclose( fin );
	fclose( fout );
}

int main()
{
	MultiBase();
	return 0;
}