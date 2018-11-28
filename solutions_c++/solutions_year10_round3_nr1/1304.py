#include <iostream>
#include <algorithm>
#include "stdio.h"
using namespace std;

//#define DBGOUT printf
void DBGOUT(...) { } 

int A[2000];
int B[2000];
int N;


int findSolution()
{
	int count = 0;
	int i,j;
	int li, hi, lj, hj;

	for (i = 0; i < N; i++)
	{
		for (j = 0 ;j < N; j++)
		{
			if (i == j )
				continue;
/*
			if (A[i] > A[j] && A[j] > B[i] && B[i] > B[j] ||
				A[j] > A[i] && A[i] > B[j] && B[j] > B[i] ||
				B[i] > A[j] && A[j] > A[i] && A[i] > B[j] ||
				B[j] > B[i] && B[i] > A[j] && A[j] > A[i])
*/
			if (A[i] < A[j] && B[i] < B[j] || A[i] > A[j] && B[i] > B[j])
			{ 
			}
			else
			{
				count++;
				DBGOUT("intersected\n");
			}
		}
	}
	return count / 2;
}


int main()
{
	int case_cnt;
	int ret = 0;

	scanf("%d", &case_cnt);

	for (int i = 0; i < case_cnt; i++)
	{
		scanf("%d", &N);

		for (int j = 0; j < N; j++)
		{		
			scanf("%d %d", &A[j], &B[j]);
		}

		ret = findSolution();

		cout << "Case #" << i + 1 << ": " << ret << endl;
	}
}

