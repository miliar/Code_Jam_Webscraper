#include <cstdio>
#include <iostream>

using namespace std;

int move(int X, int size)
{
	return X / 10 + (X % 10) * size;
}

int main()
{
	int N;
	
	scanf("%d\n", &N);
	for(int i = 0; i < N; i++)
	{
		int A, B;
		scanf("%d %d\n", &A, &B);
		
		int temp = A, length = 0, size = 1;
		while(temp)
			temp /= 10, length++, size *= 10;
		size /= 10;
		
		bool *table = new bool[B - A + 1];
		for(int C = 0; C <= B - A; C++)
			table[C] = 0;
		
		int score = 0;
		for(int C = A; C <= B; C++)
		{
			if(table[C - A])
				continue;
			int k = 0;
			for(int D = C, j = 0; j <= length; j++, D = move(D, size))
			{
				if(D < A || D > B)
					continue;
				else if(!table[D - A])
					table[D - A] = 1, k++;
			}
			score += k * (k - 1) / 2;
		}
		delete[] table;
		
		printf("Case #%d: %d\n", i + 1, score);
	}
	
	return 0;
}
