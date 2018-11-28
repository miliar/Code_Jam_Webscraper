#include<iostream>
#include<stdlib.h>
#include<string.h>
#include<stdio.h>
#include<fstream>
#include<queue>
#define MAXSIZE 1000
using namespace std;

int button[MAXSIZE] = {0};
int O[MAXSIZE] = {0};
int B[MAXSIZE] = {0};
int NO, NB, n, PB, PO, ans, moveB, moveO;

void ini()
{
	moveB = moveO = ans = NO = NB = 0;
	PB = PO = 1;
	memset( O, 0, sizeof(O) );
	memset( B, 0, sizeof(B) );
}

int main()
{
	freopen( "A-large.in", "r", stdin );
	freopen( "A-large.out", "w", stdout );
	int datacase, position , t = 0;
	char word[100];
	scanf( "%d", &datacase );
	while( datacase-- )
	{
		ini();
		scanf( "%d", &n );
		for( int i = 0; i < n; i++ )
		{
			scanf("%s%d", word, &position );
			if( word[0] == 'O' )
			{
				button[i] = position + 1000;
				O[NO++] = position + 1000;
			}
			else
			{
				button[i] = position + 2000;
				B[NB++] = position + 2000;
			}
		}
		for( int i = 0; i < n; i++ )
		{
			int now = button[i];
			//printf("%d %d %d %d %d %d\n", PB, PO, moveB, moveO, now, ans );
			if( now < 1500 )
			{
				
				now = now % 1000;
				if( PO <= now )
				{
					if( moveB + PO >= now )
					{
						ans++;
						moveB = 0;
						PO = now;
						moveO++;
						continue;
					}
					else
					{
						//now = now - moveB;
						PO = PO + moveB;
						moveB = 0;
					}
					for( int j = PO; j <= now; j++ )
					{
						ans++;
						moveO++;
					}
					PO = now;
				}
				else
				{
					if( PO - moveB <= now )
					{
						ans++;
						moveB = 0;
						PO = now;
						moveO++;
						continue;
					}
					else
					{
						//now = now + moveB;
						PO = PO - moveB;
						moveB = 0;
					}
					for( int j = PO; j >= now; j-- )
					{
						ans++;
						moveO++;
					}
					PO = now;
				}
			}
			else 
			{
				
				now = now % 2000;
				if( PB <= now )
				{
					if( moveO + PB >= now )
					{
						ans++;
						moveO = 0;
						PB = now;
						moveB++;
						continue;
					}
					else
					{
						//now = now - moveO;
						PB = PB + moveO;
						moveO = 0;
					}
					for( int j = PB; j <= now; j++ )
					{
						ans++;
						moveB++;
					}
					PB = now;
				}
				else
				{
					if( PB - moveO <= now )
					{
						ans++;
						moveO = 0;
						PB = now;
						moveB++;
						continue;
					}
					else
					{
						//now = now + moveO;
						PB = PB - moveO;
						moveO = 0;
					}
					for( int j = PB; j >= now; j-- )
					{
						ans++;
						moveB++;
					}
					PB = now;
				}
			}
			//printf("%d %d %d %d %d %d\n\n", PB, PO, moveB, moveO, now, ans );
		}
		printf("Case #%d: %d\n", ++t, ans );
	}	
	return 0;
}
