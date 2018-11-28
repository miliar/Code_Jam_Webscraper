#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
	int i, j;
	int n, N;
	int k;
	int res;
	char S[1001];
	char TEMP[1001];
	int idx[10];
	scanf("%d", &N);


	for(n=1;n<=N;n++)
	{
		int min;

		scanf("%d", &k);
		scanf("%s", S);
		for (i = 0; i < k; i++) {
			idx[i] = i;
		}
		min = 1000000000;
		do {
			int len = strlen(S);
			int cnt = 1;
			char before;
			for(i=0;i<len/k;i++)
			{
				for(j=0;j<k;j++)
				{
					TEMP[k*i+j] = S[k*i+idx[j]];
				}
			}
			before = TEMP[0];
			for(i=1;i<len;i++)
			{
				if( before!=TEMP[i] )
					cnt++;
				before = TEMP[i];
			}
			if( min > cnt )
				min = cnt;
		}while (next_permutation(idx, idx+k));
		printf("Case #%d: %d\n", n, min);
	}
	return 0;
}
