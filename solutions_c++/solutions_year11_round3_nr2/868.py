// gcj2010.cpp : Defines the entry point for the console application.
//

#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <math.h>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char* argv[])
{
	// Read input
	FILE* f = fopen("B-small-attempt0.in", "r");
	FILE* fOut = fopen("output.txt", "w");

	int i, j;

	unsigned int nCases, N;

	fscanf(f, "%i", &nCases);
	for (unsigned int iCase = 0; iCase < nCases; iCase++) {
		printf("Processing case #%i\n", iCase + 1);

		int L, t, N, C;
		int a[1000];
		int dist[1000];

		fscanf(f, "%i %i %i %i", &L, &t, &N, &C);
		for (int i = 0; i < C; i++)
			fscanf(f, "%i", &a[i]);

		int k = 0;
		for (int i = 0; i < N; i++) {
			dist[i] = a[k];
			k = (k + 1) % C;
		}

		// First star that booster should be built
		int ttotal = 0;

		int d = 0;
		vector<int> xxx;
		int first = 0;
		for (int i = 0; i < N; i++) {
			d = d + dist[i];
			int tt = d * 2;
			if (tt >= t) {
				// i = First star that booster should be built
				// 
				ttotal += (t);
				xxx.push_back((tt - t));
				first = i + 1;
				break;
			}
		}

/*		
		for (int i = 0; i < first - 1; i++)
			ttotal = ttotal + (dist[i] * 2);
*/

		for (int i = first; i < N; i++)
			xxx.push_back(dist[i] * 2);

		sort(xxx.begin(), xxx.end());
		
		int l = L;
		for (vector<int>::reverse_iterator i = xxx.rbegin(); i != xxx.rend(); i++) {
			int time = *i;
			if (l > 0) {
				l-- ;
				
				ttotal += time / 2;
			}
			else {
				ttotal += time;
			}

		}
			
		fprintf(fOut, "Case #%i: %i\n", iCase + 1, ttotal);
		fflush(fOut);
	}

	fclose(f);
	fclose(fOut);

	return 0;
}

