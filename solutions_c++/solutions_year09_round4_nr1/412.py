#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

int N, nTC;
char M[50][50];
int ar[50];

int main() {
	int tc = 1;
	scanf ("%d", &nTC);
	
	while (nTC--) {
		scanf ("%d", &N);
		
		for (int i = 0; i < N; i++) {
			ar[i] = 0;
			scanf ("%s", M[i]);
			for (int j = N - 1; j >= 0; j--) {
				if (M[i][j] == '1') {
					ar[i] = j;
					break;
				}
			}
		}
		/*
		for (int i = 0; i < N; i++)
			printf ("%d\n", ar[i]);
		puts ("");*/
		
		int ctr = 0;
		
		for (int i = 0; i < N; i++) {
			while (i < N && ar[i] <= i) {
				i++;
			}
			
			if (i == N) break;
			
			int j;
			for (j = i + 1; j < N; j++) {
				if (ar[j] <= i)
					break;
			}
			
			for (; j > i; j--) {
				if (ar[j] < ar[j - 1]) {
					ctr++;
					swap (ar[j], ar[j - 1]);
				}
			}
		}
		/*
		for (int i = 0; i < N; i++)
			printf ("%d\n", ar[i]);
		puts ("");*/
		
		printf ("Case #%d: %d\n", tc++, ctr);
	}
	
	return 0;
}
