#include <iostream>
#include <fstream>

using namespace std;

typedef unsigned int uint;
typedef unsigned long ulong;

int numCases;
int N;
char R[100];
int P[100];
int posO = 1;
int posB = 1;
int numSecs = 0;
int curInst = 0;
int curInstO = 0;
int curInstB = 0;


int findInst(int from, char bot)
{
	for (int i = from; i < N; i++)
	{
		if (R[i] == bot)
		{
			return i;
		}
	}
	return N;
}

int main (int argc, char * const argv[]) 
{
	if ( argc != 2 ) return -1;

	FILE * f = fopen(argv[1], "r");
	fscanf(f, "%d", &numCases);

	for ( int caseIndex = 0; caseIndex < numCases; caseIndex++ )
	{
		cout << "Case #" << caseIndex + 1 << ": ";
		fscanf(f, "%d", &N);
//		printf("N = %d\n", N);
		for (int i = 0; i < N; i++)
		{
			fscanf(f, " %c %d", &(R[i]), &(P[i]));
		}
		
//		for (int i = 0; i < N; i++)
//		{
//			printf("R = %c P = %d\n", R[i], P[i]);
//		}
		
		numSecs = 0;
		posO = 1;
		posB = 1;
		curInst = 0;
		curInstO = findInst(0, 'O');
		curInstB = findInst(0, 'B');

		while (curInst < N)
		{
			char curBot = R[curInst];
			int curButton = P[curInst];
			if (curBot == 'O')
			{
				if (posO == curButton)
				{	// O presses button.
					curInst++;
					curInstO = findInst(curInst, 'O');
				} else if (posO < curButton)
				{
					posO++;
				} else
				{
					posO--;
				}
				
				// B can move closer or wait but not press.
				if (posB < P[curInstB])
				{
					posB++;
				} else if (posB > P[curInstB])
				{
					posB--;
				}
			} else
			{
				if (posB == curButton)
				{	// B presses button.
					curInst++;
					curInstB = findInst(curInst, 'B');
				} else if (posB < curButton)
				{
					posB++;
				} else
				{
					posB--;
				}
				
				// O can move closer or wait but not press.
				if (posO < P[curInstO])
				{
					posO++;
				} else if (posO > P[curInstO])
				{
					posO--;
				}
			}

			numSecs++;
		}
		
		cout << numSecs << endl;
	}

	fclose(f);
	return 0;
}
