#include <stdio.h>
#include <assert.h>
#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <limits>

using namespace std;

#define MAX_LEN 40

class CrazyRows
{
public:
	void Solve(const char *strFilIn, const char *strFileOut = "out.txt");
	int GetSwapTimes();
	int SwapDown(int pos, int who);
	int SwapUp(int pos, int who);
private:
	int m_len;
	int m_matrix[MAX_LEN][MAX_LEN];
	int m_rec[MAX_LEN];
};

int CrazyRows::SwapDown(int pos, int who)
{
	int ret = 0;
	for( int i=pos+1;i<=who; i++ )
	{
		if( m_rec[i]>=who )
		{
			ret += SwapDown( i,m_rec[i] );
		}
		else
		{
			swap( m_rec[i], m_rec[i-1] );
			ret ++;
		}
	}
	return ret;
}

int CrazyRows::SwapUp( int pos, int who )
{
	int ret = 0;
	for( int i=pos-1;i>=who;i-- )
	{
		if( m_rec[i]<=who )
		{
			ret += SwapUp( i,m_rec[i] );
		}
		else
		{
			swap( m_rec[i], m_rec[i+1] );
			ret ++;
		}
	}
	return ret;
}

int CrazyRows::GetSwapTimes()
{
	int ret = 0;
	int i, i1,i2,j;
	for( i=0;i<m_len;i++ )
	{
		for( j=m_len-1;j>=0;j-- )
		{
			if( m_matrix[i][j]==1 )
				break;
		}
		m_rec[i] = j;
	}
	for( i=0;i<m_len;i++ )
	{
		if( m_rec[i]>i )
		{
			for( j=i+1;j<m_len;j++ )
			{
				if( m_rec[j]<=i )
					break;
			}
			for( ;j>i;j-- )
			{
				swap( m_rec[j],m_rec[j-1] );
				ret ++;
			}
		}
	}
	return ret;
}

void CrazyRows::Solve(const char *strFilIn, const char *strFileOut)
{
	static const BufLen = 1024;
	char buf[BufLen];
	FILE *fin, *fout;
	fin = fopen( strFilIn, "r" );
	fout = fopen( strFileOut, "w" );
	assert( fin && fout );

	int tLen;
	int i,j,k;
	fgets( buf, BufLen, fin );
	sscanf( buf, "%d", &tLen );
	for( i=0; i<tLen; i++ )
	{
		fgets( buf, BufLen, fin );
		sscanf( buf,"%d", &m_len );
		for( j = 0; j<m_len; j++ )
		{
			fgets( buf, BufLen, fin );
			for( k=0;k<m_len;k++ )
				m_matrix[j][k] = (buf[k]-'0');
		}
		fprintf( fout, "Case #%d: %d\n", i+1, GetSwapTimes() );
		printf( "-----------%d\n", i );
	}
	fclose( fin );
	fclose( fout );
}

int main()
{
	CrazyRows cr;
	cr.Solve("A-large.in");
	return 0;
}