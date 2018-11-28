#include <iostream>
#include <cstdio>
#include <string>

#define MAX_H 101
#define MAX_W 101

unsigned int input[MAX_H+1][MAX_W+1];
int map[MAX_H][MAX_W];
char final[MAX_H][MAX_W];

int main()
{
	int t, h, w;
	int T, H, W;
	int i, j;
	
	scanf("%d", &T);

	for(t=1;t<=T;t++)
	{
		memset(input, 0xff, sizeof(input));
		memset(map, 0, sizeof(map));

		scanf("%d %d", &H, &W);
		for(h=1;h<=H;h++)
		{
			for(w=1;w<=W;w++)
			{
				scanf("%d", &input[h][w]);
			}
		}

		int cur = 'a';
		// start
		for(h=1;h<=H;h++)
		{
			for(w=1;w<=W;w++)
			{
				// allocate char
				if( map[h][w]==0 )
					map[h][w] = cur++;

				// find dir
				int x, y;
				int min = input[h-1][w];
				if( min > input[h][w-1] ) min = input[h][w-1];
				if( min > input[h][w+1] ) min = input[h][w+1];
				if( min > input[h+1][w] ) min = input[h+1][w];
				if( min >= input[h][w] )
					continue;
				if( min==input[h-1][w] )
					x = -1, y = 0;
				else if( min==input[h][w-1] )
					x = 0, y = -1;
				else if( min==input[h][w+1] )
					x = 0, y = 1;
				else if( min==input[h+1][w] )
					x = 1, y = 0;

				// there alloc?
				if( map[h+x][w+y]==0 )
					map[h+x][w+y] = map[h][w];
				else
				{
					// my num -> there num
					for(i=1;i<=H;i++)
						for(j=1;j<=W;j++)
							if( map[i][j]==map[h][w] )
								map[i][j] = map[h+x][w+y];
				}
			}
		}

		// new labeling
		char start = 'a';
		memset(final, 0, sizeof(final));

		for(h=1;h<=H;h++)
		{
			for(w=1;w<=W;w++)
			{
				if( final[h][w]==0 )
				{
					cur = map[h][w];
					for(i=1;i<=H;i++)
					{
						for(j=1;j<=W;j++)
						{
							if( map[i][j]==cur )
								final[i][j] = start;
						}
					}
					start++;
				}
			}
		}
		
		printf("Case #%d:\n", t);
		for(h=1;h<=H;h++)
		{
			for(w=1;w<=W;w++)
			{
				printf("%c", final[h][w]);
				if( w!=W )
					printf(" ");
			}
			printf("\n");
		}
	}
	return 0;
}
