#include <iostream>
#include <fstream>

using namespace std;

typedef unsigned int uint;
typedef unsigned long ulong;

int numCases;
int N;
uint k;
uint R;
uint g[1000];

int main (int argc, char * const argv[]) 
{
	if ( argc != 2 ) return -1;

	FILE * f = fopen(argv[1], "r");
	fscanf(f, "%d", &numCases);

	for ( int caseIndex = 0; caseIndex < numCases; caseIndex++ )
	{
		uint earned = 0;
		uint lineHeadIndex = 0;
		cout << "Case #" << caseIndex + 1 << ": ";
		fscanf(f, "%d %d %d", &R, &k, &N);
		for ( int n = 0; n < N; ++n )
		{
			fscanf(f, "%d", &g[n]);
		}
		
		for ( int r = 0; r < R; ++r )
		{
			uint firstOnIndex = lineHeadIndex;
			uint numRiders = 0;
			uint nextGroupSize = g[lineHeadIndex];
			while ( numRiders + nextGroupSize <= k )
			{
				numRiders += nextGroupSize;
				if ( ++lineHeadIndex >= N ) lineHeadIndex = 0;
				
				if ( lineHeadIndex == firstOnIndex )
				{	// Looped around. no more waiting.
					lineHeadIndex = 0;
					break;
				} else
				{
					nextGroupSize = g[lineHeadIndex];
				}
			}
			earned += numRiders;
		}
		cout << earned << endl;
	}		

	fclose(f);
	return 0;
}
