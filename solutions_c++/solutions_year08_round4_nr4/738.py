#include "iostream"
#include <stdlib.h>
#include <math.h>
#include <vector>

#define MAX 100000

using namespace std;

string S;
int k;
int Min;

void rek(int *data,int d,int* q)
{
	if (d == k)
	{
		int r = 0;
		for (int i = 0; i < S.length()-1; i++)
		{
			//printf("%c\n",S[(i/k)*k+data[i%k]]);
			if (S[(i/k)*k+q[i%k]] != S[((i+1)/k)*k+q[(i+1)%k]])
			{
				r++;
			}
		}
		//printf("\n");
		r++;
		if (r < Min)
			Min  = r;
	}
	else
	{
		for (int i = 0; i < k; i++)
			if (data[i] == 0)
			{
				data[i] = 1;
				q[d] = i;
				rek(data, d+1,q);
				data[i] = 0;
			}
	}
}
int main()
{
	int N;
	scanf("%d\n",&N);
	for (int c = 0; c < N; c++)
	{
		Min = 5000000;
		scanf("%d\n",&k);
		char str[50000];
		scanf("%s\n",str);
		S = str;
		int* data = new int[k];
		for (int i = 0; i < k; i++)
			data[i] = 0;
		int* q = new int[k];
		rek(data,0,q);
		printf("Case #%d: %d\n",c+1,Min);
	}
	return 0;
}
