#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int A, B, P;
int N[1001], grupa[1001], used[1001];

void solve(int case_number) {
	int i,j,k;
	for(i=A; i<=B; i++) {
		N[i] = i;
		grupa[i] = i;
		used[i] = 1;
	}
	for(i=2; i<P; i++) {
		for(j=A; j<=B; j++) {
			while(N[j] % i == 0) {
				N[j] /= i;
			}
		}
	}
/*
	printf("Numere ramase: ");
	for(i=A; i<=B; i++) {
		printf("%d ",N[i]);
	}
	printf("\n");*/

	int first_ok, replace;
	for(i=P; i<=B; i++) {
		first_ok = 0;
		for(j=A; j<=B; j++) {
			if(N[j] % i == 0) {
				if(first_ok != 0 && grupa[j] != grupa[first_ok]) {
					replace = grupa[j];
					for(k=A; k<=B; k++) {
						if(grupa[k] == replace) {
							grupa[k] = grupa[first_ok];
						}
					}
					used[replace] = 0;
				} else {
					first_ok = j;
				}
			}
		}
	}
	int count = 0;
	for(i=A; i<=B; i++) {
		if(used[i]) {
			count ++;
		}
	}
	
	printf("Case #%d: %d\n", case_number, count);
}

int main(void) {
	freopen("B-small-attempt0.in", "rt", stdin);
	freopen("B.out", "wt", stdout);

	int i, T;
	scanf("%d",&T);
	for(i=1; i<=T; i++) {
		scanf("%d %d %d\n",&A, &B, &P);
		solve(i);
	}

	return 0;
}