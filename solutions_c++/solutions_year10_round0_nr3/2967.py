#include <stdio.h>
#include <iostream>

using namespace std;
int main()
{
	int R, K, N, T;
	scanf("%d", &T);
	for(int i=0;i<T;i++)
	{
		scanf("%d %d %d", &R, &K, &N);
		int* A = new int[N];
		int* Score = new int[N];
		int* Next = new int[N];
		int nTotal = 0;
		
		for(int j=0;j<N;j++)
		{
			cin >> A[j];
			nTotal += A[j];
		}
		
		if (nTotal <= K)
		{
			printf("Case #%d: %u\n", i+1, nTotal * R);
			continue;
		}
		
		for(int j=0;j<N;j++)
		{
			Score[j] = 0;
			int k = j;
			
			while(Score[j] + A[k] <= K)
			{
				Score[j] += A[k];
				k = (k+1) % N;
			}
			Next[j] = k;
		}
		
		unsigned answer = 0;
		int p = 0;
		for(int j=0;j<R;j++)
		{
			answer += Score[p];
			p = Next[p];
		}
		
		printf("Case #%d: %u\n", i+1, answer);
		delete[] A;
		delete[] Score;
		delete[] Next;
	}
}
