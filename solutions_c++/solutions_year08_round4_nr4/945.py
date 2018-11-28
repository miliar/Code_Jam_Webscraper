#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

int size(char * word, int * perm, int k)
{
	char * permuted = new char[1024];
	strcpy(permuted, word);
	int len = strlen(word);
	int iter = len / k;
	for(int i = 0; i < iter; ++i)
	{
		for(int j = 0; j < k; ++j)
		{
			permuted[i * k + j] = word[i * k + perm[j]];
		}
	}
	int g = 1;
	char prev = permuted[0];
	for(int i = 1; i < len; ++i)
	{
		if(permuted[i] != prev)
		{
			++g;
			prev = permuted[i];
		}
	}
	delete[] permuted;
	return g;
}

int main()
{
	int n;
	scanf(" %d", &n);
	for(int i = 1; i <= n; ++i)
	{
		int k;
		scanf(" %d", &k);
		int * A = new int[k];
		for(int j = 0; j < k; ++j)
		{
			A[j] = j;
		}
		char * S = new char[1024];
		scanf("%s", S);
		int max = 1000000000;
		do
		{
			int c = size(S, A, k);
			if(c < max)
			{
				max = c;
			}
		} while(next_permutation(A, A + k));
		delete[] S;
		printf("Case #%d: %d\n", i, max);
	}
	return 0;
}
