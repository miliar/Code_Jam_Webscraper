// Google CodeJAM 2011
// Author: Syed Ghulam Akbar

#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <iostream>

using namespace std;
char Tile[60][60];
long Freq[10000];

int main() {
	FILE *in = freopen( "Debug\\input.txt", "r", stdin );
	FILE *out = freopen( "Debug\\output.txt", "w", stdout );

	int C;
	scanf("%d",&C);

	for (int test=1;test<=C;test++) {
		long N=0, Low=0, High=0;

		cin >> N >> Low >> High;

		// Read frequencies
		for (int i=0; i<N; i++)
			cin >> Freq[i];

		long result = -1;
		bool found = false;

		// Check if in range
		for (long i=Low; i<=High && found == false; i++)
		{
			long match=0;
			result = -1;

			for (long j=0; j<N ; j++)
			{
				if (i == 0 || Freq[j] == 0) continue;
				if ((Freq[j] % i == 0 || i % Freq[j] == 0))
				{
					result = i;
					match++;
				}

			}

			if (match == N)
				found = true;
		}

		if (found == false)
			printf("Case #%d: NO\n", test);
		else
			printf("Case #%d: %d\n", test, result);
	}
}