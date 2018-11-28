#include <cstdio>
#include <cstdlib>

using namespace std;

const int SMALL = -(1 << 30);

int main(int argc, char *argv[])
{
	int N, T, S, p;
	scanf("%d\n", &T);
	for (int t = 0; t < T; t++) {
		scanf("%d %d %d", &N, &S, &p);
		int* A = new int[N];
		int count = 0, s = S;
		for (int n = 0; n < N; n++) {
			scanf("%d", &A[n]);
			int nonSurprisingMaxScore = SMALL;
			int rem = A[n] % 3;
			if ((rem  == 0) && (A[n] >= 0))
				nonSurprisingMaxScore = A[n]/3;
			else if ((rem == 1) && (A[n] >= 1))
				nonSurprisingMaxScore = (A[n]+2)/3;
			else if ((rem == 2) && (A[n] >= 2))
				nonSurprisingMaxScore = (A[n]+1)/3;
			else {}

			if (nonSurprisingMaxScore >= p) count++;

			int surprisingMaxScore = SMALL;
			int rem2 = A[n] % 3;
			if ((rem2 == 0) && (A[n] >= 3))
				surprisingMaxScore = (A[n]+3)/3;
			else if ((rem2 == 1) && (A[n] >= 4))
				surprisingMaxScore = (A[n]+2)/3;
			else if ((rem2 == 2) && (A[n] >= 2))
				surprisingMaxScore = (A[n]+4)/3;
			else {}

			//printf("A[%d]:%d nonSurprisingMaxScore:%d surprisingMaxScore:%d p:%d s:%d\n", n, A[n], nonSurprisingMaxScore, surprisingMaxScore, p, s);

			if ((nonSurprisingMaxScore < p) && (s > 0) && (surprisingMaxScore >= p)) {
				count++;
				s--;
			}
			// printf("count: %d\n", count);
		}
		printf("Case #%d: %d\n", t+1, count); 
		delete [] A;
	}



	return 0;
}
