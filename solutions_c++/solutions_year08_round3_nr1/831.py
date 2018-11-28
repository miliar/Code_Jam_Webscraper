//MaximZh
//C1C_A.cpp

#include <stdio.h> //Standard C++ library

int main()
{
	int N = 0;
	int freq[1000];
	
	FILE *pfin = fopen("data.in", "rt");
	FILE *pfout = fopen("data.out", "wt");
	fscanf(pfin, "%d\n", &N);
	for( int i = 0; i < N; i++ )
	{
		int P = 0;
		int K = 0;
		int L = 0;
		fscanf(pfin, "%d %d %d\n", &P, &K, &L);
		for( int j = 0; j < L; j++ )
			fscanf(pfin, "%d", freq+j);
		if( K*P >= L )
		{
			int M = L-1;
			bool flag;
			do{
				flag = false;
				for( int j = 0; j < M; j++ )
					if( freq[j]<freq[j+1] )
					{
						int tmp = freq[j];
						freq[j] = freq[j+1];
						freq[j+1] = tmp;
						flag = true;
					}
				M--;
			}while( flag );

			int Count = 0;
			int factor = 1;
			int k = 0;
			for( int j = 0; j < L; j++ )
			{
				Count += freq[j]*factor;
				if( ++k >= K )
				{
					k = 0;
					factor++;
				}
			}
			fprintf(pfout, "Case #%d: %d\n", i+1, Count);
		}
		else
			fprintf(pfout, "Case #%d: Impossible\n", i+1);		
	}
	fclose(pfout);
	fclose(pfin);
	return 0;
}