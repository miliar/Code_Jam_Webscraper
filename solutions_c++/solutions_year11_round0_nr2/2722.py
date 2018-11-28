#include <iostream>
#include <fstream>

using namespace std;

typedef unsigned int uint;
typedef unsigned long ulong;

int numCases;
int C;
int D;
int N;
char combine[36][3];
char oppose[28][2];
char seq[100];
char result[100];
int resIndex;

char combiner(char a, char b)
{
	for (int i = 0; i < C; i++)
	{
		if ((a == combine[i][0] && b == combine[i][1]) || (a == combine[i][1] && b == combine[i][0]))
		{
			return combine[i][2];
		}
	}
	return 0;
}

bool opposePair(char a, char b)
{
	for (int i = 0; i < D; i++)
	{
		if ((a == oppose[i][0] && b == oppose[i][1]) || (a == oppose[i][1] && b == oppose[i][0]))
		{
			return true;
		}
	}
	return false;
}

bool opposer(char a)
{
	for (int i = 0; i < resIndex; i++)
	{
		if (opposePair(a, result[i]))
		{
			return true;
		}
	}
	return false;
}

void printResult()
{
	cout << "[";
	if (resIndex > 0)
	{
		cout << result[0];
	}
	for (int i = 1; i < resIndex; i++)
	{
		cout << ", " << result[i];
	}
	cout << "]" << endl;
}

int main (int argc, char * const argv[]) 
{
	if ( argc != 2 ) return -1;

	FILE * f = fopen(argv[1], "r");
	fscanf(f, "%d", &numCases);

	for ( int caseIndex = 0; caseIndex < numCases; caseIndex++ )
	{
		cout << "Case #" << caseIndex + 1 << ": ";

		fscanf(f, "%d", &C);
		for (int i = 0; i < C; i++)
		{
			fscanf(f, " %s", combine[i]);
		}

		fscanf(f, " %d", &D);
		for (int i = 0; i < D; i++)
		{
			fscanf(f, " %s", oppose[i]);
		}

		fscanf(f, " %d", &N);
		fscanf(f, " %s", seq);
		
//		printf("C = %d\n", C);
//		for (int i = 0; i < C; i++)
//		{
//			printf("C[%d] = %c%c%c\n", i, combine[i][0], combine[i][1], combine[i][2]);
//		}
//
//		printf("D = %d\n", D);
//		for (int i = 0; i < D; i++)
//		{
//			printf("D[%d] = %c%c\n", i, oppose[i][0], oppose[i][1]);
//		}
//		
//		printf("N = ");
//		for (int i = 0; i < N; i++)
//		{
//			printf("%c", seq[i]);
//		}
//		printf("\n");
		
		
		resIndex = 0;
		if (N > 0)
		{
			result[resIndex] = seq[0];
			resIndex++;
		}
//		printResult();

		for (int i = 1; i < N; i++)
		{
			char curChar = seq[i];
			char prevChar = result[resIndex - 1];
			//Combine?
			char combineChar = combiner(prevChar, curChar);
			if (combineChar != 0)
			{
				result[resIndex - 1] = combineChar;
			} else
			{
				if (opposer(curChar))
				{
					resIndex = 0;
				} else
				{
					result[resIndex++] = curChar;
				}
			}
			
//			printResult();
		}
		
		printResult();
	}

	fclose(f);
	return 0;
}
