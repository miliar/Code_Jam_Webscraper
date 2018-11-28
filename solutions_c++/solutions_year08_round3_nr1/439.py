/*
 * =====================================================================================
 *
 *       Filename:  textmessage.cpp
 *
 *    Description:  gcj 08 round C-1
 *
 *        Version:  1.0
 *        Created:  2008-7-27 17:10:49
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  unicode1985 (xumx), starstarstarpku@gmail.com
 *        Company:  PKU
 *
 * =====================================================================================
 */

#include <iostream>
#include <cstdio>
using namespace std;

int comp(const void* e1, const void* e2) {
	return *((int*)e2) - *((int*)e1);
}

int foo () {
	// TODO
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int N;
	int P, K, L;
	int freqtbl[1001];
	scanf("%d\n", &N);
	for (int x=1; x<=N; ++x) {
		long long sum=0;
		scanf("%d %d %d\n", &P, &K, &L);
		if (P*K < L) {
			printf ("Case #%d: Impossible\n", x);
			continue;
		}
		for (int i=0; i<L; ++i) {
			scanf("%d", &freqtbl[i]);
		}
		qsort(freqtbl, L, sizeof(int), comp);
		for (int j=0; j<P; ++j) {
			long long temp = 0;
			for (int t=j*K; t<(j+1)*K && t<L; ++t) {
				temp += freqtbl[t];
			}
			//printf ("%d %d\n", temp, sum);
			sum += temp*(j+1);
		}
		printf ("Case #%d: %I64d\n", x, sum);
	}
	return 0;
}

int main (int argc, char *argv[])
{
	// TODO
	
	foo();
	return 0;
}


