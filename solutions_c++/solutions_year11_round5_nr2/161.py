#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <cstring>
using namespace std;

#define MAXN 16384
#define MAXM 1024
#define MAX 2048
#define INF 1000000

struct node {
	int p, w, id;
} source[MAXM], sink[MAXM];

struct node2 {
	vector<int> c;
	int prev, best;
} n[MAX];

int F[MAX][MAX], AA[MAX][MAX], ID, SIN, SOU, START, END;

int edmondskarp(int **A, int SOURCE, int SINK) {
	int s[MAX], S, E, FLOW, tmp, it;
	bool v[MAX];

	memset(F, 0, sizeof(F));
	FLOW = 0;
	while (1) {
		memset(v, false, sizeof(v));
		n[SOURCE].best = INF;
		n[SOURCE].prev = -1;
		s[0] = SOURCE; S = 0; E = 1; v[SOURCE] = true;
		while (S != E && s[S] != SINK) {
			for (it=0; it<(int)n[s[S]].c.size(); it++) {
				tmp = n[s[S]].c[it];
				if (v[tmp]==false && A[s[S]][tmp]-F[s[S]][tmp]>0) {
			   	v[tmp] = true;
					n[tmp].prev = s[S];
					n[tmp].best = min(n[s[S]].best, A[s[S]][tmp] - F[s[S]][tmp]);
					s[E] = tmp;
					E++;
				}
			}
			S++;
		}
		if (S==E) return FLOW;
		else {
		   FLOW += n[SINK].best;
			tmp = SINK;
			while (n[tmp].prev != -1) {
				F[n[tmp].prev][tmp] += n[SINK].best;
				F[tmp][n[tmp].prev] = - F[n[tmp].prev][tmp];
				tmp = n[tmp].prev;
			}
		}
	}
}

void init(int cutoff) {
	int i, j;

	memset(AA, 0, sizeof(AA));
	for (i=0; i<ID; i++) n[i].c.clear();

	for (i=0; i<SOU; i++) {
		n[START].c.push_back(source[i].id);
		AA[START][source[i].id] = source[i].w;
	}
	for (i=0; i<SIN; i++) {
		n[sink[i].id].c.push_back(END);
		AA[sink[i].id][END] = sink[i].w;
	}

	for (i=0; i<SOU; i++) {
		for (j=0; j<SIN; j++) {
			if (sink[j].p - source[i].p > cutoff) {
				n[source[i].id].c.push_back(sink[j].id);
				AA[source[i].id][sink[j].id] = INF;
			}
		}
	}
}

int main() {

freopen("in.txt", "r", stdin);

int N, i, nn[MAXN], tmp, *A[MAX], S, E, M, t, T;

for (i=0; i<MAX; i++) A[i] = AA[i];

cin >> T;

for (t=1; t<=T; t++) {

cin >> N;

memset(nn, 0, sizeof(n));
for (i=0; i<N; i++) {
	cin >> tmp;
	nn[tmp]++;
}

SOU = SIN = ID = 0;
for (i=1; i<MAXN; i++) {
	if (nn[i] > nn[i-1]) {
		source[SOU].p = i;
		source[SOU].w = nn[i] - nn[i-1];
		source[SOU].id = ID++;
		SOU++;
	} else if (nn[i] < nn[i-1]) {
		sink[SIN].p = i;
		sink[SIN].w = nn[i-1] - nn[i];
		sink[SIN].id = ID++;
		SIN++;
	}
}
START = ID++;
END = ID++;

init(0);

int OBJ = edmondskarp(A, START, END);

cout << "Case #" << t << ": ";

S = 0; E = INF;
while (E-S > 1) {
	M = (S+E)/2; init(M);
	if (edmondskarp(A, START, END) < OBJ) E = M;
	else S = M;
}
if (S+1 == INF) cout << 0 << endl;
else cout << S+1 << endl;

}

return 0;
}
