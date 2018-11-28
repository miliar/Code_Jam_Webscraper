#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <vector>
using namespace std;
typedef long long ll;

 
int N;
int h[2020];
int x[2020];


bool possible(int a, int b) {
	if(a==b) return true;
	if(x[a]>b) return false;
	return possible(a+1, x[a]) and possible(x[a], b);
}
void rec(int a, int m) {
	if(h[a]!=-1) return; //hoehe schon gesetzt
	int b = x[a];
	rec(b, m);//rechts gehts weiter -> hoehe b bestimmt
	h[a] = h[b] - (b-a)*m;
	rec(a+1, m+1);
}
int main() {
	//freopen("C.in", "r", stdin);
	int T;
	scanf("%d\n", &T);
	for(int t=1; t<=T; t++) {
		scanf("%d", &N);
		for(int i=1; i<=N-1; i++) {
			scanf("%d", &x[i]);
			h[i] = -1;
		}
		h[N] = 999999999;
		printf("Case #%d:", t);
		if(possible(1, N)) {
			rec(1, 0);
			for(int i=1; i<=N; i++)
				printf(" %d", h[i]);
		} else {
			printf(" Impossible");
		}
		printf("\n");
		
		
	}
}
