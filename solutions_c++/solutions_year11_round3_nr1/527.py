#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<string.h>
#include<vector>
#include<queue>
#include<fstream>
#define MAXSIZE 100
using namespace std;

int R, C;
char map[MAXSIZE][MAXSIZE] = {0};

void ini()
{
	memset( map, 0, sizeof(map) );
}

int main()
{
	freopen("A-large.in", "r", stdin );
	freopen("A-large.out", "w", stdout );
	int datacase, t = 0;
	char tem[MAXSIZE];
	scanf("%d", &datacase );
	while( datacase-- )
	{
		ini();
		scanf("%d%d", &R, &C );
		for( int i = 0; i < R; i++ )
		{
			scanf("%s", &map[i] );
		}
		for( int i = 0; i < R-1; i++ )
		{
			for( int j = 0; j < C-1; j++ )
			{
				if( map[i][j] == '#' )
				{
					if( map[i][j+1] == '#' && map[i+1][j] == '#' && map[i+1][j+1] == '#' )
					{
						map[i][j] = '/';
						map[i][j+1] = '\\';
						map[i+1][j] = '\\';
						map[i+1][j+1] = '/';
					}
				}
			}
		}
		int flag = 0;
		for( int i = 0; i < R; i++ )
		{
			for( int j = 0; j < C; j++ )
			{
				if( map[i][j] == '#' )
				{
					flag = 1;
					break;
				}
			}
		}
		printf("Case #%d:\n", ++t );
		if( flag )
		{
			printf("Impossible\n");
		}
		else
		{
			for( int i = 0; i < R; i++ )
				printf("%s\n", map[i] );
		}
	}
	return 0;
}
