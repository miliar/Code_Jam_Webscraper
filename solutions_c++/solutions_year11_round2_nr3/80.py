#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <math.h>
using namespace std;

int T;
bool conn[8][8];
int ar[8];
int N, M;
int bestb;
int be[8];
bool geht;
bool fg[8];

void suche(int i) {
	if (i == N) {
		geht = true;
		for (int k = 0; k < N; k++)
			be[k] = ar[k];
		return;
	}
	for (ar[i] = 0; ar[i] < bestb; ar[i]++) {
		for (int k = i-1; k >= 0; k--) {
			if (conn[k][i]) {
				for (int f = 0; f < bestb; f++)
					fg[f] = false;
				for (int j = k; j < i; ) {
					fg[ar[j]] = true;
					int las = j+1;
					for (int s = j+2; s <= i; s++)
						if (conn[j][s] && (s != i || j != k))
							las = s;
					j = las;
				}
				fg[ar[i]] = true;
				for (int f = 0; f < bestb; f++)
					if (!fg[f])
						goto weiter;
			}
		}
		suche(i+1);
		weiter: ;
	}
}

int main() {
	scanf("%d", &T);
	for (int test = 0; test < T; test++) {
		fprintf(stderr, "Test %d/%d\n", test+1, T);
		printf("Case #%d: ", test+1);
		scanf("%d %d", &N, &M);
		vector<int> A;
		vector<int> B;
		for (int i = 0; i < N; i++)
			for (int k = 0; k < N; k++)
				conn[i][k] = false;
		for (int i = 0; i < M; i++) {
			int a;
			scanf("%d", &a);
			A.push_back(a-1);
		}
		for (int i = 0; i < M; i++) {
			int a;
			scanf("%d", &a);
			B.push_back(a-1);
			conn[A[i]][B[i]] = true;
		}
		conn[0][N-1] = true;
		for (bestb = 1; ; bestb++) {
			geht = false;
			suche(0);
			if (!geht)
				break;
		}
		printf("%d\n", bestb-1);
		for (int i = 0; i < N; i++) {
			if (i)
				printf(" ");
			printf("%d", be[i]+1);
		}
		printf("\n");
	}
	return 0;
}
