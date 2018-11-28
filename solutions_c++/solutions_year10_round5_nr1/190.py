#include <stdio.h>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <utility>
#include <math.h>

using namespace std;

#define lint long long

#define sz size()
#define pb push_back

#define FOR(i,n) SFOR(i,0,n)
#define SFOR(i,m,n) for(i=m;i<n;i++)
#define FORD(i,n) for(i=n-1;i>=0;i--)

lint K[20];

int P[1000000];
int sp;
int AA[1000000];

lint MMod(lint q, int w) {
	if (q > 0) return q % w;
	q = (-q) % w;
	q = (w - q) % w;
	return q;
}

lint ans;

void Mans(lint q) {
	if (ans == -1) ans = q;
	if (ans == q) return;
	ans = -2;
}

lint obr (lint q, lint w) {
	lint w0 = w;
	q = MMod(q, w);
	lint a1, b1, a2, b2, k;
	a1 = b2 = 1;
	a2 = b1 = 0;
	while (q != 1) {
		k = w/q;
		w %= q;
		a2 -= k*a1;
		b2 -= k*b1;
		swap(a1,a2);
		swap(b1,b2);
		swap(q, w);
	}
	return MMod(a1, w0);
}

int main() {
	int t,tt,i,j,k,p,q;
	int N, T;
	int x1, x2, y1, y2, DD;
	lint A, B, D;
	memset(AA,0,sizeof(AA));
	AA[0] = AA[1] = 1;
	sp = 0;
	FOR(i,1000000) if (AA[i] == 0) {
		P[sp] = i;
		sp++;
		j = 2;
		while (i*j < 1000000) { AA[i*j] = 1; j++; }
	}
	FILE *fp = fopen("A.in", "r");
	FILE *fp1 = fopen("A.out", "w");
	fscanf(fp, "%d", &tt);
	FOR(t,tt) {
		ans = -1;
		fscanf(fp,"%d%d",&DD,&k);
		D = 1;
		FOR(i,DD) D *= 10;
		FOR(i,k) fscanf(fp,"%d",&K[i]);
		fprintf(fp1,"Case #%d: ", t+1);
		if ((k != 1) && (K[0] == K[1])) { fprintf(fp1, "%d\n", K[0]); continue; }
		if ((k > 2) && (K[1] == K[2])) { fprintf(fp1, "%d\n", K[1]); continue; }
		if (k < 2) {
			fprintf(fp1, "I don't know.\n");
		}
		else {
			ans = -1;
			FOR(p, sp) {
				if (P[p] >= D) break;
				FOR(i,k) if (K[i] >= P[p]) break;
				if (i != k) continue;
				A = MMod((K[2] - K[1]) * obr(K[1] - K[0], P[p]), P[p]);
				B = MMod(K[1] - A*K[0], P[p]);
				FOR(i,k-1) if (MMod(A*K[i] + B, P[p]) != K[i+1]) break;
				if (i != k-1) continue;
				Mans(MMod(A*K[k-1] + B, P[p]));
				if (ans == -2) break;
			}
			if (ans == -2) fprintf(fp1, "I don't know.\n"); else fprintf(fp1, "%lld\n", ans);
		}
	}
	fclose(fp);
	fclose(fp1);
	return 0;
}