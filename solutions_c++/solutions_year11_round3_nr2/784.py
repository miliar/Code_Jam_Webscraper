#include <fstream>
#include <vector>
#include <math.h>

#include <stdio.h>
#include <stdlib.h>

using namespace std;

int compare (const void * a, const void * b)
{
  return -( *(int*)a - *(int*)b );
}

int main() {

	int T, N, C, L;
	long long t;

	int a[1000]; 
	int n[1000];

	fstream f, g;

	f.open("spemergency.in", fstream::in);
	g.open("spemergency.out", fstream::out);
	
	f >> T;
	for (int test = 1; test <= T; test++) {
		memset(a, 0, sizeof( a));	
		memset(n, 0, sizeof( n));

		f >> L >> t >> N >> C;
		for (int i = 0; i < C; i++) {
			f >> a[i];
		}
		
		long step = 0;
		while (step < N) {
			n[step] = a[step % C];
			step++;
		}
		
		step = 0;
		long long sum = 0;

		if (L == 0) {
			while (step < N) {
				sum += 2 * (long long ) n[step];
				step++;
			}
			g << "Case #" << test << ": " << sum << endl;
			continue;
		}

		if (t == 0) {
			qsort (n, N , sizeof(int ), compare);
			long remaining = 0;
			while (remaining < L && step < N) {
				sum += (long long ) n[step++];
				remaining++;
			}

			while (step < N) {
				sum += 2 * (long long ) n[step++];
			}

			g << "Case #" << test << ": " << sum << endl;  
			continue;
		}

		while ((sum < t) && (step < N)) {
			sum += 2 * (long long ) n[step];
			step++;
		}
		if (sum >= t) {
			step--;
			n[step] = (sum - t) / 2;
			sum = (long long ) t;
			for (int i = 0; i < step; i++) {
				n[i] = -1;
			}
			qsort (n, N , sizeof(int ), compare);
			N -= step;
			step = 0;
			long remaining = 0;
			while (remaining < L && step < N) {
				sum += (long long ) n[step++];
				remaining++;
			}

			while (step < N) {
				sum += 2 * (long long ) n[step++];
			}

			g << "Case #" << test << ": " << sum << endl;  
		} else {
			if (step == N) {
				g << "Case #" << test << ": " << sum << endl;
			}
		}
	}

	f.close();
	g.close();
	return 0;
}
	