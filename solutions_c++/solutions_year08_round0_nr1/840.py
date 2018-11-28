#include <stdio.h>
#include <string>
#include <map>
#include <iostream>
#include <string.h>
using namespace std;

int N, S, Q;
int A[200];

int main() {
	scanf("%d", &N);
	for (int case_x = 1; case_x <= N; case_x++) {
		map<string, int> M;
		string str; int lnum, num;
		char buf[10000];
		M.clear();
		scanf("%d\n", &S);
		for (int i = 0; i < S; i++) {
			gets(buf); str = buf;
			M[str] = i;
		}
		scanf("%d\n", &Q);
		memset(A, 0, sizeof(A)); lnum = -1;
		for (int i = 0; i < Q; i++) {
			gets(buf); str = buf;
			num = M[str];
			if (lnum < 0) { lnum = num; continue; }
			int min = Q + 1;
			for (int j = 0; j < S; j++) {
				if (j == lnum) continue;
				if (A[j] < min) min = A[j];
			}
			A[lnum] = min + 1;
			lnum = num;
		}
		int min = Q + 1;
		for (int i = 0; i < S; i++) {
			if (lnum == i) continue;
			if (A[i] < min) min = A[i];
		}
		printf("Case #%d: %d\n", case_x, min);
	}
	return 0;
}
