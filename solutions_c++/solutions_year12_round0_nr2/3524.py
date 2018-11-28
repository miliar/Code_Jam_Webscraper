#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <vector>

int Emax[] = {
	0,
	1, 1, 1,
	2, 2, 2,
	3, 3, 3,
	4, 4, 4,
	5, 5, 5,
	6, 6, 6,
	7, 7, 7,
	8, 8, 8,
	9, 9, 9,
	10, 10, 10
};

int Smax[] = {
	0, 0,
	2, 2, 2,
	3, 3, 3,
	4, 4, 4,
	5, 5, 5,
	6, 6, 6,
	7, 7, 7,
	8, 8, 8,
	9, 9, 9,
	10, 10, 10,
	0, 0
};

/* resulting list should be sorted 1, 0, 30, 29, 28, 27, ..., 2*/
bool sortfunc (int first,int second) {
	/* return true if first goes before second */
	bool result = false;
	
	/* special case: first or second is 1 or 0 */
	if (first <= 1 || second <= 1) {
		result = (first < second);
		///* if both are 1 or 0, put the one which is 1 first */		if (first <= 1 && second <= 1) {
		//	result = (first > second);
		//}
		///* put the smaller digit first */
		//else
		//{
		//	result = (first < second);
		//}
	}

	/* general case */
	else {
		result = (first > second);
	}

	return result;
}
	

int main(int argc, char* argv[])
{
	FILE* fp = 0;
	char* buf = 0;
	char* search = " ";
	char* token = 0;
	size_t buflen = 1024*1024;

	int T = 0;  /* test cases */
	int Ti = 0; /* test cases index */

	int N = 0;  /* number of googlers */
	int Ni = 0; /* number of googlers index */

	int S = 0;  /* number of surprise triplets */
	int Si = 0; /* number of surprise triplets index */

	int P = 0;  /* target result */

	int p = 0;  /* number of googlers with at least P points */
	int s = 0;  /* number of surprise triplets remaining */
	int e = 0;  /* number of expected triplets remaining */

	int t[1000] = {0};  /* googlers point totals */
	int ti = 0; /* googlers point totals index */
	int ev = 0; /* googlers expected point total */
	int sv = 0; /* googlers surprise point total */

	buf = (char*) malloc(buflen);
	fp = freopen("C:/Developer/GoogleCodeJam/DancingWithGooglers/Input.txt", "r", stdin);
	/* fp = fopen("C:/Developer/GoogleCodeJam/DancingWithGooglers/Input.txt", "r"); */

	/* read number of test cases */
	if (0 == fgets(buf, buflen, fp))
		return 0;
	T = atoi(buf);

	/* process all test cases */
	for (Ti = 0; Ti < T; ++Ti) {
		if (0 == fgets(buf, buflen, fp))
			return 0;

		/* get first token; the number of googlers */
		token = strtok(buf, search);
		N = atoi(token);

		/* get next token; the number of surprise cases */
		token = strtok(0, search);
		S = atoi(token);

		/* get next token; the target result */
		token = strtok(0, search);
		P = atoi(token);

		/* for all googlers */
		for (ti = 0; ti < N; ++ti) {
			/* get next token; the googlers point total */
			token = strtok(0, search);
			t[ti] = atoi(token);
		}

		/* set test variables */
		p = 0;
		s = S;
		e = N - S;

		/* create vector of point totals */
		std::vector<int> tv(t, t+N);

		/* sort vector of point totals */
		sort (tv.begin(), tv.end(), sortfunc);

		/* for all googlers */
		for (ti = 0; ti < N; ++ti) {
			ev = Emax[tv[ti]];
			sv = Smax[tv[ti]];

			if (e > 0 && ev >= P) {
				++p;
				--e;
			}
			else if (s > 0 && sv >= P) {
				++p;
				--s;
			}
		} /* for all googlers */

		/* print result */
		printf("Case #%d: %d\n", Ti+1, p);
		fflush(stdout);

	} /* for all test cases */

	free(buf);
	return 0;
}