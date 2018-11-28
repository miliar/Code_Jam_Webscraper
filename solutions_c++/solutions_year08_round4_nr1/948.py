#include <cstdio>
#define AND 1
#define OR  0
#define MY_INT_MAX 10000000

int min(int a, int b, int c) {
    int min = a;
    if (b < min)    min = b;
    if (c < min)    min = c;
    return min;
}
int f[10001][2];
void g(int node[], int cheat[], int M) {
    int x;
    for(int i = M; i >= (M+1) / 2; i--) {
	if(node[i] == 1) {
	    f[i][1] = 0;
	    f[i][0] = MY_INT_MAX;
	} else {
	    f[i][1] = MY_INT_MAX;
	    f[i][0] = 0;
	}
    }
    for(int i = (M-1) / 2; i >= 1; i--) {
	if (node[i] == AND) {
	    f[i][1] = f[2*i][1] + f[2*i+1][1];
	    f[i][0] = min(
		f[2*i][0] + f[2*i+1][0],
		f[2*i][0] + f[2*i+1][1],
		f[2*i][1] + f[2*i+1][0]
	    );
	    if (cheat[i] == 1) {
		f[i][1] = ((x = min(
		    f[2*i][0] + f[2*i+1][1] + 1,
		    f[2*i][1] + f[2*i+1][0] + 1,
		    f[2*i][1] + f[2*i+1][1] + 1
		)) < f[i][1]) ? x : f[i][1];
		f[i][0] = ((x = f[2*i][0] + f[2*i+1][0] + 1) < f[i][0]) ? x : f[i][0];
	    }
	}
	if (node[i] == OR) {
	    f[i][1] = min(
		f[2*i][0] + f[2*i+1][1],
		f[2*i][1] + f[2*i+1][0],
		f[2*i][1] + f[2*i+1][1]
	    );
	    f[i][0] = f[2*i][0] + f[2*i+1][0];
	    if (cheat[i] == 1) {
		f[i][0] = ((x = min(
		    f[2*i][0] + f[2*i+1][0] + 1,
		    f[2*i][0] + f[2*i+1][1] + 1,
		    f[2*i][1] + f[2*i+1][0] + 1
		)) < f[i][0]) ? x : f[i][0];
		f[i][1] = ((x = f[2*i][1] + f[2*i+1][1] + 1) < f[i][1]) ? x : f[i][1];
	    }
	}
    }
    return;
}
int main() {
    int N, M, V, G, C;
    int node[10001], cheat[10001];
    scanf("%d", &N);
    for(int i = 1; i <= N; i++) {
	scanf("%d %d", &M, &V);
	for(int j = 1; j <= (M-1) / 2; j++) {
	    scanf("%d %d", &G, &C);
	    node[j] = G;
	    cheat[j] = C;
	}
	for(int j = (M+1) / 2; j <= M; j++) {
	    scanf("%d", &node[j]);
	}
	g(node, cheat, M);
	if (f[1][V] < MY_INT_MAX) {
	    printf("Case #%d: %d\n", i, f[1][V]);
	} else {
	    printf("Case #%d: IMPOSSIBLE\n", i);
	}
    }
    return 0;
}
/*
int f(int node[], int cheat, int M, int k, int V) {
    
    if (k <= (M-1) / 2) {   // internal
	if (V == 1 && node[k] == AND) {
	    f(node, cheat, M, k*2, 1) + f(node, cheat, M, k*2+1, 1)
	    if (cheat[k] == 1) {
		f(node, cheat, M, k*2, 0) + f(node, cheat, M, k*2+1, 1) + 1
		f(node, cheat, M, k*2, 1) + f(node, cheat, M, k*2+1, 0) + 1
		f(node, cheat, M, k*2, 1) + f(node, cheat, M, k*2+1, 1) + 1
	    }
	}
	if (V == 1 && node[k] == OR) {
	    f(node, cheat, M, k*2, 0) + f(node, cheat, M, k*2+1, 1)
	    f(node, cheat, M, k*2, 1) + f(node, cheat, M, k*2+1, 0)
	    f(node, cheat, M, k*2, 1) + f(node, cheat, M, k*2+1, 1)
	    if (cheat[k] == 1) {
		f(node, cheat, M, k*2, 1) + f(node, cheat, M, k*2+1, 1) + 1
	    }
	}
	if (V == 0 && node[k] == AND) {
	    f(node, cheat, M, k*2, 0) + f(node, cheat, M, k*2+1, 0)
	    f(node, cheat, M, k*2, 0) + f(node, cheat, M, k*2+1, 1)
	    f(node, cheat, M, k*2, 1) + f(node, cheat, M, k*2+1, 0)
	    if (cheat[k] == 1) {
		f(node, cheat, M, k*2, 0) + f(node, cheat, M, k*2+1, 0) + 1
	    }
	}
	if (V == 0 && node[k] == OR) {
	    f(node, cheat, M, k*2, 0) + f(node, cheat, M, k*2+1, 0)
	    if (cheat[k] == 1) {
		f(node, cheat, M, k*2, 0) + f(node, cheat, M, k*2+1, 0) + 1
		f(node, cheat, M, k*2, 0) + f(node, cheat, M, k*2+1, 1) + 1
		f(node, cheat, M, k*2, 1) + f(node, cheat, M, k*2+1, 0) + 1
	    }
	}
    }
}
*/
