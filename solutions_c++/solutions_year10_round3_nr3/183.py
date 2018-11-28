#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

#include <algorithm>
#include <set>
#include <map>
#include <queue>

using namespace std;

#include <iostream>
#define DB(x) cout << #x " == " << (x) << endl

bool mapa[700][700], mark[700][700];
char linha[500];
int hist[100000][3], res[10000][2];
int m,n;

int contar(int i, int j)
{
	int k = 1;
	while( j+k < n && i+k < m)
	{
		//if( mapa[i][j+k] != mapa[i][j+k-1] )
		{
			int l = 0;
			for( l = 0 ; l <= k ; ++l )
			{
				if( mapa[i+k][j+l] == mapa[i+k-1][j+l] || mark[i+k][j+l] ) break;
				if( mapa[i+l][j+k] == mapa[i+l][j+k-1] || mark[i+l][j+k]  ) break;
			}
			if( l <= k ) break;
		}
		++k;
	}
	return k;
}

void process()
{
	bool novo = true;
	int temp, h = 0, r = 0;
	int maxi, maxj, maxt;
	
	while( novo )
	{
		novo = false;
		maxt = 1;
		for( int i = 0 ; i < m ; ++i )
		{
			for( int j = 0 ; j < n ; ++j ) if( !mark[i][j] )
			{
				temp = contar(i,j);
				if( temp > maxt )
				{
					maxt = temp;
					maxi = i;
					maxj = j;
					novo = true;
				}
			}
		}
		
		if( novo && h && hist[h-1][2] != maxt )
		{
			res[r][0] = hist[h-1][2];
			res[r++][1] = h;
			h = 0;
		}
		if( novo )
		{
			hist[h][0] = maxi;
			hist[h][1] = maxj;
			hist[h++][2] = maxt;
			for( int i = 0 ; i < maxt ; ++i )
			{
				for( int j = 0 ; j < maxt ; ++j )
				{
					mark[maxi+i][maxj+j] = true;
				}
			}
		}
	}
	if( h )
	{
		res[r][0] = hist[h-1][2];
		res[r++][1] = h;
		h = 0;
	}
	res[r][0] = 1;
	int sum = 0;
	for( int i = 0 ; i < r ; ++i )
	{
		sum += res[i][0]*res[i][1]*res[i][0];
	}
	if( sum < m*n )
	{
		res[r++][1] = m*n-sum;
	}
	
	printf("%d\n", r);
	for( int i = 0 ; i < r ; ++i )
	{
		printf("%d %d\n", res[i][0], res[i][1]);
	}
}

bool read()
{
	scanf("%d%d", &m, &n);
	int nt = n/4, temp, tj;
	for( int i = 0 ; i < m ; ++i )
	{
		scanf("%s", linha);
		for( int j = 0, tj = 0 ; j < nt ; ++j, tj+=4 )
		{
			if( linha[j] >= '0' && linha[j] <= '9' )
			{
				temp  = linha[j] - '0'; 
			}
			else
			{
				temp = linha[j] - 'A' + 10;
			}
			mapa[i][tj] = temp&8;
			mapa[i][tj+1] = temp&4;
			mapa[i][tj+2] = temp&2;
			mapa[i][tj+3] = temp&1;
			//printf("%d%d%d%d", mapa[i][tj], mapa[i][tj+1], mapa[i][tj+2], mapa[i][tj+3]);
		}
		//printf("\n");
	}
	memset(mark, false, sizeof(mark));
}


int main()
{
	int c; scanf("%d", &c);
	int t = 1;
	while( c-- )
	{
		read();
		printf("Case #%d: ", t++);
		process();
	}	
	return 0;
}
