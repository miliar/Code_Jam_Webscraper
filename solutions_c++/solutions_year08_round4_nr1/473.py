#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int M,desiredV,M1;
bool V[10002];
bool C[10002], G[10002];
int r[10002][2];
bool visited[10002][2];

inline int min(int a, int b) {
	if(a==-1) {
		return b;
	}
	if(b==-1) {
		return a;
	}
	return a < b ? a : b;
}

int changes_for(int node, bool value) {
	if(node > M) {
		return -1;
	}
	if(visited[node][value]) {
		return r[node][value];
	}
	if(node > M1) {
		// I'm in a leaf
		if(value == V[node]) {
			visited[node][value] = true;
			r[node][value] = 0;
			return 0; // no change
		} else {
			visited[node][value] = true;
			r[node][value] = -1;
			return -1; // impossible
		}
	}
	int l0,l1,r1,r0,rAND = -1, rOR = -1;
	l0 = changes_for(2*node, false);
	l1 = changes_for(2*node, true);
	r0 = changes_for(2*node+1, false);
	r1 = changes_for(2*node+1, true);
//	printf("node: %d, %d: %d, l1: %d, r0: %d, r1: %d\n", node, value?1:0, l0, l1, r0, r1);
	if(value) {
		// we need a 1
		if(l1!=-1 && r1!=-1) {
			if(rAND==-1 || rAND>l1+r1) {
				rAND = l1+r1;
			}
		}
	} else {
		// we need a 0
		if(l0!=-1 && r0!=-1) {
			if(rAND==-1 || rAND>l0+r0) {
				rAND = l0+r0;
			}
		}
		if(l0!=-1 && r1!=-1) {
			if(rAND==-1 || rAND>l0+r1) {
				rAND = l0+r1;
			}
		}
		if(l1!=-1 && r0!=-1) {
			if(rAND==-1 || rAND>l1+r0) {
				rAND = l1+r0;
			}
		}
	}
	
	// OR gate
	if(value) {
		// we need a 1
		if(l0!=-1 && r1!=-1) {
			if(rOR==-1 || rOR>l0+r1) {
				rOR = l0+r1;
			}
		}
		if(l1!=-1 && r0!=-1) {
			if(rOR==-1 || rOR>l1+r0) {
				rOR = l1+r0;
			}
		}
		if(l1!=-1 && r1!=-1) {
			if(rOR==-1 || rOR>l1+r1) {
				rOR = l1+r1;
			}
		}
	} else {
		// we need a 0
		if(l0!=-1 && r0!=-1) {
			if(rOR==-1 || rOR>l0+r0) {
				rOR = l0+r0;
			}
		}
	}
//	printf("node: %d, %d, rAND: %d, rOR: %d, type: %d, changeable: %d\n", node, value?1:0, rAND, rOR, G[node]?1:0, C[node]?1:0);
	if(C[node] == 0) {
		// not changeable
		if(G[node] == 1) {
			visited[node][value] = true;
			r[node][value] = rAND;
			return rAND;
		} else {
			visited[node][value] = true;
			r[node][value] = rOR;
			return rOR;
		}
	} else {
		// the node is changeable
		if(G[node] == 1) {
			// AND gate
			if(rOR != -1) {
				visited[node][value] = true;
				r[node][value] = min(rAND, rOR+1);
				return min(rAND, rOR+1);
			} else {
				visited[node][value] = true;
				r[node][value] = rAND;
				return rAND;
			}
		} else {
			// OR gate
			if(rAND != -1) {
				visited[node][value] = true;
				r[node][value] = min(rOR, rAND+1);
				return min(rOR, rAND+1);
			} else {
				visited[node][value] = true;
				r[node][value] = rOR;
				return rOR;
			}
		}
	}
}

void solve(int case_number) {
	int r = changes_for(1, desiredV == 1 ? true : false);
	if(r == -1) {
		printf("Case #%d: IMPOSSIBLE\n", case_number);
		fprintf(stderr, "Case #%d: IMPOSSIBLE\n", case_number);
	} else {
		printf("Case #%d: %d\n", case_number, r);
		fprintf(stderr, "Case #%d: %d\n", case_number, r);
	}
}

int main(void) {
	freopen("A-large.in", "rt", stdin);
	freopen("A.out", "wt", stdout);

	int i, j, T, g, c, v;
	scanf("%d\n",&T);
	for(i=1; i<=T; i++) {
		scanf("%d %d\n", &M, &desiredV);
		for(j=1; j<=M; j++) {
			visited[j][0] = visited[j][1] = false;
		}
		M1 = (M-1) / 2;
		for(j=1; j<=M1; j++) {
			scanf("%d %d\n", &g, &c);
			G[j] = g == 1 ? true : false;
			C[j] = c == 1 ? true : false;
		}
		for(; j<=M; j++) {
			scanf("%d\n", &v);
			V[j] = v == 1 ? true : false;
		}
		solve(i);
	}

	return 0;
}