#include <stdio.h>
#include <iostream>
#include <string.h>
#include <stdlib.h>

using namespace std;

const char input[] = "input.in";
const char output[] = "output.out";

int A[60][60];

int main()
{
	freopen(input, "r", stdin);
	freopen(output, "w", stdout);
	
	int t;
	scanf("%d", &t);
	
	int test;
	for(test = 1; test <= t; ++test)
	{
		int n;
		scanf("%d", &n);
		
		int i, j;
		char sir[100];
		int poz[100];
		for(i = 1; i <= n; ++i)
		{
				scanf("%s", &sir);
				poz[i] = 1;
				for(j = 1; j <= n; ++j)
				{
					A[i][j] = sir[j-1] - '0';
					if(A[i][j]) poz[i] = j;
				}
		}
		
		int nrmin = 0;
		for(i = 1; i <= n; ++i)
			if(poz[i] > i)
			{
				int j;
				for(j = i+1; j <= n && poz[j] > i; ++j) ;
				nrmin += j-i;
				int aux = poz[j];
				for(; j > i; --j)
					poz[j] = poz[j-1];
				poz[j] = aux;
			}
		printf("Case #%d: %d\n", test, nrmin);
	}
	return 0;
}