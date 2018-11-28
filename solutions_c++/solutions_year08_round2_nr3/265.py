// B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


int _tmain(int argc, _TCHAR* argv[])
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	int N;
	scanf("%i\n",&N);

	for(int z=0; z<N; z++)
	{
		long long K;
		scanf("%lli\n",&K);
		long long nn;
		scanf("%lli ",&nn);
		long long *posi = new long long [nn];
		for(int i=0; i<nn; i++)
			scanf("%lli",&posi[i]);
		scanf("\n");
		long long *deck = new long long [K];
		for (int i=0; i<K; i++)
			deck[i]=0;
		long long pos=-1;
		for (int i=1; i<=K; i++)
		{
			for (int j=1; j<=i; j++)
			{
				pos++;
				if(deck[pos]>0)
					j=j-1;
				if (pos>=K)
					pos=0;
			}
			deck[pos]=i;
			//printf("%lli %lli\n", pos, deck[pos]);
		}
		printf("Case #%i: ",z+1);
		for (int i=0; i<nn; i++)
			printf("%lli ",deck[posi[i]-1]);
		printf("\n");
		delete [] posi;
		delete [] deck;
	}
	return 0;
}

