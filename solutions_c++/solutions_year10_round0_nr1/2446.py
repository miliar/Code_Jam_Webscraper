#include <iostream>
#include <fstream>

using namespace std;

typedef unsigned int uint;
typedef unsigned long ulong;

int numCases;
int N;
uint K;


int main (int argc, char * const argv[]) 
{
	if ( argc != 2 ) return -1;

	FILE * f = fopen(argv[1], "r");
	fscanf(f, "%d", &numCases);

	for ( int caseIndex = 0; caseIndex < numCases; caseIndex++ )
	{
		cout << "Case #" << caseIndex + 1 << ": ";
		fscanf(f, "%d %d", &N, &K);
		bool isOn = true;
		for ( int bit = 0; bit < N; ++bit )
		{
			if ( (K & (1 << bit )) == 0 )
			{
				isOn = false;
				break;
			}
		}
		if ( isOn )
		{
			cout << "ON\n";
		} else
		{
			cout << "OFF\n";
		}
	}		

	fclose(f);
	return 0;
}
