#include <stdio.h>

#include <iostream>
#include <string>
#include <vector>

using namespace std ;


int main()
{
	int i, j, k, l ;
	FILE *in = fopen("file.in", "r") ;
	FILE *out = fopen("file.out", "w") ;
	int R, C, T ;
	char board[55][55] ;
	
	fscanf(in, "%d\n", &T) ;
	for(l=1;l<=T;l++)
	{
		fscanf(in, "%d %d\n", &R, &C) ;
		for(i=0;i<R;i++)
		{
			for(j=0;j<C;j++) fscanf(in, "%c", &board[i][j]) ;
			fscanf(in, "\n") ;
		}
		
		for(i=0;i<R;i++)
		{
			for(j=0;j<C;j++)
				if( board[i][j] == '#' )
				{
					if( i+1 < R && board[i+1][j] == '#' && j+1 < C && board[i][j+1] == '#'
					   && board[i+1][j+1] == '#' )
					{
						board[i][j] = '/' ;
						board[i][j+1] = '\\' ;
						board[i+1][j] = '\\' ;
						board[i+1][j+1] = '/' ;
					}
				}
		}
		
		for(i=0;i<R;i++)
		{
			for(j=0;j<C;j++) if( board[i][j] == '#' ) break ;
			if( j < C ) break ;
		}
		fprintf(out, "Case #%d:\n", l) ;
		if( i < R ) fprintf(out, "Impossible\n"); 
		else for(i=0;i<R;i++)
		{
			for(j=0;j<C;j++) fprintf(out, "%c", board[i][j]) ;
			fprintf(out, "\n") ;
		}
	}
	
	return 0 ;
}
