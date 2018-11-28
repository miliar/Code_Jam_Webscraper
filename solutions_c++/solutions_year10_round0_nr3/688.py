#include <cstdio>

const int max = 1002;

inline int next( int i, int n )
{
	return i==n ? 1 : i+1;
}

int main( )
{
	// open file
	FILE* in = fopen( "in.txt", "r" );
	FILE* out = fopen( "out.txt", "w" );


	int R, K, N;
	int g[max];

	__int64 score[max];		// each round score
	int round[max];		// the head of each round
	__int64 result;			// the result
	

	int i, size;		// loop index and the size of round
	int start, end;
	int tmpscore;

	int loopsize, loopstart;
	__int64 loopscore;

	// for cases
	int t, T;
	fscanf( in, "%d", &T );

	// each case
	for( t=1; t<=T; ++t )
	{
		// input the data and initial
		fscanf( in, "%d%d%d", &R, &K, &N );
		
		for( i=1; i<=N; ++i )
		{
			fscanf( in, "%d", &g[i] );
			
			round[i] = 0;
		}
		

		// do the round until loop
		score[0] = 0;
		start = 1;
		size = 1;
		while( round[start]==0 )
		{
			end = next( start, N );
			tmpscore = g[start];
			while( end!=start && tmpscore+g[end]<=K )
			{
				tmpscore += g[end];
				end = next( end, N );				
			}
			round[start] = size;
			score[size] = score[size-1] + tmpscore;
			start = end;
			size++;
		}
		
		loopsize = size - round[start];
		loopstart = round[start];
		loopscore = score[size-1] - score[loopstart-1];
		


		if( R<loopsize )
			result = score[R];
		else
		{
			result = score[loopstart-1];
			__int64 tmp = (R-loopstart+1) / loopsize;

			result += tmp * loopscore;
			tmp = R - loopstart + 1 - tmp * loopsize;

			if( tmp>0 )
				result += score[tmp+loopstart-1] - score[loopstart-1];

		}

		// print result
		fprintf( out, "Case #%d: %I64d\n", t, result );

	}

	// close file
	fclose( in );
	fclose( out );
	return 0;
}