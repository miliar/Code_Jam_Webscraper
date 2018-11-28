#include <stdio.h>
#include <string.h>

#include <iostream>

using namespace std;

#define TRACE(x) 
#define DEBUG(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x << " = " << x << endl)

#define MSET(c, v) memset(c, v, sizeof(c))

const int MAX = 10010;
const int AND_GATE = 1;
const int OR_GATE = 0;
const int INF = 0x3f3f3f3f;

int gate[MAX], change[MAX], value[MAX];
int memo[MAX][2][2];
int M;

int solve(int x, int v, int inv=0) {
	int &m = memo[x][v][inv];
	if (m != -1) return m;

	if (x >= (M-1)/2) {
		DEBUG("%d eh folha\n", x);
		if (value[x] == v) return m=0;
		else return m=-2;
	}

	int left = 2*x+1;
	int right = 2*x+2;

	/*
	int rl = solve(left, 1);
	int rr = solve(right, 1);
	int rl0 = solve(left, 0);
	int rr0 = solve(right, 0);
	*/
	int and_ret = INF, or_ret = INF, inv_ret = INF;

	int G = gate[x];
	if (inv) G = 1-G;

	// calc
	if (G == AND_GATE) {
		if (v) {
			int rl = solve(left, 1);
			int rr = solve(right, 1);

			if (rl < 0 || rr < 0) and_ret = -2;
			else and_ret = rl+rr;
		}
		else {
			int rl = solve(left, 0);
			int rr = solve(right, 0);

			if (rl < 0 && rr < 0) and_ret = -2;
			else if (rl < 0) and_ret = rr;
			else and_ret = rl;
		}
	}
	else { // OR_GATE
		if (v) {
			int rl = solve(left, 1);
			int rr = solve(right, 1);
			if (rl < 0 && rr < 0) or_ret = -2;
			else if (rl < 0) or_ret = rr;
			else or_ret = rl;
		}
		else {
			int rl = solve(left, 0);
			int rr = solve(right, 0);

			if (rl < 0 || rr < 0) or_ret = -2;
			else or_ret = rl+rr;
		}
	}

	/*
	// calc
	if (G == AND_GATE) {
		if (rl < 0 || rr < 0) {
			if (v) and_ret = -2;
			else and_ret = 0;
		}
		else {
			if (v) and_ret = rl+rr;
			else {
				if (rl0 < 0 && rr0 < 0) and_ret = -2;

				if (rl0 == -2) rl0 = INF;
				if (rr0 == -2) rr0 = INF;

				else and_ret = min(rl0, rr0);
				if (and_ret == INF) and_ret = -2;
			}
		}
	}
	else { // OR_GATE
		if (v) {
			if (rl < 0 && rr < 0) or_ret = -2;
			else {
				if (rl < 0) or_ret = rr;
				else if (rr < 0) or_ret = rl;
				else or_ret = min(rl, rr);
			}
		}
		else {
			if (rl0 < 0 || rr0 < 0) or_ret = -2;
			else or_ret = rl0+rr0;
		}
	}
	*/
	if (!inv && change[x]) inv_ret = solve(x, v, 1)+1;

	if (and_ret < 0) and_ret = INF;
	if (or_ret < 0) or_ret = INF;
	if (inv_ret < 0) inv_ret = INF;

	int ret = min(and_ret, min(or_ret, inv_ret));
	WATCH(x); WATCH(and_ret); WATCH(or_ret); WATCH(inv_ret); WATCH(ret);
	if (ret == INF) return m = -2;
	return m = ret;
}

int main() {
	int N;
	scanf(" %d", &N);
	for (int _42=1; _42 <= N; _42++) {
		int V;
		scanf(" %d %d", &M, &V);

		MSET(gate, -1);
		MSET(change, -1);
		MSET(value, -1);
		MSET(memo, -1);

		// read
		for (int i=0; i < (M-1)/2; i++) {
			scanf(" %d %d", &gate[i], &change[i]);
		}
		for (int i=(M-1)/2; i < M; i++) {
			scanf(" %d", &value[i]);
		}

		// calc
		/*
		if (V == 0) { // inverte tudo
			for (int i=0; i < M; i++) {
				if (value[i] >= 0) value[i] = 1-value[i];
			}
		}
		*/
		int r = solve(0, V);
		
		printf("Case #%d: ", _42);
		if (r < 0) printf("IMPOSSIBLE\n");
		else printf("%d\n", r);
		DEBUG("\n");
	}


	return 0;
}

