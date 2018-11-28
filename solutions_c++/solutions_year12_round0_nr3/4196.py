#include <vector>
#include <stdlib.h>
#include <string>
#include <iostream>
#include <stdio.h>
#include <tchar.h>
#include <map>
#include <math.h>
using namespace std;

#define BOOL int
#define TRUE 1
#define FALSE 0
int readi() { int a; scanf( "%d", &a ); return a; }
char sbuf[100005]; string readstr(){ scanf( "%s", sbuf ); return sbuf; }

int DIGLEN = 0;
int DIGMIN = 0;
int MYPOW[10] = {0};
int MAX = 1000;
map<int, vector<int>> pairDB;
int GetDigits(int V)
{
	DIGMIN = 100000000;if (V / DIGMIN != 0) return 9;
	DIGMIN = 10000000;if (V / DIGMIN != 0) return 8;
	DIGMIN = 1000000;if (V / DIGMIN != 0) return 7;
	DIGMIN = 100000;if (V / DIGMIN != 0) return 6;
	DIGMIN = 10000;if (V / DIGMIN != 0) return 5;
	DIGMIN = 1000;if (V / DIGMIN != 0) return 4;
	DIGMIN = 100;if (V / DIGMIN != 0) return 3;
	DIGMIN = 10;if (V / DIGMIN != 0) return 2;
	DIGMIN = 1;if (V / DIGMIN != 0) return 1;
}

int Move(int V, int digits)
{
	int base = MYPOW[digits];
	int a = V / base;
	int b = V % base;

	int X = b * MYPOW[DIGLEN-digits] + a;

	if (X < DIGMIN)
		return -1;	
	
	return X;
}

void Prepare()
{
	pairDB.clear();
	int i, j, k, min, max;
	for (i = 1; i <= MAX; ++i)
	{
		DIGLEN = GetDigits(i);

		for (j = 1; j <= DIGLEN - 1; ++j)
		{
			k = Move(i, j);
			if (i == k || k == -1) continue;
            
            if (pairDB.count(i) == 0)
			{
				vector<int> temp;
				temp.push_back(k);
				pairDB[i] = temp;
			}
			else
			{
				pairDB[i].push_back(k);
			}
		}
	}
}

// this is a brute-force version to verify the dp-version.

int Solve(int A, int B)
{
	map<string, int> result;
	char buffer[256];
	int i,j,k;
	vector<int>::iterator it;

	for (i = A; i <= B; ++i)
	{
		if (pairDB.count(i) > 0)
		{
			vector<int> x = pairDB[i];
			for(it = x.begin(); it != x.end(); ++it)
			{
			    j = *it;

				if ( j < A || j > B) continue;

				if (i == j)
				{
					printf("\nerror!");
					continue;
				}
				else if (i < j)
				{
					sprintf(buffer, "%d, %d", i, j );
				}
				else
				{
					sprintf(buffer, "%d, %d", j, i );
				}

				result[buffer] = 1;
			}
		}
	}

	return result.size();
}


 BOOL DEBUGIN = FALSE;
 BOOL DEBUGOUT = FALSE;
int main(int argc, char* argv[])
{
	// use for to save coding.
	MYPOW[0] = 1;
	MYPOW[1] = 10;
	MYPOW[2] = 100;
	MYPOW[3] = 1000;
	MYPOW[4] = 10000;
	MYPOW[5] = 100000;
	MYPOW[6] = 1000000;
	MYPOW[7] = 10000000;
	MYPOW[8] = 100000000;
	MYPOW[9] = 1000000000;

	int N = 0, A, B, Result;
	if (!DEBUGIN) freopen("C-small-attempt0.in","rt",stdin);
	if (!DEBUGOUT) freopen("C-small-attempt0.out","wt",stdout);

	Prepare();
	N = readi(); 
	for (int i = 0; i < N; i++)
	{
		A = readi(); B = readi();

		Result = Solve(A, B);
		printf("Case #%d: %d", i + 1, Result, Result);
		printf("\n");
	}

	//int a = 12345678;
	//DIGLEN=GetDigits(a);
 //   printf("%d\n", Move (a, 1));
 //   printf("%d\n", Move (a, 2));
 //   printf("%d\n", Move (a, 3));
 //   printf("%d\n", Move (a, 4));
 //   printf("%d\n", Move (a, 5));
 //   printf("%d\n", Move (a, 6));
 //   printf("%d\n", Move (a, 7));
 //   printf("%d\n", Move (a, 8));

	//a = 12345608;
	//DIGLEN=GetDigits(a);
 //   printf("%d\n", Move (a, 1));
 //   printf("%d\n", Move (a, 2));
 //   printf("%d\n", Move (a, 3));
 //   printf("%d\n", Move (a, 4));
 //   printf("%d\n", Move (a, 5));
 //   printf("%d\n", Move (a, 6));
 //   printf("%d\n", Move (a, 7));
 //   printf("%d\n", Move (a, 8));

	getchar();
	return 0;
}
