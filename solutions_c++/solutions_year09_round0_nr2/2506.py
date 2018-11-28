#include <windows.h>
#include <stdio.h>

#include <map>


int main( int argc, char** argv ) {
	// input
	FILE* in = fopen( argv[ 1 ], "r" );

	long n = long();
	fscanf( in, "%ld", &n );

	// output
	FILE* out = fopen( "output.txt", "w" );

	// 
	for( long k = 0; k < n; k++ ) {
		// size
		long w = long();
		long h = long();

		fscanf( in, "%ld %ld", &h, &w );

		// array
		long* heights = new long[ w * h ];
		long* areas = new long[ w * h ];

		// heights
		for( long i = 0; i < h; i++ ) {
			for( long j = 0; j < w; j++ ) {
				long idx = i * w + j;

				long hh = long();
				fscanf( in, "%ld", &hh );

				heights[ idx ] = hh;
				areas[ idx ] = 0;
			}
		}

		// area
		bool loop = true;
		long maxId = 1;

		while( loop ) {
			int id = maxId;
			long row = -1;
			long col = -1;
			long maxH = -1;
			for( long i = 0; i < h; i++ ) {
				for( long j = 0; j < w; j++ ) {
					long idx = i * w + j;
	
					if( heights[ idx ] > maxH && areas[ idx ] == 0 ) {
						row = i;
						col = j;
						maxH = heights[ idx ];
					}
				}
			}
			if( row < 0 || col < 0 ) {
				loop = false;
			}

			while( row >= 0 && col >= 0 ) {
				long idx = row * w + col;
				int prevId = areas[ idx ];

				if( prevId > 0 ) {
					for( long i = 0; i < h; i++ ) {
						for( long j = 0; j < w; j++ ) {
							int tmpIdx = i * w + j;

							if( areas[ tmpIdx ] == id ) {
								areas[ tmpIdx ] = prevId;
							}
						}
					}
					id = prevId;
				}

				areas[ idx ] = id;
				
				int nextRow = -1;
				int nextCol = -1;

				int nextRows[] = { row - 1, row, row, row + 1 };
				int nextCols[] = { col, col - 1, col + 1, col };

				long minH = heights[ idx ];
				for( long i = 0; i < 4; i++ ) {
					int tmpRow = nextRows[ i ];
					int tmpCol = nextCols[ i ];

					if( tmpRow >= 0 && tmpRow < h && tmpCol >= 0 && tmpCol < w ) {
						int nextIdx = tmpRow * w + tmpCol;
						if( heights[ nextIdx ] < minH ) {
							nextRow = tmpRow;
							nextCol = tmpCol;
							minH = heights[ nextIdx ];
						}
					}
				}

				row = nextRow;
				col = nextCol;
			}

			maxId++;
		}

		std::map< long, char > mp;
		char maxC = 'a';

		fprintf( out, "Case #%d:\n", k + 1 );

		for( long i = 0; i < h; i++ ) {
			for( long j = 0; j < w; j++ ) {
				long idx = i * w + j;

				long a = areas[ idx ];
				char c = maxC;
				if( mp.find( a ) == mp.end() ) {
					mp[ a ] = c;
					maxC = maxC + 1;
				}
				else {
					c = mp[ a ];
				}

				if( j > 0 ) {
					fprintf( out, " " );
				}
				fprintf( out, "%c", c );
			}
			fprintf( out, "\n" );
		}

		delete[] heights;
		delete[] areas;
	}

	fclose( in );
	fflush( out );
	fclose( out );
}
