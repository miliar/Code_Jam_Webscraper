#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_N 110

int check_seq(char* map, char color, int N, int K, int line, int col, int d_line, int d_col)
{
	int o_line=line, o_col=col;
	//printf("(%d %d  %d %d %c) try\n", o_line, o_col, d_line, d_col, color);
	for(int i=0;i<K;i++)
	{
		if(line<0 || line>=N || col<0 || col>=N) return 0;
		//printf("(%d %d  %d %d %c %c)\n", line, col, d_line, d_col, color, map[line*MAX_N+col]);
		if(map[line*MAX_N+col]!=color) return 0;
		line += d_line;
		col += d_col;
		//printf("(%d %d  %d %d %c %c) ok\n", line, col, d_line, d_col, color, map[line*MAX_N+col]);
	}
	//printf("(%d %d  %d %d %c) OK\n", o_line, o_col, d_line, d_col, color);
	return 1;
}

int check(char* map, char color, int N, int K)
{
	for(int line=0;line<N;line++)
	{
		for(int col=0;col<N;col++)
		{
			if(map[line*MAX_N+col]!=color) continue;
			if(check_seq(map, color, N, K, line, col,  0,  1)) return 1; // right
			if(check_seq(map, color, N, K, line, col,  1,  1)) return 1; // right-down
			if(check_seq(map, color, N, K, line, col,  1,  0)) return 1; // down
			if(check_seq(map, color, N, K, line, col,  1, -1)) return 1; // left-down
			if(check_seq(map, color, N, K, line, col,  0, -1)) return 1; // left
			if(check_seq(map, color, N, K, line, col, -1, -1)) return 1; // left-up
			if(check_seq(map, color, N, K, line, col, -1,  0)) return 1; // up
			if(check_seq(map, color, N, K, line, col, -1,  1)) return 1; // right-up
		}
	}
	return 0;
}

int main()
{
	char map[MAX_N*MAX_N];
	int T=0;
	scanf("%d", &T);
	for(int i=0;i<T;i++)
	{
		memset(map, 0, sizeof(map));
		
		int N=0, K=0;
		scanf("%d %d", &N, &K);
		gets(map);
		for(int line=0;line<N;line++)
		{
			gets(&map[line*MAX_N]);
		}
		//printf("%d %d\n", N, K);
		//for(int line=0;line<N;line++)
		//{
		//	printf("%s\n", &map[line*MAX_N]);
		//}
		
		//continue;
		for(int line=0;line<N;line++)
		{
			for(int col=N-1;col>=0;col--)
			{
				int m;
				for(m=col;m>=0;m--)
				{
					if(map[line*MAX_N+m]!='.') break;
				}
				if(m>=0)
				{
					// swap m and col
					char tmp = map[line*MAX_N +col];
					map[line*MAX_N +col] = map[line*MAX_N +m];
					map[line*MAX_N +m] = tmp;
				}
			}
		}
		for(int line=0;line<N;line++)
		{
			//printf("%s\n", &map[line*MAX_N]);
		}
		
		// check
		int B = check(map, 'B', N, K);
		int R = check(map, 'R', N, K);
		//printf("B %d\n", B);
		//printf("R %d\n", R);
		char* table[]={"Neither", "Red", "Blue", "Both"};
		printf("Case #%d: %s\n", i+1, table[B*2+R]);
	}
}
