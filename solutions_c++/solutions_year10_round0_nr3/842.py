#define __USE_MINGW_ANSI_STDIO  1

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace std;

int main()
{
	int  T;
	int  R, k, N;
	int  g_i[1000];
	long long  acc_i[2000];
	
	cin >> T;

	for (int ncase=1; ncase <= T; ncase++)
	{
		// Input Data
		cin >> R >> k >> N;

		for (int i=0; i<N; i++)
			cin >> g_i[i];

		// Verify Input
		/*
		printf("%d %d %d\n", R, k, N);
		for (int i=0; i<N; i++)
			printf("%d ", g_i[i]);
		printf("\n");
		*/
		
		// Build Accumulate Array
		acc_i[0] = g_i[0];
		for (int i=1; i<N; i++) {
			acc_i[i] = acc_i[i-1]+g_i[i];
		}
		for (int i=0; i<N; i++) {
			acc_i[i+N] = acc_i[i+N-1]+g_i[i];
		}
		
		long long money = 0;
		int first_group = 0;
		
		if ( acc_i[N-1] <= k )
			money = R * acc_i[N-1];
		else
		for (int r=0; r<R; r++)
		{
			// input: acc_i, N, first_group, k
			// output: last_group, ride_person
			
			// last_group is in first_group ~ first_group+N-1
			// maximum ride_person <= k
			// ride_person = acc_i[last_group] - acc_i[first_group-1]
			if ( first_group == 0 )
				first_group = N;
			int  end_line_group = first_group+N-1;
			long long  acc_for_maxride = acc_i[first_group-1] + k;
			
			// look up maximum x such that acc_i[x] <= acc_for_maxride
			int  low = first_group;
			int  high = end_line_group;
			while ( low < high )
			{
				int  mid = high - (high - low)/2;
				if ( acc_i[mid] > acc_for_maxride )
					high = mid - 1;
				else
					low = mid;
			}
			
			int last_group = low;
			long long ride_person = acc_i[last_group] - acc_i[first_group-1];
			
			first_group = (last_group + 1)%N;
			
			// make money, 1 euro per person
			money += ride_person;
		}
		
		// Output Result
		printf("Case #%d: ", ncase);
		printf("%lld", money);
		
		printf("\n");
	}
}
