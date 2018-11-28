// qualification watersheds2.cpp
#include<iostream>
#include<sstream>
#include<algorithm>
#include<numeric>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<list>
#include<stack>
#include<queue>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<cctype>
#include<climits>
#include<cfloat>

using namespace std;

char basins[100][100] = {0};
int altitudes[100][100] = {0};
bool isvalid( int i, int j, int H, int W );
int p[10000] = {0}, rank[10000] = {0};

int make_set(int x)
{
		p[x] = x; rank[x] = 0;
}

int find_set(int x)
{
		if (x != p[x]) p[x] = find_set(p[x]);
		return p[x];
}
void link(int x, int y)
{
	if (rank[x] > rank[y]) p[y] = x;
	else 
	{
		p[x] = y;
		if (rank[x] == rank[y]) rank[y]++;
	}
}

void unionSets(int x, int y)
{
	link(find_set(x),find_set(y));
}


int main()
{
    int T;
    scanf( "%d", &T );
    for( int caseNo = 1; caseNo <= T; caseNo++ )
    {
	int H, W;
	scanf( "%d%d", &H, &W );
	for( int i = 0; i < H; i++ )
	{
	    for( int j = 0; j < W; j++ )
	    {
		scanf( "%d", &altitudes[i][j] );
		basins[i][j] = 'z' + 1;
	    }
	}
	for (int i = 0; i < 10000; i++)
		p[i] = i;
	printf( "Case #%d:\n", caseNo );
	
	    for( int i = 0; i < H; i++ )
	    {
		for( int j = 0; j < W; j++ )
		{
		    int lowest = altitudes[i][j];
		    if( isvalid( i - 1, j, H, W ) )   
			lowest = min( altitudes[i-1][j], lowest );
		    if( isvalid( i, j - 1, H, W ) )
			lowest = min(  altitudes[i][j-1], lowest );
		    if( isvalid( i, j + 1, H, W ) )
			lowest = min( altitudes[i][j+1], lowest );
		    if( isvalid( i + 1, j, H, W ) )
			lowest = min( altitudes[i+1][j], lowest );
		    bool sink = ( lowest == altitudes[i][j] );
		    bool foundfirst = false;
		    int nexti = 0, nextj = 0;
		    if( !foundfirst && isvalid( i - 1, j, H, W ) )   
			 if( lowest == altitudes[i-1][j] )
			 	nexti = i - 1, nextj = j, foundfirst = true;
		    if( !foundfirst && isvalid( i, j - 1, H, W ) )
			 if( lowest == altitudes[i][j-1] )
			 	nexti = i, nextj = j - 1, foundfirst = true;
		    if( !foundfirst && isvalid( i, j + 1, H, W ) )
			 if( lowest == altitudes[i][j+1] )
			 	nexti = i, nextj = j + 1, foundfirst = true;
		    if( !foundfirst && isvalid( i + 1, j, H, W ) )
			 if( lowest == altitudes[i+1][j] )		
	     		     nexti = i + 1, nextj = j, foundfirst = true;
	            if( sink == false )
	            	unionSets( 100 * i + j, 100 * nexti + nextj );
		    
		}
	    }
	
	char currentc = 'a';
	map<int, char> lexico;
	for( int i = 0; i < H; i++ )
	{
	    for( int j = 0; j < W; j++ )
	    {
	    	int myset = find_set( 100 * i + j );
		if( lexico.find( myset ) == lexico.end() )
		{
		    lexico[myset] = currentc++;
		    basins[i][j] = lexico[myset];
		}
		else
		{
		    basins[i][j] = lexico[myset];
		}   	      
	    }
	}
	for( int k = 0; k < H; k++ )
	{
	    for( int l = 0; l < W; l++ )
	    {
		printf( "%c", basins[k][l] );
		if( l != W - 1 )
		    printf( " " );
	    }
	    printf( "\n" );
	}	
    }
    return 0;
}

bool isvalid( int i, int j, int H, int W )
{
    if( i >= 0 && i < H && j >= 0 && j < W )
	return true;
    return false;
}
